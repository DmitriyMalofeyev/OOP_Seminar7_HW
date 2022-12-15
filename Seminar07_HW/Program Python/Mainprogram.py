
import FigureController


class Main_figures():

    def run(self):
        controller = FigureController.Controllers()

        controller.add_circle(6)
        controller.add_rectangle(1, 3)
        controller.add_square(13)
        controller.add_triangle(4, 4, 4)
        print()
        controller.all_area()
        print()
        controller.all_perimetr()
        print()
        controller.print_list_figure()


m = Main_figures()
m.run()
