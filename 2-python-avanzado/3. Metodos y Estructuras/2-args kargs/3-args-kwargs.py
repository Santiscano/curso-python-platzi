class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs
    
    def show_employee(self):
        print(f'Employee: {self.name}')
        print('Skills', self.skills) # args son una tupla
        print('Details', self.details) # kwargs son un diccionario

employee = Employee('Carlos', 'Python', 'Java', 'C++', age=30, city = 'Bogotá')
employee.show_employee()

employee2 = Employee('santiago', 'Python', 'Java', 'Javascript', 'php', 'sql', age=32, city='Medellin')
employee2.show_employee()