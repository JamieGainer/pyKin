import unittest

import numpy as np

from pykin.lhco import PhysicsObject


class TestPhysicsObject(unittest.TestCase):

    lhco_object_string = "   1    2   -1.219  4.739   449.95   0.11   1.0   0.0    12.15   0.0   0.0 "

    def test_physics_object_number(self):
        new_physics_object = PhysicsObject(object_number=1)
        self.assertEqual(new_physics_object.object_number, 1)

    def test_physics_object_typ(self):
        new_physics_object = PhysicsObject(type=1)
        self.assertEqual(new_physics_object.type, 1)

    def test_physics_object_eta(self):
        new_physics_object = PhysicsObject(eta=1.0)
        self.assertEqual(new_physics_object.eta, 1.0)

    def test_physics_object_phi(self):
        new_physics_object = PhysicsObject(phi=1)
        self.assertEqual(new_physics_object.phi, 1.0)

    def test_physics_object_pt(self):
        new_physics_object = PhysicsObject(pt=1.0)
        self.assertEqual(new_physics_object.pt, 1.0)

    def test_physics_object_mass(self):
        new_physics_object = PhysicsObject(mass=1.0)
        self.assertEqual(new_physics_object.mass, 1.0)

    def test_physics_object_jmass_as_mass(self):
        new_physics_object = PhysicsObject(jmass=1.0)
        self.assertEqual(new_physics_object.mass, 1.0)

    def test_physics_object_jmass_as_jmass(self):
        new_physics_object = PhysicsObject(jmass=1.0)
        self.assertEqual(new_physics_object.jmass, 1.0)

    def test_physics_object_n_tracks(self):
        new_physics_object = PhysicsObject(n_tracks=1.0)
        self.assertEqual(new_physics_object.n_tracks, 1.0)

    def test_physics_object_ntrk_as_n_tracks(self):
        new_physics_object = PhysicsObject(ntrk=1.0)
        self.assertEqual(new_physics_object.n_tracks, 1.0)

    def test_physics_object_ntrk_as_ntrk(self):
        new_physics_object = PhysicsObject(ntrk=1.0)
        self.assertEqual(new_physics_object.ntrk, 1.0)

    def test_physics_object_btag(self):
        new_physics_object = PhysicsObject(btag=1)
        self.assertEqual(new_physics_object.btag, 1.0)

    def test_physics_object_had_em(self):
        new_physics_object = PhysicsObject(had_em=1.0)
        self.assertEqual(new_physics_object.had_em, 1.0)

    def test_physics_object_dummy1(self):
        new_physics_object = PhysicsObject(dummy1=1.0)
        self.assertEqual(new_physics_object.dummy1, 1.0)

    def test_physics_object_dummy2(self):
        new_physics_object = PhysicsObject(dummy2=1.0)
        self.assertEqual(new_physics_object.dummy2, 1.0)

    def test_physics_object_nonsense_name(self):
        with self.assertRaises(ValueError):
            new_physics_object = PhysicsObject(zxqy=1.0)

    def test_physics_object_objectnumber_as_object_number(self):
        new_physics_object = PhysicsObject(objectnumber=1)
        self.assertEqual(new_physics_object.object_number, 1)

    def test_physics_object_ETA_as_eta(self):
        new_physics_object = PhysicsObject(ETA=1.0)
        self.assertEqual(new_physics_object.eta, 1.0)

    def test_physics_object_ETA_as_ETA(self):
        new_physics_object = PhysicsObject(ETA=1.0)
        self.assertEqual(new_physics_object.ETA, 1.0)

    def test_physics_object_eta_as_ETA(self):
        new_physics_object = PhysicsObject(eta=1.0)
        self.assertEqual(new_physics_object.ETA, 1.0)

    def test_physics_object_theta_from_vector(self):
        new_physics_object = PhysicsObject(pt=1., eta=0., phi=0., mass=0.)
        new_physics_object.set_attributes_from_four_vector()
        self.assertAlmostEqual(new_physics_object.theta, np.pi / 2)

    def test_physics_object_energy_from_vector(self):
        pt, mass = 3., 4.
        new_physics_object = PhysicsObject(pt=pt, eta=0., phi=0., mass=mass)
        new_physics_object.set_attributes_from_four_vector()
        self.assertAlmostEqual(new_physics_object.energy, np.sqrt(pt**2 + mass**2))

    def test_physics_object_energy_from_vector(self):
        pt, mass = 3., 4.
        new_physics_object = PhysicsObject(pt=pt, eta=0., phi=0., mass=mass)
        new_physics_object.set_attributes_from_four_vector()
        self.assertAlmostEqual(new_physics_object.energy, np.sqrt(pt**2 + mass**2))

    def test_physics_object_E_from_vector(self):
        pt, mass = 3., 4.
        new_physics_object = PhysicsObject(pt=pt, eta=0., phi=0., mass=mass)
        new_physics_object.set_attributes_from_four_vector()
        self.assertAlmostEqual(new_physics_object.E, np.sqrt(pt**2 + mass**2))

    def test_physics_object_px_from_vector(self):
        pt, mass = 3., 1.2
        new_physics_object = PhysicsObject(pt=pt, eta=0., phi=0., mass=mass)
        new_physics_object.set_attributes_from_four_vector()
        self.assertAlmostEqual(new_physics_object.px, pt)

    def test_physics_object_py_from_vector(self):
        pt, mass = 3., 1.2
        new_physics_object = PhysicsObject(pt=pt, eta=0., phi=np.pi / 2, mass=mass)
        new_physics_object.set_attributes_from_four_vector()
        self.assertAlmostEqual(new_physics_object.py, pt)

    def test_physics_object_from_string(self):
        string = "   1    2   -1.219  4.739   449.95   0.11   1.0   0.0    12.15   0.0   0.0 "
        new_physics_object = PhysicsObject.set_from_string(string)
        string_values = list(map(float, string.split()))
        object_values = [getattr(new_physics_object, attr) for attr in
                         ["object_number", "type", "eta", "phi", "pt", "mass", "n_tracks", "btag",
                          "had_em", "dummy1", "dummy2"]]
        self.assertListEqual(string_values, object_values)

    def test_assertion_error_raised_from_string_with_too_many_fields(self):
        string = "   1    2   -1.219  4.739   449.95   0.11   1.0   0.0    12.15   0.0   0.0 2"
        with self.assertRaises(AssertionError):
            new_physics_object = PhysicsObject.set_from_string(string)

    def test_assertion_error_raised_from_string_with_too_few_fields(self):
        string = "   1    2   -1.219  4.739   449.95   0.11   1.0   0.0    12.15   0.0 "
        with self.assertRaises(AssertionError):
            new_physics_object = PhysicsObject.set_from_string(string)

    def test_assertion_error_raised_from_non_alphanumeric_character_in_string(self):
        string = "#   1    2   -1.219  4.739   449.95   0.11   1.0   0.0    12.15   0.0 "
        with self.assertRaises(AssertionError):
            new_physics_object = PhysicsObject.set_from_string(string)

if __name__ == '__main__':
    unittest.main()