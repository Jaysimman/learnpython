a=[1,2,3,4,5]#list accepts duplicate values also and it also accept strings
print(a)
a.append(6)# add the value of list in last element
print(a)
a.insert(0,0)# inster the value in specific position
print(a)
a.insert(1,11)
print(a)
a.append(3)
print(a)
a[0]=1# it is used to replace the value in specific position
print(a)
a.pop(2)#pop is used to remove the element in the specific position
print(a)
a.append("hello")
print(a)
b=[8,9,10]
a.extend(b)# its used to combine two list in to "a" list
print(a)
print("--------------------------------------------------")
print("------TUPLE-------")
c=(1,2,3,4,5)#we cannot add or remove elements in tuple
print(type(c))
d=list(c)#type casting convert the tuple to list
print(d)
print("-----------------DICTIONARY----------------")
e={1,2,7,3,4,5}
print(e)# dont allow duplicate values it removes duplicate values, we cannot modify set items but we can add or remove set items and aslo sets are unordered
e.add(6)
print(e)
e.remove(3)
print(e)
e.pop()
print(e)