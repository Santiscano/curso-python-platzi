import os

try:
    file_path = os.path.join(os.path.dirname(__file__), 'text.txt')
    # con r+ se puede leer y escribir. 
    # con w+ se puede escribir y leer, pero se sobreescribe el archivo
    with open(file_path, 'w+') as file: 
        for line in file:
            print(line)
        file.write('nuevas cosas en este archivo\n')
        file.write('otra linea\n')
        file.write('mas lineas\n')
except FileNotFoundError:
    print("El archivo 'text.txt' no se encontró. Verifica la ruta del archivo.")