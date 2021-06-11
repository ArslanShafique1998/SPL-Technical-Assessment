#We take input of two maps
n1=int(input("Enter number length of map 1:"))
n2=int(input("Enter number length of map 2:"))
d1={}
d2={}
for i in range(0,n1,1):
    key=input("Enter key of map1:")
    value=int(input("Enter value of map1 regarding above key it should be integer:"))
    d1[key]=value
for i in range(0,n2,1):
    key=input("Enter key of map2:")
    value=int(input("Enter value of map2 regarding above key it should be integer:"))
    d2[key]=value
print(d1)
print(d2)
# check either the two dictionary is equal or not
if d1==d2:
    print('true')
else:
    print('false')