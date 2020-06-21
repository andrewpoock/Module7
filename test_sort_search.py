from fun_with_collections import sort_search
import unittest
import unittest.mock as mock

class TestListElements(unittest.TestCase):
    def test_sort(self):
        with mock.patch('builtins.input', side_effect=[2, 1, 3]):
            assert sort_search.sort_list() == [1, 2, 3]
    def test_found(self):
        with mock.patch('builtins.input', side_effect=[2, 14, 3]):
            assert sort_search.search_list() == 'The index of 14: 1'
    def test_found(self):
        with mock.patch('builtins.input', side_effect=[2, 1, 3]):
            assert sort_search.search_list() == -1


if __name__ == '__main__':
    unittest.main()
