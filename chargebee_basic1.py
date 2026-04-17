# Variables and Data Types
a = 5
print(a)
print(type(a))

name = "Sowmiya"
print(name[1:-1])
print(name[::2])
print(name[::-1])
print(name[-1])

full_name = "    Sowmiya Ashok    "
print(full_name.strip())
print(full_name.lstrip())
print(full_name.rstrip())


# Different Data Types
a = 5
b = 1.1
c = "Sowmiya Ashok"
d = 4+2j
e = True
print(a, b, c, d, e)
print(type(a), type(b), type(c), type(d), type(e))


# String Operations
a = "Sowmiya"
print(a)
print(a[0])
print(a[-1])
print(a[2:6])
print(a[::2])
print(a[::-1])


# List, Tuple, Set, Dictionary
lst = ["apple", "egg", "milk"]
tpl = ("apple", "egg", "milk")
st = {1, 1.1, "S"}
dct = {1: "Sowmiya", 2: "Ashok"}

print(lst)
print(tpl)
print(st)
print(dct)
print(dct[1])


# Modify List
lst[0] = "bag"
print(lst)


# Conditional Statements (Password Check)
password = "Sowmiya@123"
limit = 0

while limit < 3:
    entry = input("Enter the password: ")
    if password == entry:
        print("Password matched ✅")
        break
    else:
        print("Wrong password ❌")
        limit += 1
else:
    print("Attempt limit reached 🚫")


# Functions
def greet():
    print("Hello Sowmiya 👋")
    print("Welcome to Python")

greet()


def add(a, b):
    print("Sum:", a + b)

add(2, 3)


# Object-Oriented Programming
class First:
    a = 78

    def method1(self):
        print("This is Method1")

o1 = First()
print(o1.a)
o1.a = 80
print(o1.a)
o1.method1()


# Inheritance
class Second(First):
    b = 45

    def method2(self):
        print("This is Method2")

s1 = Second()
print(s1.b)
print(s1.a)


# Module Example (Make sure cal.py exists)
# cal.py should contain add, sub, mul, div functions

from cal import *

add(5, 4)
sub(5, 4)
mul(5, 4)
div(5, 4)
