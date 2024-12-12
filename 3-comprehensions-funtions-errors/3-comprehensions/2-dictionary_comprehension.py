import random

#* ciclo for
dict = {}
for i in range(1, 5):
    dict[i] = i * 2
print(dict) # {1: 2, 2: 4, 3: 6, 4: 8}

#* dictionary comprehension
dict_v2 = { i: i * 2 for i in range(1, 5)}
print(dict_v2) # {1: 2, 2: 4, 3: 6, 4: 8}

#* ejemplo 2
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population) # {'col': 45, 'mex': 67, 'bol': 34, 'pe': 56}

#* dictionary comprehension
population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2) # {'col': 45, 'mex': 67, 'bol': 34, 'pe': 56}

#* ejemplo 3
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]
# zip hace una tuplas a partir de dos listas
print(zip(names, ages)) # <zip object at 0x7f8b1c3b7d00>
print(list(zip(names, ages))) # [('nico', 12), ('zule', 56), ('santi', 98)]

#* dictionary comprehension
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict) # {'nico': 12, 'zule': 56, 'santi': 98}

#* ciclo for con condicional
result_if = {}
for (country, population) in population_v2.items():
    if population > 50:
        result_if[country] = population
print(result_if) # {'mex': 67, 'pe': 56}

#* dictionary comprehension con condicional
result_if_v2 = { country: population for (country, population) in population_v2.items() if population > 50 }
print(result_if_v2) # {'mex': 67, 'pe': 56}


# ejemplo 4
text = 'Hola, soy Santiago'
unique_if = {}
for c in text:
    if c in 'aeiou':
        unique_if[c] = c.upper()
print(unique_if) # {'o': 'O', 'a': 'A', 'i': 'I', 'o': 'O', 'a': 'A', 'o': 'O'}

unique_if_v2 = { c: c.upper() for c in text if c in 'aeiou' }
print(unique_if_v2) # {'o': 'O', 'a': 'A', 'o': 'O', 'a': 'A', 'i': 'I', 'a': 'A', 'o': 'O'}