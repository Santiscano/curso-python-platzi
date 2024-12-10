from collections import defaultdict # establece un valor por defecto para las claves que no existen

def count_products(orders: list[str]) -> defaultdict:
    #Crea un diccionario con valor por defecto 0 
    product_count = defaultdict(int) # si existiera una clave que no existe, se le asigna un valor por defecto que seria en este caso 0
    for product in orders:
        product_count[product] +=1
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count)