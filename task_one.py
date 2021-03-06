WELCOME_MSG = '\n*** Welcome to the Chessboard Generator ***'\
              '\nFor correct using of program, enter only two integers divided by comma.'
VALUE_ERROR_MSG = 'Please, try again and enter only integer number.'


class Chessboard:
    """
    The main task of this class is printing Chessboard by two parameters:
    WIDTH - int, basically equal 0,
    HEIGHT - int, basically equal 0.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        self.main()

    def main(self):
        field_one, field_two = [], []
        for i in range(self.width):
            if i % 2 == 0:
                field_one.append('⬜')
                field_two.append('⬛')
            else:
                field_one.append('⬛')
                field_two.append('⬜')
        while self.height > 0:
            if self.height % 2 == 0:
                print(''.join(field_one))
            else:
                print(''.join(field_two))
            self.height -= 1


if __name__ == "__main__":
    while True:
        print(WELCOME_MSG)
        try:
            chess_width = int(input('Enter the value for width: '))
            chess_height = int(input('Enter the value for height: '))
        except ValueError:
            print(VALUE_ERROR_MSG)
            continue

        chess = Chessboard(chess_width, chess_height)

        iteration = input('One more time?[y/n]: ')
        if iteration.lower() not in ['y', 'yes']:
            break
