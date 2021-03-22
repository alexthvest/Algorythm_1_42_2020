import unittest
import pogtest

from module2 import sort_process, pairs_sort, merge_sort_with_borders
from module2 import number_of_inversions, number_of_different, warehouse, radix_sort

from module3 import substring_search, circular_shift


def load_tests(loader, tests, ignore):
    modules = [
        sort_process,
        pairs_sort,
        merge_sort_with_borders,
        number_of_inversions,
        number_of_different,
        warehouse,
        radix_sort,

        substring_search,
        circular_shift
    ]

    for module in modules:
        tests.addTests(pogtest.DocTestSuite(module))

    return tests


if __name__ == '__main__':
    unittest.main()
