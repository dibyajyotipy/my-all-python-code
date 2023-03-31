class MyClass:
  def __init__(self, value):
      self._value = value
    
  def show(self):
    print(f"Value is {self._value}")
    
  @property                         #Getter
  def ten_value(self):
      return 10* self._value
    
  @ten_value.setter                 #Setter
  def ten_value(self, new_value):
      self._value = new_value/10

a = MyClass(10)
a.ten_value = 67
print(a.ten_value)
a.show()