a = (1,45,342,3424,False, 45, "Rohan", "Shivam")
print(a) 

no = a.count(45)
print(no)

i = a.index(3424)
print(i)

print(len(a))

# Tuple Methods and Built-in Functions

t = (10, 20, 30, 20, 40)

# Tuple methods
print("Count of 20:", t.count(20))   # Output: 2
print("Index of 30:", t.index(30))   # Output: 2

# Common built-in functions
print("Length:", len(t)) # print the length of the tuple
print("Max:", max(t)) # print the maximum value in the tuple
print("Min:", min(t)) # print the minimum value in the tuple
print("Sum:", sum(t)) # print the sum of all elements in the tuple
print("Any True?:", any(t)) # checks if any element is true
print("All True?:", all(t)) # checks if all elements are true
print("Sorted:", sorted(t)) # returns a sorted list of the tuple elements
print("Tuple from list:", tuple([1, 2, 3])) # converts a list to a tuple
