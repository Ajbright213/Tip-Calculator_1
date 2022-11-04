import io
from unittest import mock, TestCase

from tip_calculator import tip_user_input, calculate_total_bill


class TestLibraryFunctions(TestCase):

    @mock.patch('builtins.input', side_effect=['15', '1', '20', 'no'])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tip_user_input1(self, mock_stdout, mock_input):
        tip_user_input()

        expected = "Each person's total is $19.5\nThe total bill with tip and tax is $19.5\nThanks! Have a great day!\n"

        self.assertEqual(expected, mock_stdout.getvalue())
        

    @mock.patch('builtins.input', side_effect=['25000000', '3', '31', 'no'])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tip_user_input2(self, mock_stdout, mock_input):
        tip_user_input()

        expected = "Each person's total is $11750000.0\nThe total bill with tip and tax is $35250000.0\nThanks! Have a great day!\n"

        self.assertEqual(expected, mock_stdout.getvalue())
       
       

        

    @mock.patch('builtins.input', side_effect=['78.99', '6', '0', 'no'])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tip_user_input3(self, mock_stdout):
        tip_user_input()


        expected = "Each person's total is $14.48\nThe total bill with tip and tax is $86.89\nThanks! Have a great day!\n"

        self.assertEqual(expected, mock_stdout.getvalue())

        

    @mock.patch('builtins.input', side_effect=['5000', '876', '12', 'no'])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tip_user_input4(self, mock_stdout):
        tip_user_input()


        expected = "Each person's total is $6.96\nThe total bill with tip and tax is $6100.0\nThanks! Have a great day!\n"

        self.assertEqual(expected, mock_stdout.getvalue())

        