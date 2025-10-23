# Q1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

H2E = {
    "Namaste" : "Hello",
    "madad" : "Help",
    "bili" : "cat",
}
# word = input("Enter a word for translation : ")
# print(H2E[word])


# Q2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).

# n1=int(input("Enter number : "))
# n2=int(input("Enter number : "))
# n3=int(input("Enter number : "))
# n4=int(input("Enter number : "))
# n5=int(input("Enter number : "))
# n6=int(input("Enter number : "))
# n7=int(input("Enter number : "))
# n8=int(input("Enter number : "))

# numbers = {n1,n2,n3,n4,n5,n6,n7,n8}
# print("You Enter these number(common numbers were eliminated)", numbers)


# Q3 Can we have a set with 18 (int) and '18' (str) as a value in it?

# s= {18, '18'}
# print(s) # Output: {18, '18'}
# Yes, we can have both 18 (int) and '18' (str) as values in a set because 
# they are of different data types.


# Q4 What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?
# b= len(s)
# print("The length of the set is : ",b)
# The length of the set will be 2 because 20 and 20.0 are considered equal in Python,
# so only one of them will be stored in the set along with '20' (string).

# Q5 s = {}
# What is the type of 's'?

# s is a dictionary. In Python, using curly braces {} without any key-value pairs
# creates an empty dictionary, not a set. To create an empty set, you should use set().
# print(type(s))  # Output: <class 'dict'>

# Q6.Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

f1 = input("Enter your Name : ")
s1 = input("Enter Language Name")
f2 = input("Enter your Name : ")
s2 = input("Enter Language Name")
f3 = input("Enter your Name : ")
s3 = input("Enter Language Name")
f4 = input("Enter your Name : ")
s4 = input("Enter Language Name")

s= {f1:s1,f2:s2,f3:s3,f4:s4}

print(s)


#07 If the names of 2 friends are same; what will happen to the program in problem
# 6?

# If the names of 2 friends are the same, the program will overwrite the previous entry
# for that name in the dictionary. Since dictionary keys must be unique, the last
# entry will be the one that is retained.
# For example, if two friends both enter the name "Harsh", the dictionary will only
# keep the language of the last friend who entered it.

# Q8 If languages of two friends are same; what will happen to the program in problem
# 6?

# If the languages of two friends are the same, the program will not have any issue
# because the values in a dictionary can be duplicated. In this case, both friends
# will have their favorite language stored in the dictionary under their unique names.
# For example, if both friends enter "Python" as their favorite language, the
# dictionary will store both entries without any conflict.

# 09 Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}


# No, you cannot change the values inside a list that is contained in a set because
# lists are mutable and sets require their elements to be immutable.
# Attempting to include a list inside a set will raise a TypeError.