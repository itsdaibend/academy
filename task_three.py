from math import sqrt

WELCOME_MSG = '*** Welcome to the Triangle Comparator ***' \
              '\nFor correct using of program, enter only name and three numbers.'
ONE_MORE_MSG = 'Do you want to add another triangle?: '
ERROR_MSG = 'You should enter only 4 parameters: name of triangle and only three lengths divided by comma.\n'
NEW_TRIANGLE_MSG = 'Enter name and length of triangle divided by comma: '


class Triangle:
    """
    The main task of this class is creating different triangles by their areas.
    """

    def __init__(self, triangle_name, side_a, side_b, side_c):
        self.triangle_name = triangle_name
        self.side_a = int(side_a)
        self.side_b = int(side_b)
        self.side_c = int(side_c)

        self.get_values()

    def get_values(self):
        semi_per = (self.side_a + self.side_b + self.side_c) / 2
        area = sqrt(semi_per * (semi_per - self.side_a) * (semi_per - self.side_b) * (semi_per - self.side_c))
        print(
            f'New triangle created as {self.triangle_name}, lengths - {self.side_a},'
            f'{self.side_b},{self.side_c} cm.'
            f'\nPerimeter(P) = {semi_per*2} cm,\nArea(S) = {round(area, 2)} cm.'
             )

        triangles.append((self.triangle_name, area))


if __name__ == "__main__":
    triangles = []

    while True:
        print(WELCOME_MSG)
        try:
            name, side_first, side_second, side_third = input(NEW_TRIANGLE_MSG).split(',')
            int_new_triangle = list(map(lambda i: int(i), (side_first, side_second, side_third)))
            int_new_triangle.insert(0, name)
        except ValueError:
            print(ERROR_MSG)
            continue

        triangle_to_compare = Triangle(name, side_first, side_second, side_third)

        question = input(ONE_MORE_MSG)
        if question.lower() in ['y', 'yes']:
            print("Let's add one more...\n")
            continue
        else:
            break

    triangles.sort(key=lambda y: y[1], reverse=True)
    print('\n====== Triangles list: ======')
    for triangle in triangles:
        print(f'[Triangle {triangle[0]}]: {round(triangle[1],2)} cm.')
