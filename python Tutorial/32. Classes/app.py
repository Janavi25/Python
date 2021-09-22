# We use classes to define new types, these  can have methods that we define in the body of the the class and they can also have attributes that we can set anywhere in our programs.

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


Point1 = Point()
Point1.draw()
Point1.x = 10
Point1.y = 20
print(Point1.x)
Point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)
