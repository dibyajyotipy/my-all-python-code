class employee:
    def __init__(self,name,id):
        self.name = name
        self.id=id
    
class programer(employee):
    def __init__(self, name, id , lang):
        super().__init__(name,id)
        self.lang=lang

e = employee("Harry ", 554)
p = programer("Dib",558,"Python")
print(e.name)
print(p.name)