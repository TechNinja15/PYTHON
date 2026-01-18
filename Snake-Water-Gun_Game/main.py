'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([1,0,-1])
userin = input("Enter your choice : ")
userDict = {"s": 1, "w":-1, "g":0}
revuserDict = {1:"SNAKE 🐍", -1 : "WATER 💦", 0: "GUN 🔫"}
user=userDict[userin]

print(f"You choice : {revuserDict[user]} \nComputer choice : {revuserDict[computer]}")

if (computer == user):
    print("Its a Draw")
else:
    if (computer==-1 and user == 1 ):
        print("YOU Wins")
    elif(computer==-1 and user == 0):
        print("Computer wins")
    elif(computer == 1 and user == -1):
        print("Computer Wins")
    elif(computer == 1 and user == 0):
        print("YOU Wins")
    elif(computer == 0 and user == -1):
        print("YOU Wins")
    elif(computer ==0 and user == 1):
        print("Computer Wins")