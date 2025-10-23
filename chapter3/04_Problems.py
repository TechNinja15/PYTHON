# Q1 Write a python program to display a user entered name followed by Good Afternoon using input () function.

name = input("Enter your Name: ")
print("Good Afternoon", name)

# Q2 Write a program to fill in a letter template given below with name and date. 

# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

name = input("Enter your Name: ")
date = input("Enter Date: ")
letter = '''
Dear <Name>,  
You are selected!
<Date>
'''
letter = letter.replace("<Name>", name)
letter = letter.replace("<Date>", date)
print(letter)

# Q3 Write a program to detect double space in a string.

str = input("Enter a string: ")
ds = "  "
if ds in str:
    print("Double space detected")
else:
    print("No double space detected")

# Q4 Replace the double space from problem 3 with single spaces


str = input("Enter a string: ")
ds = "  "
if ds in str:
    print("Double space detected")
    str = str.replace("  ", " ")
    print("String after replacing double spaces with single spaces: ")
    print(str)
else:
    print("No double space detected")
    print("the origninal string is : ")
    print(str)


# Q5 Write a program to format the following letter using escape sequence characters.

# letter = "Dear Harry, this python course is nice. Thanks!"

letter = "Dear Harry,\nthis python course is nice.\nThanks!"
print(letter)