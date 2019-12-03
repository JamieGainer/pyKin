import unittest

import lorentz

class TestFourVector(unittest.TestCase):

    a = lorentz.FourVector([1, 0, 0, 0], '^mu', 'lab')

    # Creation of four vectors

    def test_that_four_vector_must_have_raised_or_lowered_index(self) -> None:
        with self.assertRaises(ValueError):
            a = lorentz.FourVector([1, 0, 0, 0], 'mu', 'lab')

    # Equality of foru vectors

    def test_two_four_vectors_are_equal(self) -> None:
        b = lorentz.FourVector([1, 0, 0, 0], '^mu', 'lab')
        self.assertEqual(self.a, b)

    def test_two_four_vectors_are_different_if_different_values(self) -> None:
        a = lorentz.FourVector([2, 0, 0, 0], '^mu', 'lab')
        self.assertNotEqual(a, self.a)

    def test_two_four_vectors_are_different_if_different_indices(self) -> None:
        a = lorentz.FourVector([1, 0, 0, 0], '^nu', 'lab')
        self.assertNotEqual(a, self.a)

    def test_two_four_vectors_are_different_if_different_frames(self) -> None:
        a = lorentz.FourVector([1, 0, 0, 0], '^mu', 'other')
        self.assertNotEqual(a, self.a)

    # Sum of four vectors

    def test_sum_of_two_four_vectors(self) -> None:
        a = lorentz.FourVector([0.5, 0, 0, 3], '^mu', 'lab')
        b = lorentz.FourVector([0.5, 0, 0, -3], '^mu', 'lab')
        self.assertEqual(a + b, self.a)

if __name__ == '__main__':
    unittest.main()
