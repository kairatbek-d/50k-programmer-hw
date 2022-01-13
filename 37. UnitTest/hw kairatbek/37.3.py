import unittest
from _37_2 import excelFunc

class MyExcelFuncTest(unittest.TestCase):
    def test_cells_more_four(self):
        assert excelFunc("Bill", 44, 32, 56, 44, yacheika="E5") == 44
    
    def test_if_cell_equalTo_one(self):
        with self.assertRaises(AttributeError):
            excelFunc("Bill", 44, 32, 56, 44, yacheika=1)
    
    def test_if_cell_equalTo_zero(self):
        with self.assertRaises(IndexError):
            excelFunc("Bill", 44, 32, 56, 44, yacheika=0)
    
    def test_if_first_second_are_str(self):
        self.assertEqual(excelFunc("Bill", "John", 44, 44, yacheika="E5"), 44)

unittest.main()

# python 37.3.py -v => for to see each