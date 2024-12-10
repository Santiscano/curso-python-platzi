from collections import deque

# Crear una deque
d = deque([1, 2, 3])

# Agregar elementos
d.append(4)       # Agregar al final
d.appendleft(0)   # Agregar al inicio

# Eliminar elementos
d.pop()           # Quitar del final
d.popleft()       # Quitar del inicio

print(d)  # deque([1, 2, 3])
