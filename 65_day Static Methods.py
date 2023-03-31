class Math:
    def __init__(self,num):
        self.num = num
    


    @staticmethod
    def add(a,b):
        return a+b

a=Math(5)
print(a.add(3,6))