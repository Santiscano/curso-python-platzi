# ciclo for
numbers = []
for element in range(1, 11):
    numbers.append(element * 2)
print(numbers)

# List comprehension
numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)



# ciclo for con condicional
numbers_if = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers_if.append(i * 2)
print(numbers_if)

numbers_if_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_if_v2)