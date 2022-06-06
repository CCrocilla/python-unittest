""" Imports """
import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    """ Test 1.0 """
    # def test_function_return_True(self):
    #     self.assertTrue(even_number_of_evens([]))

    # Use Descriptive name that details what it is testing
    def test_throws_error_if_value_passed_in_is_not_listed(self):
        """
        Checks if TypeError is raised when the
        function is called with value 4
        """
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        """ Check if the list is empty/Value are evens """
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


if __name__ == '__main__':
    unittest.main()
