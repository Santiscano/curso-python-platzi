import asyncio
import time
import random
import multiprocessing

# Función asíncrona para verificar el inventario
async def check_inventory(item):
    print(f"Verificando inventario para {item}...")
    await asyncio.sleep(random.randint(3, 6))  # Simula una operación de verificación
    print(f"Inventario verificado para {item}")
    # Simular disponibilidad del producto
    return random.choice([True, False])

# Función asíncrona para procesar el pago
async def process_payment(order_id):
    print(f"Procesando pago para la orden {order_id}...")
    # simular tiempo de espera que tiene un servicio de pago
    await asyncio.sleep(random.randint(3, 6))
    print(f"Pago completado para la orden {order_id}")
    return True

# Función intensiva en CPU para calcular el costo total del pedido
def calculate_total(items):
    print(f"Calculando costo total para {len(items)} articulos...")
    time.sleep(random.randint(3, 6))  # Simula una operación intensiva en CPU
    total = sum(item['price'] for item in items)
    print(f"Costo total calculado: ${total}")
    return total



# Función principal para procesar un pedido en línea
async def process_order(order_id, items):
    print(f"Iniciando procesamiento para la orden {order_id}...")
    # Verificar la disponibilidad de los artículos
    inventory_check = [check_inventory(item['name']) for item in items]
    inventory_results = await asyncio.gather(*inventory_check)
    if not all(inventory_results):
        print(f"Algunos artículos no están disponibles para la orden {order_id}")
        return
    
    # Si todos los artículos están disponibles, calcular el costo total
    with multiprocessing.Pool() as pool:
        total = await pool.apply_async(calculate_total, (items,))
    
    # Procesar el pago
    payment_result = await process_payment(order_id)
    
    if payment_result:
        print(f"Orden {order_id} procesada exitosamente. Costo total: ${total}")
    else:
        print(f"Error al procesar el pago para la orden {order_id}")



async def main():
    # Crear tres pedidos de ejemplo
    orders = [
        {'order_id': 1, 'items': [{'name': 'Laptop', 'price': 1000}, {'name': 'Mouse', 'price': 20}]},
        {'order_id': 2, 'items': [{'name': 'Monitor', 'price': 300}, {'name': 'Keyboard', 'price': 50}]},
        {'order_id': 3, 'items': [{'name': 'Headphones', 'price': 100}, {'name': 'Webcam', 'price': 80}]}
    ]
    # procesar múltiples pedidos en paralelo
    tasks = [process_order(order['order_id'], order['items']) for order in orders]
    await asyncio.gather(*tasks) # Esperar a que todos los pedidos se completen, corre en paralelo


# Ejecutar el bucle de eventos de asyncio
if __name__ == "__main__":
    asyncio.run(main())