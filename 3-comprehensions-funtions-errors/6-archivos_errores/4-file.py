import os

try:
    file_path = os.path.join(os.path.dirname(__file__), 'text.txt')
    print('path: ',file_path)
    file = open(file_path)
    print(file.read()) # Lee todo el archivo
    # print(file.readline()) # Lee una linea
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())

    for line in file:
        print(line)
    file.close()
    
    with open(file_path) as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("El archivo 'text.txt' no se encontró. Verifica la ruta del archivo.")