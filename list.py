mylist = []
mylist.append(1)
mylist.append(2)

print(mylist[0])
print(mylist[1])


# change value of list 
mylist[1]= 69
print(mylist)


# list slicing
friends = ["pankaj","sanjay","bhoben","raju"]
print(friends[2])
print(friends[1:3])


# list method 
l1=[5,4,3,2,1,0]
print("this is normal list",l1)
l1.sort()                #sort the list
print("this is sort list",l1)

l1.reverse()             #reverse the list
print("this is reverse list",l1)

l1.append(69)            #add to the end of the list
print("this is append",l1)

l1.insert(0, 000)         #insert value at the given index
print("this is insert ",l1)

l1.pop(0)                 #delete value from the given index
print("this is pop",l1)

l1.remove(69)              #delete the value
print("this is remove",l1)
