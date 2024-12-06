class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello! I am a person.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet() # con super() solo se pueden llamar los metodos de la clase padre
        print(f"Hello, my student ID is {self.student_id}") # con self se pueden llamar los atributos de la clase padre
    
    def nameStudent(self):
        print(f"")

student = Student("Ana", 20, "S123")
student.greet()
    
    