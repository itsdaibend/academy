WELCOME_MSG = '\n***Welcome to the Natural Row Generator***' \
              '\nFor detail instructions press enter without text.' \
              '\nFor starting the program - enter only natural number: '


class NaturalRowGenerator:
    """
    This class is generating a natural row until the number, square of which is bigger than entered number.
    """
    def __init__(self, number):
        self.number = number

    def main(self):
        return print([n for n in range(self.number) if 0 < n**2 < self.number])


if __name__ == '__main__':
    actually = True
    while actually:
        incoming_data = input(WELCOME_MSG)

        if incoming_data == '':
            print('some instructions')
        elif incoming_data.isdigit() is True:
            numb = NaturalRowGenerator(int(incoming_data))
            numb.main()
        else:
            continue

        iteration = input('\nStart the program one more time?[y/n]: ')
        if str(iteration.lower()) != 'y':
            actually = False