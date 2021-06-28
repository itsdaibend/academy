from random import randint
import re


WELCOME_MSG = '\n***Welcome to the Lucky Tickets Finder***' \
              '\nFor detail instructions - press enter without text.' \
              '\nIf you need to generate tickets - press "1", choose the sorting method - "2": '
INFORMATION_MSG = '\nFor correct using this application, after start choose the mode of program.' \
                  '\nTickets-generator mode creates .txt file with certain amount of tickets.' \
                  '\nTickets-sorting mode chooses tickets from the .txt file and sorting them by two methods.' \
                  '\nYour file has to be in the program repository.'
SORTING_MSG = "Select the sorting method - Moscow or Petersburg, respectively, by pressing 1 or 2: "
DATA_MSG = 'Enter the name of file, amount of tickets, min.,max. values divided by comma: '
ERROR_MSG = "The file you were looking for was not found. Please,try again."


class TicketsGenerator:
    """
    This class creates a .txt file with certain amount of tickets in a digit format.
    """
    def __init__(self, file_name, tickets_amount, min_ticket_value, max_ticket_value):
        self.file_name = file_name
        self.tickets_amount = tickets_amount
        self.min_ticket_value = min_ticket_value
        self.max_ticket_value = max_ticket_value

    def get_file(self):
        with open(self.file_name, 'w') as file:
            for i in range(int(self.tickets_amount)):
                file.write(f'{randint(self.min_ticket_value,self.max_ticket_value):06} ')
            file.close()


class TicketsCounter:
    """
    This class checks all the tickets in file and returns amount of special combinations.
    """
    @staticmethod
    def moscow_method(file):
        count = 0
        try:
            with open(file, 'r') as f:
                for line in f:
                    all_numbers = re.findall(r'[0-9]{6}', line)
                    for number in all_numbers:
                        if (
                                int(number[0]) + int(number[1]) + int(number[2]) ==
                                int(number[3]) + int(number[4]) + int(number[5])
                           ):
                            count += 1
            f.close()
        except FileNotFoundError:
            return print(ERROR_MSG)
        return print(count)

    @staticmethod
    def saint_petersburg_method(file):
        count = 0
        try:
            with open(file, 'r') as f:
                for line in f:
                    all_numbers = re.findall(r'[0-9]{6}', line)
                    for number in all_numbers:
                        if (
                                int(number[0]) + int(number[2]) + int(number[4]) ==
                                int(number[1]) + int(number[3]) + int(number[5])
                           ):
                            count += 1
            f.close()
        except FileNotFoundError:
            return print(ERROR_MSG)
        return print(count)


if __name__ == '__main__':
    actually = True
    while actually:
        mode = input(WELCOME_MSG)
        if mode == '':
            print(INFORMATION_MSG)
        elif mode == '1':
            try:
                incoming_data = input(DATA_MSG).split(',')
                t = TicketsGenerator(
                    f'{incoming_data[0]}.txt', int(incoming_data[1]), int(incoming_data[2]), int(incoming_data[3])
                                    )
                t.get_file()
            except (IndexError, ValueError):
                continue
        elif mode == '2':
            t = TicketsCounter
            sorting_method = input(SORTING_MSG)
            incoming_data = input('Enter the name of file or path to file: ')
            if sorting_method == '1':
                t.moscow_method(incoming_data)
            elif sorting_method == '2':
                t.saint_petersburg_method(incoming_data)

        iteration = input('\nStart the program one more time?[y/n]: ')
        if str(iteration.lower()) != 'y':
            actually = False
