'''
The word polymorphism means having many forms. In programming, polymorphism
means the same function name (but different signatures) being used for different
types. The key difference is the data types and number of arguments used in function.
'''
def add(a,b,c=0):
    print(a+b+c)
add(10,20)
add(10,20,30)

#method overridding:
class Animal():
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):#if we cannot define sound method means it will print animal class sound it is also call as method overridding
        print("Dog barks")
class bird(Dog):
    def sound(self):
        print("bird sings")
d1=Dog()
d1.sound()

b=bird()
b.sound()