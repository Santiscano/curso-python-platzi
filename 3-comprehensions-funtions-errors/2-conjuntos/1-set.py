# propiedades de conjuntos
# 1- se pueden modificar
# 2- no tienen orden
# 3- no se pueden acceder por indice
# 4- no se pueden repetir elementos

set_countries = {'col', 'mex', 'bol', 'arg', 'col'}
print(set_countries) # {'col', 'mex', 'bol', 'arg'} - elimino el repetido
print(type(set_countries)) # <class 'set'>

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers) # {1, 2, 23, 443} - elimino el repetido

set_types = {1, 'hola', False, 12.12} 
print(set_types) # {False, 1, 12.12, 'hola'}

set_from_string = set('hoola')
print(set_from_string) # {'o', 'h', 'l', 'a'}

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples) # {'abc', 'cbv', 'as'}

numbers_list = [1,2,3,1,2,3,4]
set_numbers = set(numbers_list)
print(set_numbers) # {1, 2, 3, 4}
unique_numbers = list(set_numbers) 
print(unique_numbers) # [1, 2, 3, 4]

# forma corta de limpiar una lista con set
numbers = [1,2,3,1,2,3,4]
numbers_clean = list(set(numbers))
print(numbers_clean) # [1, 2, 3, 4]
