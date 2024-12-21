import unittest
from unittest.mock import patch
from main import (
    get_bet_numbers,
    get_number,
    get_wager,
    generate_lucky_numbers,
    process_bet
)

class TestBig6Game(unittest.TestCase):

    @patch('builtins.input', side_effect=['2'])
    def test_get_bet_numbers_valid(self, mock_input):
        self.assertEqual(get_bet_numbers(), 2)

    @patch('builtins.input', side_effect=['STOP'])
    def test_get_bet_numbers_stop(self, mock_input):
        self.assertEqual(get_bet_numbers(), 'STOP')


    @patch('builtins.input', side_effect=['3'])
    def test_get_number_valid(self, mock_input):
        self.assertEqual(get_number("Enter a number: "), 3)

    @patch('builtins.input', side_effect=['7', '1'])
    def test_get_number_invalid_then_valid(self, mock_input):
        self.assertEqual(get_number("Enter a number: "), 1)

    @patch('builtins.input', side_effect=['100'])
    def test_get_wager_valid(self, mock_input):
        self.assertEqual(get_wager("Enter your wager: "), 100)

    @patch('builtins.input', side_effect=['0', '10'])
    def test_get_wager_invalid_then_valid(self, mock_input):
        self.assertEqual(get_wager("Enter your wager: "), 10)

    def test_generate_lucky_numbers(self):
        lucky_numbers = generate_lucky_numbers()
        self.assertEqual(len(lucky_numbers), 3)
        self.assertTrue(all(1 <= num <= 6 for num in lucky_numbers))

    def test_process_bet_win_once(self):
        lucky_numbers = [1, 2, 3]
        result = process_bet(lucky_numbers, 1, 50)
        self.assertEqual(result, 50)

    def test_process_bet_win_twice(self):
        lucky_numbers = [1, 1, 3]
        result = process_bet(lucky_numbers, 1, 50)
        self.assertEqual(result, 100)

    def test_process_bet_win_three_times(self):
        lucky_numbers = [2, 2, 2]
        result = process_bet(lucky_numbers, 2, 50)
        self.assertEqual(result, 150)

    def test_process_bet_lose(self):
        lucky_numbers = [3, 4, 5]
        result = process_bet(lucky_numbers, 1, 50)
        self.assertEqual(result, -50)

if __name__ == "__main__":
    unittest.main()