a= "AKJ"
age = 19
def greet(name,age):
    # print("Hello " + name + age) # This will give a error cause integer (age) and string(name) cannot be added together
    print("Hello " + name + str(age)) #and then also if wanted to add we can convert the int into a str
    print("Hello " + name)
    print(age)
    return "thank u"
a = greet(a,age)
print(a)