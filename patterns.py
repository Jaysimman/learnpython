number = int(input("Enter a number: "))# to get a input from keyboard
for i in range(1,number+1):#range starts from number 1 to number + 1
    for j in range(1,i+1):#range starts from 1st number of i and it goes to print statement
        print(j,end="")#it print first value of j
    print()#it print the nextline so we use this