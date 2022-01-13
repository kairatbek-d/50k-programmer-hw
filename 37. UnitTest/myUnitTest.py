import unittest
from func import my_sum

class MySumTest(unittest.TestCase):
    def test_sum_two_numbers(self):
        assert my_sum(3, 5) == 8
        # self.assertEqual(my_sum(7, 2), 9)
    
    def test_sum_two_string(self):
        assert my_sum("Hello", "World") == "HelloWorld"
    
    def test_sum_num_and_str(self):
        with self.assertRaises(TypeError):
            my_sum(10, 'equal')
    
    def test_sum_str_and_num(self):
        with self.assertRaises(TypeError):
            my_sum('equal', 10)

unittest.main()

# python myUnitTest.py -v => for to see each