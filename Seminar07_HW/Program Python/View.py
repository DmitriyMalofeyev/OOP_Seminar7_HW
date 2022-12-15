import Circle
import Rectangle
import Square
import Triangle


class Print():

    def print_circle(self, radius):
        temp = Circle.Circle(radius)
        print(f"Circle - R: {radius},  S: {temp.get_area()}, Length of the circle: {temp.lengtHable()}")

    def print_rectangle(self, first, second):
        temp = Rectangle.Rectangle(first, second)
        print(f"Rectangle - side 1: {first}, side 2: {second}, S: {temp.get_area()}, P: {temp.perimetr()}")

    def print_square(self, side):
        temp = Square.Square(side)
        print(f"Square - side : {side}, S: {temp.get_area()}, P: {temp.perimetr()}")

    def print_triangle(self, first, second, third):
        temp = Triangle.Triangle(first, second, third)
        print(
            f"Triangle - side 1: {first}, side 2: {second}, side 3: {third}, S: {temp.get_area()}, P: {temp.perimetr()}")

    def print_all_area(self, area):
        print(f"Total S of all the shapes = {area}")

    def print_all_perimetr(self, perimetr):
        print(f"Total P of all the shapes = {perimetr}")
