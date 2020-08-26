import unittest


class ErrorTest(unittest.TestCase):
    raise RuntimeError()


if __name__ == '__main__':
    unittest.main()
