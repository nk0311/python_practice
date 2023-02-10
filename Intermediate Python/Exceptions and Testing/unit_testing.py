import unittest

def multipy(x, y):
    return x * y

# Usuall tests live in a tests file, or module, not inline
class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multipy(test_x, test_y), 50)


if __name__ == "__main__":
    unittest.main()

