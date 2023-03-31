class Employee:
    no_employee = 0
    def __init__(self,name):
        self.name = name
        Employee.no_employee +=1
    def showDetail(self):
        print(f"The name of employee {self.no_employee} is {self.name}")


em1 = Employee("Harry")
em1.showDetail()
em2 = Employee("Dibyajyoti")
em2.showDetail()