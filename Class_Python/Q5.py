class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x,new_y)
    
    def display(self):
        print(f"Point(x={self.x}, y = {self.y})")

p1 = Point(10,20)
p2 = Point(12,15)

p3 = p1 + p2
p3.display()
