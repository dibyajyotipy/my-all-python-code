class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0], string.split("-")[1])

string = "Dib-19"
e1 = Employee.fromStr(string)
print(e1.name,e1.age)
