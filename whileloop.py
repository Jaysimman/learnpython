i = 10
j = 10
while(i<=200):
    print(i,end=",")
    i+=10
print()
while(j>=0):
    print(j,end=",")
    j-=1
print()
number = int(input("Enter a number:"))
fact=1
while(number>=1):
    fact*=number
    number-=1
print(fact)