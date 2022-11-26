from operations import *
from utils import *
import unittest
def main():
    #print(fac(6))
    #print(converting_string_nums_to_nums_list("23+7a-1!5.4-- 12"))
    #print(converting_string_operators_to_operators_list("(7+4)+(5)"))
    #print(parse_operators("23+7a-1!5.4-- 12"))
    #print(clean_spaces("23+7a-1!5.4--12"))
    #print()
    #print(parse_operators("(7+4)+(5)"))
    #print(validate_brackets("(7+4)+(5)"))
    #print(find_index_of_closing_bracket(['(','(','^','*',')','@',')','%'],1))
    tester = TestUtils()
    #tester.test_find_index_of_closing_bracket()
    #tester.test_brackets_check()
    tester.test_find_numbers_between_operators_1()
class TestUtils(unittest.TestCase):
    def test_find_index_of_closing_bracket(self):
      t = find_index_of_closing_bracket(['(','(','^','*',')','@',')','%'],1)
      self.assertEqual(4,t)
    def test_brackets_check(self):
      t = validate_brackets("(6*(~(7+8)*8))+((~6+2)%3)")

    def test_find_numbers_between_operators_1(self):
        t = "(6*((7+8)*8))!+((6+2)%3)"
        operators_list = converting_string_operators_to_operators_list(t)
        num_of_nums = find_numbers_between_operators(operators_list,0,len(t))
        self.assertEqual(7, num_of_nums)
if __name__ == "__main__":
    main()