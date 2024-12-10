from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Crear un ChainMap
cm = ChainMap(dict1, dict2)

print(cm['a'])  # 1 (de dict1)
print(cm['b'])  # 2 (el primero encontrado)
print(cm['c'])  # 4 (de dict2)
