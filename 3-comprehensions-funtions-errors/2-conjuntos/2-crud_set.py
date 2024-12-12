set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size) # 3 - cantidad de elementos

print('col' in set_countries) # True - si un elemento esta en el conjunto
print('pe' in set_countries)

# add
set_countries.add('pe')
print(set_countries) # {'col', 'mex', 'bol', 'pe'}
set_countries.add('pe')
print(set_countries) # {'col', 'mex', 'bol', 'pe'} - no se pueden repetir elementos

# update
set_countries.update({'ar', 'ecua', 'pe'}) # update es igual a add pero este permite agregar varios elementos
print(set_countries) # {'col', 'mex', 'bol', 'pe', 'ar', 'ecua'} - agrega varios elementos

# remove, discard, clear
set_countries.remove('col')
print(set_countries) # {'mex', 'bol', 'pe', 'ar', 'ecua'} - elimina un elemento

set_countries.remove('ar') # falla si no existe
set_countries.discard('arg') # no falla si no existe
print(set_countries) # {'mex', 'bol', 'pe', 'ecua'}
set_countries.add('arg')
print(set_countries)
set_countries.clear() # elimina todos los elementos
print(set_countries) # set()
print(len(set_countries)) # 0 - el clear elimina todos los elementos