UNITS = {
    '0': 'ноль',
    '1': ('один', 'одна'),
    '2': ('два', 'две'),
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять'
        }
DOZENS = {
    '10': 'десять',
    '11': 'одиннадцать',
    '12': 'двенадцать',
    '13': 'тринадцать',
    '14': 'четырнадцать',
    '15': 'пятнадцать',
    '16': 'шестнадцать',
    '17': 'семнадцать',
    '18': 'восемнадцать',
    '19': 'девятнадцать',
    '2': 'двадцать',
    '3': 'тридцать',
    '4': 'сорок',
    '5': 'пятьдесят',
    '6': 'шестьдесят',
    '7': 'семьдесят',
    '8': 'восемьдесят',
    '9': 'девяносто'
         }
HUNDREDS = {
    '1': 'сто',
    '2': 'двести',
    '3': 'триста',
    '4': 'четыреста',
    '5': 'пятьсот',
    '6': 'шестьсот',
    '7': 'семьсот',
    '8': 'восемьсот',
    '9': 'девятьсот',
           }

THOUSANDS = ['тысяча', 'тысячи', 'тысяч']
MILLIONS = ['миллион', 'миллиона', 'миллионов']
BILLIONS = ['миллиард', 'миллиарда', 'миллиардов']
TRILLIONS = ['триллион', 'триллиона', 'триллионов']
QUADRILLIONS = ['квадриллион', 'квадриллиона', 'квадриллионов']
QUINTILLIONS = ['квинтиллион', 'квинтиллиона', 'квинтиллионов']
SEXTILLIONS = ['секстиллион', 'секстиллиона', 'секстиллионов']

RANKS = [THOUSANDS, MILLIONS, BILLIONS, TRILLIONS, QUADRILLIONS, QUINTILLIONS, SEXTILLIONS]


WELCOME_MSG = '\n*** Welcome to the Numbers Convertor ***'\
              '\nFor the correct work, enter a number up to sextillions: '
ERROR_MSG = "\nYour number is bigger than 999 sextillions, the coder is lazy and didn't make this functional. " \
            "\nPlease, try again with number less than 999 sextillions."
VALUE_ERROR_MSG = '\nYour number is incorrect. Please, try again with integer number up to 999 sextillions.'


class NumbersRepresentation:
    """
    This class made to convert numbers to their word's representations.
    """
    def __init__(self, number: int):
        self.number = number
        self.iteration = 0

    # this method converts a number into a three-digits data_list.
    # >>> ['123','456','789']
    def list_packing(self):
        return f'{self.number:,}'.split(',')

    # method counts ranks and adds it for the special data_list.
    def get_rank_counts(self, enter_list):
        self.suitable_ranks = RANKS[:len(enter_list)-1]
        return self.suitable_ranks

    def first_translation_method(self, counter, group, data_list):
        for digit in group:
            if digit == '0':
                counter += 1
                continue
            elif counter in [2, 5, 8, 11, 14, 17, 20]:
                if digit in ['1', '2'] and group == data_list[-2]:
                    self.string_result.append(UNITS.get(digit)[1])
                    counter += 1
                    continue
                elif digit in ['1', '2']:
                    self.string_result.append(UNITS.get(digit)[0])
                    counter += 1
                    continue
                else:
                    self.string_result.append(UNITS.get(digit))
            counter += 1
        return counter, self.string_result

    def second_translation_method(self, counter, group):
        for digit in group:
            if digit == '0':
                counter += 1
                continue
            if counter in [1, 4, 7, 10, 13, 16, 19]:
                self.string_result.append(DOZENS.get(digit + group[-1]))
            counter += 1
        return counter, self.string_result

    def third_translation_method(self, counter, group, data_list):
        for digit in group:
            if digit == '0':
                counter += 1
                continue
            if counter in [1, 4, 7, 10, 13, 16, 19]:
                self.string_result.append(DOZENS.get(digit))
            elif counter in [2, 5, 8, 11, 14, 17, 20]:
                if digit in ['1', '2'] and group == data_list[-2]:
                    self.string_result.append(UNITS.get(digit)[1])
                    counter += 1
                    continue
                elif digit in ['1', '2']:
                    self.string_result.append(UNITS.get(digit)[1])
                    counter += 1
                    continue
                else:
                    self.string_result.append(UNITS.get(digit))
            counter += 1
        return counter, self.string_result

    def fourth_translation_method(self, counter, group, data_list):
        for digit in group:
            if digit == '0':
                counter += 1
                continue
            if counter in [0, 3, 6, 9, 12, 15, 18, 21]:
                self.string_result.append(HUNDREDS.get(digit))
            elif counter in [2, 5, 8, 11, 14, 17, 20]:
                if len(data_list) >= 2 and digit in ['1', '2'] and group == data_list[-2]:
                    self.string_result.append(UNITS.get(digit)[1])
                    counter += 1
                    continue
                elif digit in ['1', '2'] and group != data_list[-2]:
                    self.string_result.append(UNITS.get(digit)[0])
                    counter += 1
                    continue
                else:
                    self.string_result.append(UNITS.get(digit))
            counter += 1
        return counter, self.string_result

    def fifth_translation_method(self, counter, group):
        for digit in group:
            if counter in [0, 3, 6, 9, 12, 15, 18, 21]:
                self.string_result.append(HUNDREDS.get(digit))
            elif counter in [1, 4, 7, 10, 13, 16, 19]:
                self.string_result.append(DOZENS.get(digit + group[-1]))
            counter += 1
        return counter, self.string_result

    def sixth_translation_method(self, counter, group, data_list):
        for digit in group:
            if counter in [0, 3, 6, 9, 12, 15, 18, 21, 24]:
                self.string_result.append(HUNDREDS.get(digit))
            elif counter in [1, 4, 7, 10, 13, 16, 19, 22]:
                self.string_result.append(DOZENS.get(digit))
            elif counter in [2, 5, 8, 11, 14, 17, 20, 23]:
                if digit == '0':
                    counter += 1
                    continue
                elif len(data_list) >= 2 and digit in ['1', '2'] and group == data_list[-2]:
                    self.string_result.append(UNITS.get(digit)[1])
                    counter += 1
                    continue
                elif digit in ['1', '2']:
                    self.string_result.append(UNITS.get(digit)[0])
                    counter += 1
                    continue
                else:
                    self.string_result.append(UNITS.get(digit))
            counter += 1
        return counter, self.string_result

    # method for converting a data_list of numbers to a data_list of words.
    def sub_number_representation(self, data_list):
        self.string_result = []

        try:
            if len(str(self.number)) in [3, 6, 9, 12, 15, 18, 21, 24]:
                self.iteration = 0
            elif len(str(self.number)) in [1, 4, 7, 10, 13, 16, 19, 22]:
                self.iteration = 2
            elif len(str(self.number)) in [2, 5, 8, 11, 14, 17, 20, 23]:
                self.iteration = 1
        except NameError:
            print(ERROR_MSG)

        # remember, data_list seems like:
        # >>> ['123','456','789']
        # in this case, '123' - first group, etc.
        for group in data_list:
            # if first, second digits equal '0'.
            if len(group) >= 2 and group[0] == group[1] == '0':
                self.iteration, self.string_result = self.first_translation_method(self.iteration, group, data_list)

            # if first digit equal '0' and 2,3 less than 19.
            elif group[0] == '0' and int(str(group[-2])+str(group[-1])) <= 19:
                self.iteration, self.string_result = self.second_translation_method(self.iteration, group)

            # if digit '0' is first in the group.
            elif len(group) >= 2 and group[0] == '0':
                self.iteration, self.string_result = self.third_translation_method(self.iteration, group, data_list)

            # if digit '0' in the middle of group.
            elif len(group) >= 2 and group[-2] == '0':
                self.iteration, self.string_result = self.fourth_translation_method(self.iteration, group, data_list)

            # if last two numbers in group less than 19.
            elif len(group) >= 2 and int(str(group[-2])+str(group[-1])) <= 19:
                self.iteration, self.string_result = self.fifth_translation_method(self.iteration, group)
            else:
                # all another cases.
                self.iteration, self.string_result = self.sixth_translation_method(self.iteration, group, data_list)

            # in this block we add the right ranks for number.
            if self.suitable_ranks:
                if group == '000':
                    self.suitable_ranks.pop()
                    continue
                if len(group) > 1 and group[-2] + group[-1] in ['11', '12', '13', '14']:
                    ending = 2
                elif len(data_list) >= 2 and group[-1] in ['2', '3', '4']:
                    ending = 1
                elif group[-1] == '1':
                    ending = 0
                else:
                    ending = 2

                self.string_result.append(self.suitable_ranks[-1][ending])
                self.suitable_ranks.pop()
                self.iteration = 0
        return self.string_result


def main(class_instance):
    ordered_list = class_instance.list_packing()
    class_instance.get_rank_counts(ordered_list)

    return ' '.join(class_instance.sub_number_representation(ordered_list)).capitalize()


if __name__ == '__main__':
    while True:
        incoming_data = input(WELCOME_MSG)
        try:
            numb = NumbersRepresentation(int(incoming_data))
        except ValueError:
            print(VALUE_ERROR_MSG)
            continue

        print(main(numb))

        iteration = input('Start the program one more time?[y/n]: ')
        if iteration.lower() not in ['y', 'yes']:
            break
