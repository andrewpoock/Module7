from fun_with_collections import sort_search
import unittest


class TestListElements(unittest.TestCase):
    def test_sort(self):
        expected_list = sort_search.sort_list([2, 4, 1, 3])
        self.assertEqual(expected_list, [1, 2, 3, 4])

    def test_found(self):
        assert sort_search.search_list([2, 14, 3]) == 'The index of 14 is 1'

    def test_not_found(self):
        assert sort_search.search_list([2, 1, 3]) == -1


if __name__ == '__main__':
    unittest.main()
