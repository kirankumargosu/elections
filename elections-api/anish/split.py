a = "This is a nice place"
b = "empid,empname,salary"
print(a)
output = a.split(" ")
print(output)
print(type(output))
print(b)
bList = b.split(",")
print(bList)
for item in bList:
    print(item)


c = "I will succeed"

print(c)
c = c.split(" ")
print(c)

L1 = [7, 2, 3, 4]
# L2 = L1 + 2
L1 = L1 * 2
L = L1.pop(7)
print(L1)
print(L1)
print(L)