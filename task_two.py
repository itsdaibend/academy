WELCOME_MSG = '*** Welcome to the Envelopes Comparator ***' \
              '\nFor correct using of program, enter integers in each input.'
RESULT_FIRST_MSG = 'Second envelope is accommodate in first.'
RESULT_SECOND_MSG = 'First envelope is accommodate in second.'
RESULT_NONE_MSG = "Second envelope isn't accommodate in first and vice versa."


class Envelope:
    """
    *** Welcome to the Envelops Generator ***
    The main task of this class is creating envelopes.
    """

    def __init__(self, width=float(0), height=float(0)):
        self.width = width
        self.height = height

    def __gt__(self, another_env):
        return (
                self.width > another_env.width and self.height > another_env.height
                or self.width > another_env.height and self.height > another_env.width
               )

    def __lt__(self, another_env):
        return (
            self.width < another_env.width and self.height < another_env.height
            or self.width < another_env.height and self.height < another_env.width
               )


def env_compare():
    if env1 > env2:
        result = RESULT_FIRST_MSG
    elif env1 < env2:
        result = RESULT_SECOND_MSG
    else:
        result = RESULT_NONE_MSG
    return result


if __name__ == '__main__':
    while True:
        print(WELCOME_MSG)
        try:
            first_width = float(input('Enter the value for width of first envelope: '))
            first_height = float(input('Now, enter the value for height of first envelope: '))
            second_width = float(input('Good! Enter the value for width of second envelope: '))
            second_height = float(input('Ok, enter the value for width of second envelope: '))
        except ValueError:
            print(f'\nPlease, try again and enter only integer or float numbers.')
            continue

        env1 = Envelope(first_width, first_height)
        env2 = Envelope(second_width, second_height)

        print(env_compare())

        iteration = input('Start the program one more time?[y/n]: ')
        if iteration.lower() not in ['y', 'yes']:
            break
