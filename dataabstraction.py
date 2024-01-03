from abc import ABC, abstractmethod

# Define an abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Implement a concrete class that extends the abstract class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Implement another concrete class that extends the abstract class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Create objects of the concrete classes
square_obj = Square(5)
circle_obj = Circle(3)

# Access the area method without worrying about implementation details
print("Area of the square:", square_obj.area())
print("Area of the circle:", circle_obj.area())



'''In this example, Shape is an abstract class with an abstract method area. The Square and Circle classes are concrete classes that inherit from the Shape abstract class and provide their own implementations of the area method. The abstract class serves as a blueprint, enforcing that all concrete classes must implement the area method.

By using this structure, you can create objects of the concrete classes (Square and Circle) and call the area method without needing to know the specific implementation details of each class. This is an example of data abstraction, where the implementation details are hidden, and the user interacts with the abstract interface.


'''