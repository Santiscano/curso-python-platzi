# args: argumentos - se usan cuando no se tiene la cantidad de argumentos, y estos seran pasados como una tupla
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1,2,3,4,5))
print(sum_numbers(1,2))
print(sum_numbers(1,2,3,4,5,7,8,9,10))