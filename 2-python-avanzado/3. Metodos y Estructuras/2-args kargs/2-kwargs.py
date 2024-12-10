# kwargs: keyword arguments - se usan cuando no se tiene la cantidad de argumentos, y estos seran pasados como un diccionario
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_info(name='Carlos', age=30, city='Bogotá')
print_info(name='Carlos', age=30, city='Bogotá', country = 'Colombia')