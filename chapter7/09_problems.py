# # 1. Write a program to print multiplication table of a given number using for loop.

# a= int(input("Enter a number for multiplication Table : "))

# i=1
# for i in range(11):
#     print(a,"x",i,"=", a*i)
#     i=i+1

# # 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# #    l = ["Harry", "Soham", "Sachin", "Rahul"]

# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for i in l:
#     s=i;
#     if s[0].lower()=='s':
#         print('hello',s)
#     else:
#         print("fuck you",s)

# 3. Attempt problem 1 using while loop.

# a= int(input("Enter a number for multiplication table : "))

# i=1
# while(i<11):
#     print(a, "x", i,"=", a*i)
#     i=i+1

# Write a program to find whether a given number is prime or not.

# a= int(input("Enter a number to check wheater it is a prime number or not : "))
# count=0
# for i in range(1,a+1):
#     if a%i==0:
#         count=count+1
# if count==2:
#     print('prime number hai bhaiii')
# else :
#     print("Gawar hai kya")

#Write a program to find the sum of first n natural numbers using while loop.

# n= int(input("Enter a number to find the sum of all the previous number including that you entered : "))

# i=1
# sum=0
# while(i<=n):
#     sum = sum + i 
#     i+=1
# print("sum of the number is : ",sum)


#6. Write a program to calculate the factorial of a given number using for loop.

# n = int(input("Enter a no to check wheater the no is factorial or not : "))

# p=1
# for i in range(1,n+1):
#     p = p * i

# print (f"The factorial of {n} is {p}")


# 7. Write a program to print the following star pattern.
'''
  *
 ***
***** for n = 3
'''

# n = int(input("Enter a number : "))

# for i in range(1, n + 1):
#         # Print leading spaces
#         # Number of spaces decreases with each row
#         for j in range(n - i):
#             print(" ", end="")

#         # Print stars
#         # Number of stars is (2*i - 1)
#         for k in range(2 * i - 1):
#             print("*", end="")

#         # Move to the next line after the row is complete
#         print()



# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

# n=int(input("Enter a number : "))
# for i in range(1, n+1):
#     print("*" * i);
#     i=i+1


# 9. Write a program to print the following star pattern.
# * * *
# *   *   for n = 3
# * * *

# n = int(input("Enter a number : "))

# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*"*n, end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")


# 10. Write a program to print multiplication table of n using for loops in reversed
# order.

n= int(input("Enter a Number : "))
for i in range(10,0,-1):
    print(n,"x",i, "=",n*i)