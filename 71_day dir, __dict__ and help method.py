x = [1,2,3,4]
print(dir(x))

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p = Person("Dib", 19)
print(p.__dict__)

print(help(Person))