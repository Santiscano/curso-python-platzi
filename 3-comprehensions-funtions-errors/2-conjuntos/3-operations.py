# operaciones con conjuntos
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# union
set_c = set_a.union(set_b)
print(set_c) # {'col', 'mex', 'bol', 'pe'}
print(set_a | set_b) # {'col', 'mex', 'bol', 'pe'} - une los dos conjuntos

# interseccion
set_c = set_a.intersection(set_b)
print(set_c) # {'bol'}
print(set_a & set_b) # {'bol'} - solo los elementos comunes

# diferencia
set_c = set_a.difference(set_b)
print(set_c) # {'col', 'mex'} - los elementos que estan en el conjunto a pero no en el b
print(set_a - set_b) # {'col', 'mex'} - solo los elementos que no estan en el otro conjunto

# diferencia simetrica
set_c = set_a.symmetric_difference(set_b)
print(set_c) # {'col', 'mex', 'pe'}
print(set_a ^ set_b) # {'col', 'mex', 'pe'} - solo los elementos que no estan en ambos conjuntos

# subconjunto
set_c = {'col', 'mex'}
print(set_c.issubset(set_a)) # True
print(set_c.issubset(set_b)) # False - si todos los elementos de un conjunto estan en otro

# superconjunto
print(set_a.issuperset(set_c)) # True
print(set_b.issuperset(set_c)) # False - si todos los elementos de un conjunto estan en otro

# agregar elementos
set_a.add('pe')
print(set_a) # {'col', 'mex', 'bol', 'pe'}

# eliminar elementos
set_a.remove('pe')
print(set_a) # {'col', 'mex', 'bol'} 

# eliminar todos los elementos
set_a.clear()
print(set_a) # set()

# eliminar un elemento aleatorio
set_a = {'col', 'mex', 'bol'}
set_a.pop()
print(set_a) # {'mex', 'bol'}

# copiar un conjunto
set_a_copy = set_a.copy()
print(set_a_copy) # {'mex', 'bol'}

# eliminar un conjunto
del set_a_copy
# print(set_a_copy) # NameError: name 'set_a_copy' is not defined

# iterar un conjunto
for element in set_a:
    print(element)