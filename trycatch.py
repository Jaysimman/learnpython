a=input()
b=input()

try:
    c=int(a)+int(b)
except Exception as e:
    print("You Made a mistake")
    print(e)
else:
    print(c)
finally:
    print("It will execute automatically that it doesn't know about what is in the try block or except exception as e block")