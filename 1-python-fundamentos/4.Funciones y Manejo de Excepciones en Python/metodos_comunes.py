# para cadenas de texto
str = "Hola Mundo"
# str.upper(): Convierte una cadena a mayúsculas.
# str.lower(): Convierte una cadena a minúsculas.
# str.capitalize()` Convierte el primer carácter a mayúscula y el resto a minúsculas.
# str.split(sep=None): Divide una cadena en una lista, usando el separador `sep`.
# str.join(iterable): Une una lista o iterable en una sola cadena, usando el string como separador.
# str.strip(): Elimina espacios en blanco (u otros caracteres) al inicio y final de la cadena.
# str.replace(old, new): Reemplaza todas las ocurrencias de una subcadena `old` por `new`.
# str.find(sub): Busca la subcadena `sub` y devuelve la posición de su primera aparición, o `1` si no la encuentra.

# Metodos para listas
list = [1, 2, 3, 4, 5]
# list.append(item): Agrega un elemento al final de la lista.
# list.extend(iterable): Agrega todos los elementos de un iterable al final de la lista.
# list.insert(index, item): Inserta un elemento en una posición específica.
# list.remove(item): Elimina la primera aparición de un elemento en la lista.
# list.pop(index=-1): Elimina y devuelve el elemento en la posición `index` (el último por defecto).
# list.index(item): Devuelve el índice de la primera aparición de un elemento.
# list.sort(): Ordena la lista en orden ascendente.
# list.reverse(): Invierte el orden de los elementos en la lista.


# Metodos para diccionarios
dict = {'nombre': 'Juan', 'edad': 23}
# dict.get(key, default=None): Devuelve el valor asociado a la clave `key`, o `default` si la clave no existe.
# dict.keys(): Devuelve una vista de todas las claves del diccionario.
# dict.values(): Devuelve una vista de todos los valores del diccionario.
# dict.items(): Devuelve una vista de todos los pares clave-valor del diccionario.
# dict.update(other_dict): Actualiza el diccionario con los pares clave-valor de otro diccionario.
# dict.pop(key, default=None): Elimina y devuelve el valor asociado a la clave `key`.

# Metodos de conjuntos
set = {1, 2, 3}
# set.add(item): Agrega un elemento al conjunto.
# set.remove(item): Elimina un elemento del conjunto. Lanza un error si el elemento no está presente.
# set.discard(item): Elimina un elemento sin lanzar un error si no está presente.
# set.union(other_set): Devuelve un nuevo conjunto con los elementos de ambos conjuntos.
# set.intersection(other_set): Devuelve un conjunto con los elementos comunes entre ambos conjuntos.
# set.difference(other_set): Devuelve un conjunto con los elementos presentes en el conjunto original pero no en `other_set`.


# Metodos para archivos
file = open('archivo.txt', 'w')
# open(filename, mode): Abre un archivo y lo devuelve como un objeto de archivo.
# file.read(): Lee todo el contenido del archivo.
# file.readline(): Lee una línea del archivo.
# file.readlines(): Lee todas las líneas del archivo y las devuelve como una lista.
# file.write(string): Escribe una cadena en el archivo.
# file.writelines(lines): Escribe una lista de cadenas en el archivo.
# file.close(): Cierra el archivo.


# Metodos para manejo de excepciones
# try: Comienza un bloque de código que podría generar una excepción.
# except: Se ejecuta si ocurre una excepción dentro del bloque `try`.
# finally: Se ejecuta independientemente de si se produce una excepción o no.
# raise: Lanza una excepción manualmente.


# Funciones generales
# len(obj): Devuelve la longitud de un objeto (lista, cadena, etc.).
# type(obj): Devuelve el tipo de un objeto.
# isinstance(obj, class): Verifica si un objeto es una instancia de una clase.
# sum(iterable): Devuelve la suma de los elementos de un iterable.
# max(iterable): Devuelve el valor máximo de un iterable.
# min(iterable): Devuelve el valor mínimo de un iterable.
# range(start, stop, step): Genera una secuencia de números desde `start` hasta `stop`, con un incremento de `step`.
# zip(iter1, iter2): Combina dos iterables en una lista de tuplas.
# map(func, iterable): Aplica una función a cada elemento de un iterable.
# filter(func, iterable): Filtra los elementos de un iterable según una función.
