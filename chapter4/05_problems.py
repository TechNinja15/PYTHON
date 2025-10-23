# Q1 Write a program to store seven marks in a list entered by the user

# marks = []
# f1=int(input("Enter marks of 1 student: "))
# marks.append(f1)
# f2=int(input("Enter marks of 2 student: "))
# marks.append(f2)
# f3=int(input("Enter marks of 3 student: "))
# marks.append(f3)
# f4=int(input("Enter marks of 4 student: "))
# marks.append(f4)
# f5=int(input("Enter marks of 5 student: "))
# marks.append(f5)
# f6=int(input("Enter marks of 6 student: "))
# marks.append(f6)
# f7=int(input("Enter marks of 7 student: "))
# marks.append(f7)

# print("The marks entered are: ", marks) 
 
# Q2 Write a program to accept marks of 6 students and display them in a sorted manner.

# marks = []
# f1=int(input("Enter marks of 1 student: "))
# marks.append(f1)
# f2=int(input("Enter marks of 2 student: "))
# marks.append(f2)
# f3=int(input("Enter marks of 3 student: "))
# marks.append(f3)
# f4=int(input("Enter marks of 4 student: "))
# marks.append(f4)
# f5=int(input("Enter marks of 5 student: "))
# marks.append(f5)
# f6=int(input("Enter marks of 6 student: "))
# marks.append(f6)
# f7=int(input("Enter marks of 7 student: "))
# marks.append(f7)

# marks.sort()

# print("The marks entered are: ", marks)


# Q3 Check that a tuple type cannot be changed in python.

# a= (34, 45.6, "Avneesh")

# a[2] = "Avneesh"
# print(a)

# output : TypeError: 'tuple' object does not support item assignment

# Q4 Write a program to sum a list with 4 numbers

list = [1,1,1,1]
a = sum(list)
print(a)


# Q5 Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)

a = (7, 0, 8, 0, 0, 9)
n = a.count(0)
print(n)