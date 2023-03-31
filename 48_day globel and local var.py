x=10               #Globel variable
print(f"This is globel variable: {x}")

def my_function():
    y=5           #This is local variable
    print(f"This is local variable: {y}")
    global x         #Globel keyword allow you to change globel variable under function
    x=5
    print(f"This is globel variable after change: {x}")


my_function()