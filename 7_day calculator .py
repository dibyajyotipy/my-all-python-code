a = int(input("Enter your first number\n"))
b = int(input("Enter your second number\n"))
c = (input('''
        ****Select operator****
            +  ,  -  ,  *  ,  /   \n
'''))
if (c=='+'):
    print("Calculation is :",a+b,end="\n")
elif(c=='-'):
    print("Calculation is :",a-b,end="\n")
elif(c=='*'):
    print("Calculation is :",a*b,end="\n")
elif(c=='/'):
    print("Calculation is :",a/b,end="\n")
else:
    print("Invalid input")