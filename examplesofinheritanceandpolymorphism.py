class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=10
        b=20
        areaofrectangle=l*b
        print(areaofrectangle)
r1=rectangle()
r1.area()

class person():
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print(self.name,self.grade)
s=student("Jay","A")
s.display()

class vehicle():
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print("Car started")
c=car()
c.start()