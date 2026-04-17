"""
a=5
print(a)
print(type(a))
b="Sowmiya"
print(b[1:-1])
print(b[::2])
print(b[::-1])
print(b[-1])
c = "    Sowmiya Ashok    "
print(c.strip())
print(c.lstrip())
print(c.rstrip())
"""
#variables = values

"""

a = 5
b = 1.1
c = "Sowmiya Ashok"
d = 4+2j
e = True
print(a,b,c,d,e)
print(type(a),type(b),type(c),type(d),type(e))


#collection datatypes
list   a = [ item1, item2, ...] 
tuple  b = ( item1, item2, ... )
set    c = { item1, item2, ...}
dict   d = {key:value,key:value,key:value,...}

#string operations

a = "Sowmiya"
#    012345678
print(a)
print(a[0])
print(a[4])
print(a[-1])
print(a[-3])
print(a[4:8])
print(a[::2])
print(a[::-1])

"""
"""
b = "Sowmiya Ashok"
print(b[9:6:-1])
print(b[-5:-8:-1])
print(b[9:-8:-1])
print(b[-5:6:-1])
"""
"""
b = "   Sowmiya Ashok  "
print(b.strip())
print(b.lstrip())
print(b.rstrip())
"""

"""

a = ["apple", "agg", "milk"]
print(a)
print(type(a))

b = ("apple", "agg", "milk")
print(b)
print(type(b))

a[0] = "bag"
print(a)
b[0] = "cat"
"""
"""
c= {1,1.1,"j"}
print(c)
print(type(c))

d={1:"Sowmiya",2:"Ashok"}
print(d)
print(d[1])

"""

#conditional statments
#if, elif, else
#loops
#for, while

password= "admin@123"
limit =0
while (limit<3):
    entry = input("Enter the password")
    if (password == entry):
        print("password match")
        break
    else:
        print("check your password")
        limit = limit+1
else:
    print("attempt limit reached")

#funtions

def abc():
    print("hello world")
    print("123")

abc()

def add(a,b):
    print(a+b)

add(2,3)

#object oriented programing language
#classes, object

class First:
    a = 78

    def method1(self):
        print("Method1")

o1 = First()
print(o1.a)
o1.a = 80
print(o1.a)
o1.method1()

#inheritance concept (parent and child)

class Second(First):
    b = 45

    def Method2(self):
        print("Method2")

s1 = Second()
print(s1.b)
print(s1.a)

#print(o1.b)
#modules

from cal import *

add(5,4)
sub(5,4)
mul(5,4)
div(5,4)
