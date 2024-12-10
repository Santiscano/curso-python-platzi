#Desempaquetado args
def add(a, b, c):
    return a + b + c

values = (1, 2, 3)
print(add(*values)) 

def show_info(name, age):
    print(f"Name: {name}, Age: {age}")

data = {"name": "Ana", "age": 28}
show_info(**data)


# cantidades indefinidas de argumentos
def sum_numbers(*args):
    return sum(args)

numbers = (1, 2, 3, 4, 5)
print(sum_numbers(*numbers))

# Desempaquetado kwargs
def show_dates(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

data = {"name": "Ana", "age": 28, "city": "Medellin"}
show_dates(**data)