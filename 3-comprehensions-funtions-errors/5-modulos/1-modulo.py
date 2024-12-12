import sys
print(sys.path) # C:\Users\Usuario\Documents\Python\3-comprehensions-funtions-errors\5-modulos

import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)
print(result) # ['311', '123', '121', '57', '3']

import time
timestamp = time.time()
print(timestamp) # 1620000000.0

local = time.localtime()
result = time.asctime(local)
print(result) # Tue May 04 20:00:00 2021

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter) # Counter({1: 4, 2: 2, 3: 2, 4: 1, 5: 1, 21: 1})