from random import randint
import task_five
import unittest


class TestNumbersRepresentation(unittest.TestCase):
    """
    This class tests task_five.py
    """

    def test_get_numbers(self):
        self.assertEqual(task_five.main(task_five.NumbersRepresentation(1)), 'Один')
        self.assertEqual(task_five.main(task_five.NumbersRepresentation(150)), 'Сто пятьдесят')
        self.assertEqual(task_five.main(task_five.NumbersRepresentation(15119)), 'Пятнадцать тысяч сто девятнадцать')
        self.assertEqual(task_five.main(task_five.NumbersRepresentation(102101777305)),
                         'Сто два миллиарда сто один миллион семьсот семьдесят семь тысяч триста пять')
        self.assertEqual(task_five.main(task_five.NumbersRepresentation(800)), 'Восемьсот')
        self.assertEqual(task_five.main(task_five.NumbersRepresentation(101912)),
                         'Сто одна тысяча девятьсот двенадцать')
        self.assertEqual(task_five.main(task_five.NumbersRepresentation(54000212)),
                         'Пятьдесят четыре миллиона двести двенадцать')
        self.assertEqual(task_five.main(task_five.NumbersRepresentation(11540)), 'Одиннадцать тысяч пятьсот сорок')

    def test_random_numbers(self):
        for i in range(5):
            number = randint(1, 9)
            print(number)
            self.assertEqual(task_five.main(task_five.NumbersRepresentation(number)),
                             (task_five.UNITS[str(number)]).capitalize() if number not in [1, 2] else
                             (task_five.UNITS[str(number)][0]).capitalize())

    def test_get_number_rank(self):
        first_number = task_five.NumbersRepresentation(595)
        self.assertEqual(task_five.NumbersRepresentation.get_rank_counts(first_number, ['595']), [])

        second_number = task_five.NumbersRepresentation(595150)
        self.assertEqual(task_five.NumbersRepresentation.get_rank_counts(second_number, ['595', '150']),
                         [task_five.THOUSANDS])

        third_number = task_five.NumbersRepresentation(595150200)
        self.assertEqual(task_five.NumbersRepresentation.get_rank_counts(third_number, ['595', '150', '200']),
                         [task_five.THOUSANDS, task_five.MILLIONS])


if __name__ == '__main__':
    unittest.main()
