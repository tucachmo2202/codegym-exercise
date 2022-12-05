import turtle
import math



class Circle:
    x = 0 # Hoành độ của tâm đường tròn
    y = 0 # Tung độ của tâm đường tròn
    r = 100 # Bán kính đường tròn
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y - self.r)
        turtle.pendown()
        turtle.circle(self.r)

    def get_area(self):
        return self.r*self.r*math.pi
    
    def get_perimeter(self):
        return 2*self.r*math.pi
    
def write_information(area, perimeter, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write("Area = " + str(area))
    turtle.penup()
    turtle.goto(x, y - 20)
    turtle.pendown()
    turtle.write("Perimeter = " + str(perimeter))
    
circle_a = Circle(0, 0, 200)
circle_a.draw()
area_a = circle_a.get_area()
perimeter_a = circle_a.get_perimeter()

write_information(area_a, perimeter_a, 0, -210)

turtle.done()


