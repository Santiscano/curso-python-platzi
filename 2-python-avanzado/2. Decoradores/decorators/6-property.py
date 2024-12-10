class Circle:
    def __init__(self, radius:float):
        self._radius = radius
    
    @property # es como si fuera un getter
    def area(self) -> float:
        return 3.1416 * (self._radius **2)
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter # permite modificar el valor de radius
    def radius(self, value: float):
        if value < 0:
            raise ValueError('El radio no puede ser negativo')
        self._radius = value

circle = Circle(5)
#print(circle.area)
circle.radius = -10 # aqui utilizamos el setter
print(circle.area) # aqui utilizamos el getter