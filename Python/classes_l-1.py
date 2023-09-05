# ----

# class Point:
#     x = 0
#     y = 0

#     def coordinates(self):
#         print(f'coordinates are: {self.x}, {self.y}')



# my_point = Point()
# my_point.x = 10
# my_point.coordinates()

# ----

# class Point:
#     def __init__(self, x, y, a):
#         self.x = x
#         self.y = y
#         self.a = a

#     def coordinates(self):
#         print(f'coordinates are: {self.x}, {self.y}')           

# my_point = Point(6, 9, "Hello")
# my_point.coordinates()

# ----

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<Point x: {self.x}, y: {self.y}>' 
           

my_point = Point(6, 9)
print(my_point)
print(my_point.x)


