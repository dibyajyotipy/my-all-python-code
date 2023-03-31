a = (input("Enter a number between 1-5"))

try:
    if (a=='quit'):
        print("No error")
except:
    if (a>5 or a<1):
        raise ValueError("enter number between 1-5")
