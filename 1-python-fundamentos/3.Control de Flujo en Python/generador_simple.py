def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)


# fibonnacci
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

# Generador de números pares
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)