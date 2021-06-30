WELCOME_MSG = '\n***Welcome to the Fibonacci Row Generator***' \
              '\nEnter only two positive integers for generating borders of the row divided by comma: '
ERROR_MSG = '\nPlease, try again and enter only integer numbers divided by comma.'


class FibonacciRange:
    """
    The main goal of this class - is generating Fibonacci's numbers for the special range.
    If you need instructions - pass empty parameters.
    """

    def __init__(self, open_number, close_number):
        self.open_number = open_number
        self.close_number = close_number

    def __repr__(self):
        return ', '.join(str(x) for x in self.numbers() if self.open_number < x < self.close_number)

    def numbers(self):
        result = []
        numb_one, numb_two = 0, 1
        while numb_two < self.close_number:
            yield numb_one
            numb_one, numb_two = numb_two, numb_one + numb_two


if __name__ == '__main__':
    while True:
        try:
            fib_numbers = input(WELCOME_MSG).split(',')
            f = FibonacciRange(int(fib_numbers[0]), int(fib_numbers[1]))
            print(f)
        except (IndexError, ValueError):
            print(ERROR_MSG)
            continue

        iteration = input('Start the program one more time?[y/n]: ')
        if iteration.lower() not in ['y', 'yes']:
            break
