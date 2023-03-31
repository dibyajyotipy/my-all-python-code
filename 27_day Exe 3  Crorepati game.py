questions=["What is the the capital of india","Which country win Fifa WorldCup 2022 "]
ans=[["1.Kolkata","2.Chennai","3.Delhi","4.Assam"],["1.Portugal","2.Argentina","3.Brazil","4.India"]]
money = 0
score = 0
print("Kaun banega crorepati me apka swagat he")
inputU = int(input('''
        1 - New Game
        2 - How to play
        3 - Check new update

'''))

if inputU==1:
        print(questions[0],"\n")
        ansU = int(input(ans[0]))
        if ansU == 3:
            print("Wow! Akdum sahi jawab")
            money = money + 100
            score = score + 2
            print("Your money: ",money,"\n Score: ",score)
        else:
            print("Nahi apka jawab galat he")
        nx=int(input(("1 - Next question")))
        if nx==1:
            print(questions[1],"\n")
            ansU = int(input(ans[1]))
        if ansU == 2:
            print("Wow! Akdum sahi jawab")
            money = money + 100
            score = score + 2
            print("Your money: ",money,"\n Score: ",score)
        else:
            print("Nahi apka jawab galat he")
        nx=int(input(("1 - Next question")))
        if nx==1:
            print("More questions comming soon")
elif inputU==2:
        print("this is how to play\nUpdating soon!")
elif inputU==3:
        print('''           ****Checking for updates****
        -----------------------------------
            You are using latest version
                No new updates!
        -----------------------------------
                Thank You!
        
        ''')
else:
        print("Invalid Input")

