# marks= {
#     "Avneesh": 80,
#     "Rohan" : 77,
#     "Aryan" : 45,
#     "list" : [1,2,3,4]
# }

# print (marks, type(marks))
# print(marks["list"])


# =========================== Methods of Dictionary ===============================

marks= {
    "Avneesh": 80,
    "Rohan" : 77,
    "Aryan" : 45,
    0 : "Avneesh"
}

# print (marks.items())
# print (marks.keys())
# print (marks.values())
# marks.update({"Avneesh": 99})
# print(marks)

# print (marks.get("Avneesh2")) # Prints "None"
# print (marks["Avneesh2"]) # While this Prints a Error



# Dictionary Methods in Python

# Creating a dictionary
student = {
    "name": "Avneesh",
    "age": 18,
    "course": "B.Tech CSE"
}

# 1️ clear() – removes all items from the dictionary
temp = student.copy()
temp.clear()
print("1. clear():", temp)

# 2️ copy() – returns a shallow copy of the dictionary
copy_dict = student.copy()
print("2. copy():", copy_dict)

# 3️ fromkeys() – creates a new dictionary from given keys with same value
keys = ("name", "age", "city")
new_dict = dict.fromkeys(keys, "unknown")
print("3. fromkeys():", new_dict)

# 4️ get() – returns value for the key, or default if key not found
print("4. get('name'):", student.get("name"))
print("   get('branch', 'Not Found'):", student.get("branch", "Not Found"))

# 5️ items() – returns all key-value pairs as tuples
print("5. items():", student.items())

# 6️ keys() – returns all keys
print("6. keys():", student.keys())

# 7️ values() – returns all values
print("7. values():", student.values())

# 8️  pop() – removes key and returns its value
temp = student.copy()
removed = temp.pop("age")
print("8. pop('age'):", removed)
print("   After pop:", temp)

# 9️ popitem() – removes last inserted key-value pair
temp = student.copy()
popped = temp.popitem()
print("9. popitem():", popped)
print("   After popitem:", temp)

# 10 setdefault() – returns value of key; if key doesn’t exist, adds it with given value
temp = student.copy()
temp.setdefault("city", "Raipur")
print("10. setdefault('city', 'Raipur'):", temp)

# 11 update() – updates dictionary with another dict or key-value pairs
temp = student.copy()
temp.update({"branch": "AI", "age": 19})
print("11. update():", temp)


