#!/usr/bin/python3

"""Module containing
Unittest for function max_integer([])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def module_docstr_test(self):
        """Test len of module docsting"""
        mdl = __import__('6-max_integer').__doc__
        self.assertTrue(len(mdl) > 1)

    def function_docstr_test(self):
        """Test len of function docstring"""
        func = max_integer.__doc__
        self.assertTrue(len(func) > 1)

    def empty_list_test(self):
        """Tests for empty list []"""
        self.assertEqual(max_integer([]), None)

    def no_args_test(self):
        """Test for no args"""
        self.assertIsNone(max_integer())

    def one_element_test(self):
        """Test for only one arg to list"""
        self.assertEqual(max_integer([1]), 1)

    def positive_end_test(self):
        """Max at end of positive list"""
        ls = [10, 20, 30, 40, 50]
        self.assertEqual(max_integer(ls), 50)

    def positive_middle_test(self):
        """Max in middle of positive list"""
        ls = [10, 20, 50, 40, 30]
        self.assertEqual(max_integer(ls), 50)

    def positive_beginning_test(self):
        """Max at the begining of positive list"""
        ls = [50, 40, 30, 20, 10]
        self.assertEqual(max_integer(ls), 50)

    def one_negative_test(self):
        """List with one negative number"""
        ls = [20, 15, 10, -5, 1, 0]
        self.assertEqual(max_integer(ls), 20)

    def all_negative_test(self):
        """List with all negative numbers"""
        ls = [-20, -15, -10, -5, -1, -2]
        self.assertEqual(max_integer(ls), -1)

    def none_arg_test(self):
        """Test for passing None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def mixed_type_test(self):
        """Test for mixed types in list"""
        s = [0, "Win", 2, 4, 6]
        with self.assertRaises(TypeError):
            max_integer(s)

    def float_test(self):
        """Compare floats"""
        self.assertEqual(max_integer([1.0, 2.0, 1.5]), 2.0)

    def strings_test(self):
        """Use ascii to compare strs"""
        self.assertEqual(max_integer('WINnie'), 'n')


if __name__ == "__main__":
    unittest.main()
