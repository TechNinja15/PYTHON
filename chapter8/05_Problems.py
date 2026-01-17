# 1. Write a program using functions to find greatest of three numbers.
'''
def greatest(a,b,c):
    if a>b and a>c:
        print(a,"is the greatest number among all")
    elif b>a and b>c:
        print(b,"is the greatest number among all")
    else:
        print(c,"is the greatest number among all")
a= int(input("Enter 1st Number : "))
b= int(input("Enter 2nd Number : "))
c= int(input("Enter 3rd Number : "))

greatest(a,b,c)
'''

# 2. Write a python program using function to convert Celsius to Fahrenheit

'''
def CtoF(n):
    a=(n*1.8)+32
    return a
n=int(input("Enter Temperature in Celsius : "))
print(f"In Fahrenheit : {CtoF(n)}")

'''

# 3. How do you prevent a python print() function to print a new line at the end.

'''
print("a")
print("b")
print("c", end="")
print("d", end="")

'''

# 4. Write a recursive function to calculate the sum of first n natural numbers.

'''
def sum(n):
    if n == 1:
        return 1

    return n + sum(n-1)
n = int(input("Enter a Number : "))
print(f"The sum of n numbers  are {sum(n)}")
'''
'''
5. Write a python function to print first n lines of the following pattern:
***
**               for n = 3
*
'''
'''
def star(n):
    for i in range(n, 0,-1):
        print("*" * i)    
n = int(input("Enter a Number : "))   
star(n)        
'''

# 6. Write a python function which converts inches to cms.

'''
def cms(inchs):
    cm=inchs*2.54
    return cm
inchs = float(input("Enter value in Inchs : "))
print(f"the value is converted into cm {cms(inchs)}")
'''

# 7. Write a python function to remove a given word from a list ad strip it at the same time.

'''
def rem(l, word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l=["apple", "mango", "banana","an"]

print(rem(l, "abc"))
'''

# 8. Write a python function to print multiplication table of a given number.

'''

def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
n=int(input("Enter a Number : "))
table(n)

'''