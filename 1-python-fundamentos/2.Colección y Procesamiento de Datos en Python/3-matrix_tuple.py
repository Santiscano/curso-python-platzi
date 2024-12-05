matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[2][1])
numbers = (1,2,3,4,5) # tupla - son inmutables, solo son de lectura
numbers_2 = 1,2,3,4,5 # forma 2 de escribir una tupla
print(numbers)
print(type(numbers))
print(numbers[0])
#numbers[0] = 'unos'
#print(numbers)


matrix2 = [
    [
        [1,2,3],[4,5,6],[7,8,9]
    ],
    [
        [10,11,12],[13,14,15],[16,17,18]
    ],
]
numberTen = matrix2[1][0][0]
numberEight = matrix2[0][2][1]