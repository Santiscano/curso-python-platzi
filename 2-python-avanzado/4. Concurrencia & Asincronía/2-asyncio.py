import asyncio

async def process_data(data):
    print(f'Procesando {data}...')
    await asyncio.sleep(10) # Simula un proceso de 10 segundos
    print(f'{data} completado')
    return data * 2

async def main():
    # Crear una lista de tareas
    tasks = [process_data(i) for i in range(3)]
    
    # Ejecutar las tareas en paralelo
    results = await asyncio.gather(*tasks)
    print(f'Resultados: {results}')