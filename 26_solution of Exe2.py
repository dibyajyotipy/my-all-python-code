import time

timeh = int(time.strftime('%H'))
yourname = 'Dibyajyoti'
if (timeh>=5 and timeh<12):
    print("Good morning",yourname)
elif(timeh>=12 and timeh<18):
    print("Good afternoon",yourname)
elif(timeh>=18 and timeh>21):
    print("Good evening",yourname)
else:
    print("Good night",yourname)