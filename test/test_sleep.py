import time
import unittest


class SleepTest(unittest.TestCase):

    def test_sleep(self):
        time.sleep(90)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
