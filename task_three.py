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

    def __init__(self, name, side_a, side_b, side_c):
        self.name = name
        self.side_a = int(side_a)
        self.side_b = int(side_b)
        self.side_c = int(side_c)

        self.main()

    def main(self):
        semi_per = (self.side_a + self.side_b + self.side_c) / 2
        area = sqrt(semi_per * (semi_per - self.side_a) * (semi_per - self.side_b) * (semi_per - self.side_c))
        print(
            f'New triangle created as {self.name}, lengths - {self.side_a},'
            f'{self.side_b},{self.side_c} cm.'
            f'\nPerimeter(P) = {semi_per*2} cm,\nArea(S) = {round(area, 2)} cm.'
             )

        triangles.append((self.name, area))


if __name__ == "__main__":
    triangles = []
    actually = True

    while actually:
        print(WELCOME_MSG)
        try:
            new = input(NEW_TRIANGLE_MSG).split(',')
            if len(new) < 4:
                print(ERROR_MSG)
                continue
            int_new_triangle = list(map(lambda i: int(i), new[1:]))
            int_new_triangle.insert(0, new[0])
        except ValueError:
            continue

        triangle = Triangle(new[0], new[1], new[2], new[3])

        question = input(ONE_MORE_MSG)
        if question.lower() == 'yes' or question.lower() == 'y':
            print("Let's add one more...\n")
            continue
        else:
            break

    triangles.sort(key=lambda y: y[1], reverse=True)
    print('\n====== Triangles list: ======')
    for x in triangles:
        print(f'[Triangle {x[0]}]: {round(x[1],2)} cm.')

    iteration = input('\nStart the program one more time?[y/n]: ')
    if str(iteration.lower()) != 'y':
        actually = False
