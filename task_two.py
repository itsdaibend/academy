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


if __name__ == '__main__':
    actually = True
    while actually:
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

        def env_compare():
            if env1 > env2:
                result = 'env 2 is accommodate in env 1'
            elif env1 < env2:
                result = 'env 1 is accommodate in env 2'
            else:
                result = "env 2 isn't accommodate in env 1 and vice versa."
            return result

        print(env_compare())

        iteration = input('One more time?[y/n]: ')
        if str(iteration.lower()) != 'y':
            actually = False
