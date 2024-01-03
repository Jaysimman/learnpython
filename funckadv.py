# No return type with arguments
def add(a,b):
    c=a+b
    print(c)
add(10,20)

#return type with argument
def sub(a,b):
    c=a-b
    return c #it doesnot return Anything in the output
x=sub(20,10)
print(x)

#Arbitary arguments
def names(*students):
    print(students)
names("Ramesh","Suresh","Dinesh")

def message(name,age):
    print(name, "age is ",age)
message("Jai",20)

#keyword arguments in function
def note(name,age):
    print(name, "age is",age)
note(age=21,name="jai")

#arbitary keyword arguments
def letter(**data):
    print(data)
letter(name="Jai",age=25,gender="Male",number=987456123)

#default parameter function
def user(name,city="Tiruppur"):
    print(name,"is from",city)
user("jai")
user("simman","Chennai")

#passing list as a function
def total(marks):
    return sum(marks)
print(total([10,20,30,40,50]))

#recursive function
def factorial(x):
    if x==1:
        return x
    else:
        return (x*factorial(x-1))
print(factorial(5))

#lambda Function
x=lambda y:y+10
print(x(10))
