class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        return 0  

    def perimeter(self):
        return 0  

    def __str__(self):
        return f"Shape with color {self.color}"
    

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self): 
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return (f"Rectangle with color {self.color}, "
               f"width {self.width}, and height {self.height}")

if __name__ == "__main__":
    shape = Shape("green")
    print(shape)
    print("Area is", shape.area())
    print("Perimeter is", shape.perimeter())

rectangle = Rectangle("red", 5, 3)
print(rectangle)  
print("Area is", rectangle.area())  
print("Perimeter is", rectangle.perimeter())  



