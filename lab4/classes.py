import matplotlib.pyplot as plt


class Circle(object):

    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius

    def draw_circle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis("scaled")
        plt.show()


RedCircle = Circle(10, 'red')
print(dir(RedCircle))
print(RedCircle)
print(RedCircle.radius)
print(RedCircle.color)

RedCircle.radius = 5
print(RedCircle.radius)

# RedCircle.draw_circle()

print('Radius of object:', RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):', RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):', RedCircle.radius)

BlueCircle = Circle(radius=100)


# BlueCircle.draw_circle()

class Rectangle(object):

    def __init__(self, width=2, height=3, color='r'):
        self.width = width
        self.height = height
        self.color = color

    def draw_rectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()


SkinnyBlueRectangle = Rectangle(2, 10, 'blue')
print(SkinnyBlueRectangle.height)
print(SkinnyBlueRectangle.width)
print(SkinnyBlueRectangle.color)
SkinnyBlueRectangle.draw_rectangle()

FatYellowRectangle = Rectangle(20, 5, 'yellow')
FatYellowRectangle.draw_rectangle()
