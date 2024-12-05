try:
    divisor = int(input("Ingresa un numero divisor: "))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser cero")
    print("Ha ocurrido un error: ", e)
except ValueError as e:
    print("Error: Debes introducir un número válido ")
    print("Ha ocurrido un error: ", e)
except IndexError as e:
    print("Error: Intentas acceder a un índice fuera del rango de una lista o una secuencia")
    print("Ha ocurrido un error: ", e)
except KeyError as e:
    print("Error: Intentas acceder a una clave que no existe en un diccionario")
    print("Ha ocurrido un error: ", e)
except TypeError as e:
    print("Error: Operar con tipos incompatibles (por ejemplo, sumar una cadena con un número).")
    print("Ha ocurrido un error: ", e)
except NameError as e:
    print("Error: Estas intentado usar una variable que no ha sido definida")
    print("Ha ocurrido un error: ", e)
except AttributeError as e:
    print("Error: Estas intentado acceder a un atributo que no existe en un objeto")
    print("Ha ocurrido un error: ", e)
except ImportError as e:
    print("Error: Estas intentado importar un modulo que no existe")
    print("Ha ocurrido un error: ", e)
except ModuleNotFoundError as e:
    print("Error: Estas intentado importar un modulo que no existe")
    print("Ha ocurrido un error: ", e)
except FileNotFoundError as e:
    print("Error: Estas intentado abrir un archivo que no existe")
    print("Ha ocurrido un error: ", e)
except IOError as e:
    print("Error: Error de entrada/salida")
    print("Ha ocurrido un error: ", e)
except StopIteration as e:
    print("Error: Error de iteración")
    print("Ha ocurrido un error: ", e)
except MemoryError as e:
    print("Error: Falta de memoria para completar la operación")
    print("Ha ocurrido un error: ", e)
except OverflowError as e:
    print("Error: Resultado de una operación aritmética que excede el rango permitido.")
    print("Ha ocurrido un error: ", e)
except IndentationError as e:
    print("Error: Error de indentación en el código")
    print("Ha ocurrido un error: ", e)
except SyntaxError as e:
    print("Error: Error de sintaxis en el código")
    print("Ha ocurrido un error: ", e)
except RuntimeError as e:
    print("Error: Error de tiempo de ejecución ocasionado por una operación que no puede ser realizada")
    print("Ha ocurrido un error: ", e)
except NotImplementedError as e:
    print("Error: Método o función que no está implementado")
    print("Ha ocurrido un error: ", e)
except UnboundLocalError as e:
    print("Error: Estas intentando acceder a una variable local que no ha sido definida")
    print("Ha ocurrido un error: ", e)
except AssertionError as e:
    print("Error: Fallo de una declaración assert")
    print("Ha ocurrido un error: ", e)
except Exception as e:
    print("Error: Se ocasiona cuando se produce un error que no es manejado por ninguna de las excepciones anteriores")
    print("Ha ocurrido un error: ", e)

# Documentacion de excepciones en python
# https://docs.python.org/es/3/tutorial/errors.html
# https://docs.python.org/es/3/tutorial/controlflow.html#pass

# exceptions
# https://docs.python.org/3/library/exceptions.html