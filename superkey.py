class a():
    def __init__(self):
        print("A")
    def display(self):
        print("you are in class A")
class b():
    def __init__(self):
        super().__init__()#it'll call the parent class constructor
        print("B")
    def display(self):
        print("You are in class B")
class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("You are in class C")
obj=c()