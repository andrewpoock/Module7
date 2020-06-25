from fun_with_collections import ss_array
import unittest


class TestListElements(unittest.TestCase):
    def test_sort(self):
        expected_list = ss_array.sort([2, 4, 1, 3])
        self.assertEqual(expected_list, [1, 2, 3, 4])

    def test_found(self):
        assert ss_array.search([2, 4, 3]) == 'The index of 4 is 1'

    def test_not_found(self):
        assert ss_array.search([2, 1, 3]) == -1


if __name__ == '__main__':
    unittest.main()
