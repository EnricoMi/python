import unittest


class ExampleTest(unittest.TestCase):

    def test_example(self):
        self.assertEqual(True, True)

    def test_more(self):
        self.assertEqual(True, True)

    def test_fail(self):
        self.assertEqual(True, False)

    def test_skip(self):
        self.skipTest("not tested")

    def test_conditional_skip(self):
        import sys
        if sys.version_info[0:2] == (3, 6):
            self.skipTest('not tested')


if __name__ == '__main__':
    unittest.main()
