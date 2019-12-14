import unittest
import lorentz

class TestFourVector(unittest.TestCase):

    a = lorentz.FourVector([1, 0, 0, 0], '^mu', 'lab')

if __name__ == '__main__':
    unittest.main()
