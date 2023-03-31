class person:
    name = ""
    age = ""
    def info(self):
        print(f"{self.name} age is {self.age}")


a = person()
a.name = "Harry"
a.age = 18
a.info()