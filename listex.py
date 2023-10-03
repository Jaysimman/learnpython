a = []
n = int(input("Enter a number: "))
print("Enter a number from 1 to ",n)
for i in range(1,n+1):
    num = int(input("Enter a number "+str(i)+" :"))
    a.append(num)
print(a)

sum = 0
for i in a:
    sum+=i
print("Sum of these numbers are :",sum)
print("Average of these numbers are :",sum/n)