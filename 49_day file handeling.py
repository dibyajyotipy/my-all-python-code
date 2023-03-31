f = open('myfile.txt','r')
text = f.read()
print(text)
f.close()

f = open('myfile.txt','a')
f.write('Hello')
f.close()

