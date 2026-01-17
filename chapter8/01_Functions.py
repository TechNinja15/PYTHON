
# A function is a group of statements performing a specific task.
# When a program gets bigger in size and its complexity grows, it gets difficult for a
# program to keep track on which piece of code is doing what!
# A function can be reused by the programmer in a given program any number of times

# a=12
# b=24
# c=56

# avg = (a+b+c)/3
# print(avg)

def avg():  # Defining a dunction
    a=12
    b=24
    c=56

    avg = (a+b+c)/3
    print(avg)

avg() # Calling a function
avg()
avg()
avg()
avg()


# QUICK QUIZ

def greet():
    print("Hello User")
    
greet()


# TYPES OF FUNCTIONS IN PYTHON
# There are two types of functions in python:
# • Built in functions (Already present in python)
# • User defined functions (Defined by the user)
# Examples of built in functions includes len(), print(), range() etc.
# The func1() function we defined is an example of user defined function