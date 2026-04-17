#string operations

a= "sowmiya ashok"

#   012345678

print(a[0])#s
print(a[4])#i
print(a[-1])#k
print(a[-3])#o
#print(a[start index,stop index-1])
print(a[4:8])#miya
#print(a[start index:stop index-1:step])
print(a[::2])#alternative
print(a[::-1])#reverse


b = "Deepa Jeevana"
print(b[9:6:-1])#ana
print(b[-5:-9:-1])

b = "       Sowmiya Ashok      "
print(b.strip())
print(b.lstrip())
print(b.rstrip())

a = ["sowmiya", "deepa", "jeevana"]
print(a)
print(type(a))


b = ["sowmiya", "deepa", "jeevana"]
print(b)
print(type(b))


a[0] = "Ashok"
print(a)
#b(0) = "Ashok"


c = {1,1.1,"sowmiya"}
print(c)

d = {1:"deepa",2:"jeevana"}
print(d)
print(d[1])

d = {"veg":{"tomato":5,"carrot":10,"fruit":{"grapes":6,"apple":8}}}
print(d)
print(d["veg"])
