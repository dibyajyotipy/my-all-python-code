def fun():
    try:
        a = [1,2,3,4]
        i = int(input("enter index"))
        print(a[i])
        return 1
    except:
        print("Error")
        return 0
    finally:
        print("I will always execute")

x = fun()
print(x)