dic = {
    1 : "Dib",
    2:"Raju",
    3:"Bikash",
    4: "Sanjay"
}
# print(dic[5])      #Get error
print(dic.get(5))    #Get none

for key,value in dic.items():
    print(f"{key} is {value}")