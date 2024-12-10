from collections import namedtuple

# Definir un namedtuple
Punto = namedtuple('Punto', ['x', 'y'])

# Crear un objeto Punto
p1 = Punto(10, 20)

# Acceder a los valores
print(p1.x)  # 10
print(p1.y)  # 20
