class Employee:
    def  __init__(self,name,id):
        self.name = name
        self.id = id
    
    def info(self):
        print(f"The name of employee {self.id} is {self.name}")

class Programer (Employee):
    def lang (self):
        print("The default language is Python")

e1 = Programer("Dib", 69)
e1.info()
e1.lang()