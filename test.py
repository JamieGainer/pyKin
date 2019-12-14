import unittest
import lorentz

import numpy as np

class TestFourVector(unittest.TestCase):

    a = lorentz.FourVector(10., 3., 4., 5.)
    def compare_phi_from_vector_with_given_phi_and_phi(self, phi):
        a = lorentz.FourVector(10., 5. * np.cos(phi), 5. * np.sin(phi), 5.)
        self.assertAlmostEqual(a.phi, phi)

    def test_obtain_p_t(self):
        self.assertEqual(self.a.p_T, 5.)

    def test_obtain_M(self):
        self.assertAlmostEqual(self.a.M, np.sqrt(50.))

    def test_obtain_p(self):
        self.assertAlmostEqual(self.a.p, np.sqrt(50.))

    def test_obtain_phi_eq_phi_over_4(self):
        self.compare_phi_from_vector_with_given_phi_and_phi(np.pi / 4)

    def test_obtain_phi_eq_1(self):
        self.compare_phi_from_vector_with_given_phi_and_phi(1.)

    def test_obtain_phi_eq_3(self):
        self.compare_phi_from_vector_with_given_phi_and_phi(3.)

    def test_obtain_phi_eq_5(self):
        self.compare_phi_from_vector_with_given_phi_and_phi(5.)


if __name__ == '__main__':
    unittest.main()
