class Person:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Account(Person):
    def __init__(self, name, code, pay):
        super().__init__(name, code)
        self.mpay = pay
    
class Admin(Person):
    def __init__(self, experience):
        self.exp = experience

class Employee(Admin, Account):
    def __init__(self, name, code, experience, pay):
        Admin.__init__(self, experience)
        Account.__init__(self, name, code, pay)

    def __str__(self):
        return (f"Name: {self.name}\n\
Code: {self.code}\n\
Exp: {self.exp} years\n\
Pay: {self.mpay}")
    
print(Employee.mro())
e = Employee("john doe", 'E007', 4, 200000)
print(e)