# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

#Leer un archivo línea por línea
"""with open('caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#Leer todas las líneas en una lista
"""with open('caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)"""

# contar las líneas de un archivo
with open('caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(len(lines))


#Añadir texto - a hace referencia a append
"""with open('caperucita.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")"""

#Sobreescribir el texto
with open('caperucita.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")