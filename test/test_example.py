import random
import unittest


class ExampleTest(unittest.TestCase):

    def test_that_succeeds(self):
        self.assertEqual(True, True)

    def test_that_fails(self):
        self.assertEqual(True, False)

    def test_that_is_skipped(self):
        self.skipTest('not implemented')

    def test_that_errors(self):
        raise RuntimeError()

    def test_that_is_flaky(self):
        if random.random() < 0.5:
            self.fail('flaky')


if __name__ == '__main__':
    unittest.main()
