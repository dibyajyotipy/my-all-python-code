class Person:
    def __init__(self,name,occ):
        print("Hay iam a person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is {self.occ}")


a = Person("Harry", "Developer")
b = Person("Shraddha", "HR")
a.info()
b.info()