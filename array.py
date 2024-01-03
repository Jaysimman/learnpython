#Array in python
a=[]
n=int(input("Enter a number to store : "))
for i in range(n):
    num=int(input("Enter a number " +str(i+1)+" : "))
    a.append(num)
print(a)
def largest(a):
    large= max(a)
    return large
print("The largest element is ",largest(a))
def shortest(a):
    short= min(a)
    return short
print("The shortest elememt is ",shortest(a))

# Removing duplicates from the list
list1 = list(set(a))

# Sorting the list
list1.sort()

# Printing the second last element
print("Second largest element is:", list1[-2])
