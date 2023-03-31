myDict = {
    "dog" : "Animal",
    "mango" : "Fruite",
    "anotherDict": {"Dib" : "coder"}
}

print(myDict)



# dict methods
print(myDict.keys())        #print keys
print(myDict.items())       #print valus
print(myDict.get("dog"))    #get without error
updateDict = {              #update dict
    "update": "success"
}
myDict.update(updateDict)
print(myDict)