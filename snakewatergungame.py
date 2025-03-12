
import random



'''
snake water gun game

snake = -1

water = 1

gun =0 

if  user enters 1 and computer enters -1 user looses

if  user enters -1 and computer enters 1 user wins

if  user enters 0 and computer enters -1 user wins

if  user enters 0 and computer enters 1 user looses

if  user enters -1 and computer enters 0 user looses

if  user enters 0 and computer enters -1 user wins

'''

computer=random.choice([-1,1,0])
SWGDict={"s":-1,"w":1,"g":0}
string=input("Enter users choice:")
newswgdict=SWGDict[string]
reversedict={-1:"Snake",1:"Water",0:"Gun"}

print(f"computer entered {reversedict[computer]} \n you enterd {reversedict[newswgdict]}")


if (computer==newswgdict):
    print("Its a draw")
else:

    if ( computer==-1 and newswgdict==1):
        print("you loose")

    elif( computer==-1 and newswgdict==0):
        print("you win")

    elif( computer==1 and newswgdict==-1):
        print("you win")

    elif( computer==1 and newswgdict==0):
        print("you loose")

    elif( computer==0 and newswgdict==-1):
        print("you loose")

    elif( computer==0 and newswgdict==1):
        print("you win")










