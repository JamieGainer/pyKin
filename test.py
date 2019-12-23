import unittest
import lorentz

import numpy as np

E, px, py, pz = 10., 3., 4., 5

class TestFourVector(unittest.TestCase):

    a = lorentz.FourVector(E, px, py, pz)

    def test_obtain_p_t(self):
        self.assertEqual(self.a.p_T, pz)

    def test_obtain_M(self):
        self.assertAlmostEqual(self.a.M, np.sqrt(E**2 - px**2 - py**2 - pz**2))

    def test_obtain_p(self):
        self.assertAlmostEqual(self.a.p, np.sqrt(px**2 + py**2 + pz**2))

    def test_obtain_phi_eq_1(self):
        self._compare_phi_from_vector_with_given_phi_and_phi(1.)

    def test_obtain_phi_eq_3(self):
        self._compare_phi_from_vector_with_given_phi_and_phi(3.)

    def test_obtain_phi_eq_5(self):
        self._compare_phi_from_vector_with_given_phi_and_phi(5.)

    def test_obtain_theta_0_point_5(self):
        self._compare_theta_from_vector_with_given_theta_and_phi_and_theta(0.5)

    def test_obtain_theta_1(self):
        self._compare_theta_from_vector_with_given_theta_and_phi_and_theta(1., phi=2.0)

    def test_obtain_theta_2(self):
        self._compare_theta_from_vector_with_given_theta_and_phi_and_theta(2., phi=4.0)

    def test_obtain_eta_0(self):
        self._compare_eta_from_vector_with_given_theta_and_phi_and_theta(np.pi / 2)

    def test_obtain_eta_when_theta_eq_1(self):
        self._compare_eta_from_vector_with_given_theta_and_phi_and_theta(1., phi=2.0)

    def test_obtain_eta_when_theta_eq_2(self):
        self._compare_theta_from_vector_with_given_theta_and_phi_and_theta(2., phi=4.0)

    def test_define_four_vector_from_eta_phi_pt_M_when_theta_eq_0_point_5(self):
        self._can_we_redefine_four_vector_from_eta_phi_pt_M(0.5, 1.)

    def test_define_four_vector_from_eta_phi_pt_M_when_theta_eq_1(self):
        self._can_we_redefine_four_vector_from_eta_phi_pt_M(1., 3.)

    def test_define_four_vector_from_eta_phi_pt_M_when_theta_eq_2(self):
        self._can_we_redefine_four_vector_from_eta_phi_pt_M(2., 3., E=13., p=2.)

    # methods to streamline tests above
    def assertListAlmostEqual(self, a, b):
        self.assertEqual(len(a), len(b))
        for a_i, b_i in zip(a, b):
            self.assertAlmostEqual(a_i, b_i)

    def _compare_phi_from_vector_with_given_phi_and_phi(self, phi):
        a = lorentz.FourVector(10., 5. * np.cos(phi), 5. * np.sin(phi), 5.)
        self.assertAlmostEqual(a.phi, phi)

    def _compare_theta_from_vector_with_given_theta_and_phi_and_theta(self, theta, phi=1.):
        a = lorentz.FourVector(10., 5. * np.cos(phi) * np.sin(theta),
                               5. * np.sin(phi) * np.sin(theta),
                               5. * np.cos(theta))
        self.assertAlmostEqual(a.theta, theta)

    def _compare_eta_from_vector_with_given_theta_and_phi_and_theta(self, theta, phi=1.):
        a = lorentz.FourVector(10., 5. * np.cos(phi) * np.sin(theta),
                               5. * np.sin(phi) * np.sin(theta),
                               5. * np.cos(theta))
        self.assertAlmostEqual(a.eta, self._eta_as_a_function_of_theta(theta))

    def _eta_as_a_function_of_theta(self, theta):
        return -np.log(np.tan(theta / 2))

    def _generic_four_vector(self, theta, phi, E=10., p=5.):
        return lorentz.FourVector(E, p * np.sin(theta) * np.cos(phi),
                                  p * np.sin(theta) * np.sin(phi), p * np.cos(theta))

    def _component_list_from_four_vector(self, four_vector):
        return [four_vector.E, four_vector.p_x, four_vector.p_y, four_vector.p_z]

    def _can_we_redefine_four_vector_from_eta_phi_pt_M(self, theta, phi, E=10., p=5.):
        a = self._generic_four_vector(theta, phi, E=E, p=p)
        b = lorentz.FourVector.from_eta_phi_pt_M(a.eta, a.phi, a.p_T, a.M)
        self.assertListAlmostEqual(self._component_list_from_four_vector(a),
                                   self._component_list_from_four_vector(b))


if __name__ == '__main__':
    unittest.main()
