WELCOME_MSG = '\n***Welcome to the Fibonacci Row Generator***' \
              '\nEnter only two positive integers for generating borders of the row divided by comma: '
ERROR_MSG = '\nPlease, try again and enter only integer numbers divided by comma.'


class Fibonacci:
    """
    The main goal of this class - is generating Fibonacci's numbers for the special range.
    If you need instructions - pass empty parameters.
    """

    def __init__(self, open_number, close_number):
        self.open_number = open_number
        self.close_number = close_number

        self.main()

    def main(self):
        result = []
        numb_one, numb_two = 0, 1
        while numb_two < self.close_number:
            numb_one, numb_two = numb_two, numb_one + numb_two
            result.append(numb_one)
        while result[0] < self.open_number:
            result.pop(0)
        return print(result)


if __name__ == '__main__':
    actually = True
    while actually:
        try:
            fib_numbers = input(WELCOME_MSG).split(',')
            f = Fibonacci(int(fib_numbers[0]), int(fib_numbers[1]))
        except (IndexError, ValueError):
            print(ERROR_MSG)
            continue

        iteration = input('\nOne more time?[y/n]: ')
        if str(iteration.lower()) != 'y':
            actually = False
