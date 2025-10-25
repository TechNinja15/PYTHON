# Q1. Write a program to find the greatest of four numbers entered by the user.

n1= int(input("Enter first number: "))
n2= int(input("Enter Second number: "))
n3= int(input("Enter Third number: "))
n4= int(input("Enter Fourth number: "))

if n1>n2:
    if n1>n3:
        if n1>n4:
            print("First no is the greatest Number among all")
        else:
            print("Fourth no is the greatest Number among all")
    elif n3>n4:
        print("Third no is the greatest Number among all")
    else: 
        print("Fourth no is the greatest Number among all")
elif n2>n3:
    if n2>n4:
        print("Second no is the greatest Number among all")
    else:
        print("Fourth no is the greatest Number among all")
else:
    print("Third no is the greatest Number among all")


# Q2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

sub1 = int(input("Enter markers of subject 1 : "))
sub2 = int(input("Enter markers of subject 2 : "))
sub3 = int(input("Enter markers of subject 3 : "))

per_overall = (sub1+sub2+sub3)/3

if per_overall >= 40 and sub1>=33 and sub2>=33 and sub3>=33:
    print("Congratulations you are Pass!!")
    print("subject 1 : ", sub1)
    print("subject 2 : ", sub2)
    print("subject 3 : ", sub3)
    print("Overall Percentage is : ", per_overall)
else:
    print("Better luck next Time :(")
    print("subject 1 : ", sub1)
    print("subject 2 : ", sub2)
    print("subject 3 : ", sub3)
    print("Overall Percentage is : ", per_overall)


# # Q3 A spam comment is defined as a text containing following keywords:
# # “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# # to detect these spams

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
comment = input("Enter your comment: ")

if (p1 in comment or p2 in comment or p3 in comment or p4 in comment):
    print("This is a spam message!!")
else:
    print("This is a geniune message")

#Q4. Write a program to find whether a given username contains less than 10
# characters or not.

username= input("Enter your username : ")
length = len(username)

if length<10:
    print("The username consist less than 10 character")
else:
    print("Username consist", length,"characters, make it less than 10 characters")

# Q5. Write a program which finds out whether a given name is present in a list or not

name = ["avneesh", "akj", "bsb", "bn"]

a= input("Enter a name to check in the list : ")

if a.lower() in name:
    print("Your Name is in the list!")
else:
    print("Your name is not in the list")

# Q6. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter you marks : "))

if marks>=90 and marks<=100:
    print("Your Grade is 'Ex'")
elif marks>=80 and marks<90:
    print("Your Grade is 'A'")
elif marks>=70 and marks<80:
    print("Your Grade is 'B'")
elif marks>=60 and marks<70:
    print("Your Grade is 'C'")
elif marks>=50 and marks<60:
    print("Your Grade is 'D'")
elif marks<50:
    print("Your Grade is 'F'")


# Q7.Write a program to find out whether a given post is talking about “AKJ” or not.

post = input("Enter your Post")

if "akj" in post.lower():
    print("'AKJ' is there in your Post")
else:
    print("You didn't mentioned 'AKJ' in you Post")