# Q1 WAP to add 2 variables 
a= 3
b = 5
print("The sum is ", a + b)

# Q2 Write a python program to find remainder when a number is divided by z.

a= 34
b= 5
print("The remainder is ", a % b)

# Q3. Check the type of variable assigned using input () function

a = input ("Enter something: ")
b= type(a)
print ("the type of variable is :",b)

# Q4. Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80

a= 34
b= 80
c= a > b
if c==True:
    print("a is greater than b")    
else: 
    print("a is not greater than b")

# Q5. Write a python program to find an average of two numbers entered by the user

a= int(input("Enter first num: "))
b= int(input("Enter Second num: "))
avg= (a + b)/2
print("The average of two numbers is ", avg)

# Q6. Write a python program to calculate the square of a number entered by the user.

a= int(input("Enter a number to square it: "))
sq= a*a
print("The square of the number is ", sq)