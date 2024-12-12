def sum_with_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

result = sum_with_range(1, 10)
print(result)
result_2 = sum_with_range(result, result + 10)
print(result_2)


# ==========================================================
#* Multiple return values
def find_volume(length=1, width=1, depth=1):
    return length * width * depth, width, 'hola'

# forma de asignar los valores de todos los returns
result, width, text = find_volume(width=10)

print(result)
print(width)
print(text)