# Public 
class employee:
    def __init__(self,name):
        self.name = name
e = employee("dibyajyoti")
print(e.name)



# Private
class employee1:
    def __init__(self,name):
        self.__name = name  
e2 = employee1("Suman")
# print(e2.__name)          Cannot acessiable direcly
print(e2._employee1__name)  #Can be access indirecly



#Proctected
class employee3:
    def __init__(self,name):
        self._name = name
e3=employee3("Puja")
print(e3._name)