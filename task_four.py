import re


WELCOME_MSG = '\n***Welcome to the File Parser***' \
              '\nFor detail instructions - press enter without text.' \
              '\nIf you need text-counter mode - press "1", text-substitute - "2": '
FRST_MODE_MSG = '\nYou have chosen the text-counter mode.' \
              '\nEnter the name of file and text you want to find, divided by comma: '
SEC_MODE_MSG = 'You have chosen the text-substitute mode.' \
              '\nEnter the name of file,text to change and to substitute divided by comma: '
INFORMATION_MSG = '\nFor correct using this application, after start choose the mode of program.' \
                  '\nText-counter mode is count the amount of your text in a file.' \
                  '\nText-substitute mode replaces a string with another in the whole file.' \
                  '\nYour file has to be in the program repository.'
ERROR_MSG = "The file you were looking for was not found. Please,try again."


class FileParser:
    def __init__(self, file_path, string_to_change, new_string=''):
        self.file_path = file_path
        self.string_to_change = string_to_change
        self.new_string = new_string

    # this method initializes the second mode.
    def change_content(self):
        try:
            with open(path, 'r+') as file:
                old_data = file.read()
                new_data = old_data.replace(self.string_to_change, self.new_string)
                file.write(new_data)
                print(f"String {self.string_to_change} has changed on {self.new_string}.")
        except FileNotFoundError:
            print(ERROR_MSG)

    # this method initializes the first mode.
    def find_content(self):
        result = 0
        try:
            with open(path, 'r') as file:
                for line in file:
                    comparation = re.findall(string_to_find, line)
                    result += len(comparation)
                print(f'Text {self.string_to_change} appears {result} times in the file.')
        except FileNotFoundError:
            return print(ERROR_MSG)


if __name__ == '__main__':
    while True:
        mode = input(WELCOME_MSG)

        if mode == '':
            print(INFORMATION_MSG)
        elif mode == '1':
            try:
                incoming_data = input(FRST_MODE_MSG).split(',')
                path, string_to_find = incoming_data
            except ValueError:
                continue
            f = FileParser(path, string_to_find)
            f.find_content()
        elif mode == '2':
            try:
                incoming_data = input(SEC_MODE_MSG).split(',')
                path, old_str, new_str = incoming_data
            except ValueError:
                continue
            f = FileParser(path, old_str, new_str)
            f.change_content()
        else:
            continue

        iteration = input('Start the program one more time?[y/n]: ')
        if iteration.lower() not in ['y', 'yes']:
            break
