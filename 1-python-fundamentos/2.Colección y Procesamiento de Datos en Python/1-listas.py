to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
numbers = [1,2,3,4, "cinco"]
print(type(numbers))
mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Ultimo elemento:", mix[-1])
string = "Hola mundo"
print("Primer elemento", string[0])
print("Segundo elemento", string[1])
print("Ultimo elemento:", string[-1])
print(mix[2:-2])
print(mix)
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"]) # inserta en la posición indicada, en este caso en la posición 1
print(mix)
print(mix.index(["a","b"])) # indica la primer aparición
numbers = [1,2,100.01,90.45,3,4, 5]
print(numbers)
print("Mayor:",max(numbers)) # devuelve el mayor número
print("Menor:",min(numbers)) # devuelve el menor número
del numbers[-1] # elimina el último elemento
print(numbers)
del numbers[:2] # elimina los dos primeros elementos
print(numbers)
del numbers # elimina la lista completa
# print(numbers)
