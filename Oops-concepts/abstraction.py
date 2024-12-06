from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return (self.width*self.height)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return (3.14*self.radius*self.radius)
print("area of rectangle :",Circle(10).area())
print("area of circle :",Rectangle(10,15).area())









# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
    # def __init__(self, width, height):
    #     self.width = width
    #     self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

# class Circle(Shape):
    # def __init__(self, radius):
    #     self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# # Create instances of each shape
# rectangle = Rectangle(4, 5)
# circle = Circle(3)

# # Call methods
# print(f"Rectangle area: {rectangle.area()}")         # Output: Rectangle area: 20
# print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Output: Rectangle perimeter: 18
# print(f"Circle area: {circle.area()}")               # Output: Circle area: 28.26
# print(f"Circle perimeter: {circle.perimeter()}")       # Output: Circle perimeter: 18.84
