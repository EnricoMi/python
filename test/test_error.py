import unittest


class ErrorTest(unittest.TestCase):
    import sys
    if sys.version_info[0:2] == (3, 6):
        raise RuntimeError()


if __name__ == '__main__':
    unittest.main()
