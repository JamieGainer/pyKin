import unittest
import lhco_event
import four_vector

class TestPhysicsObject(unittest.TestCase):

    lhco_object_string = "   1    2   -1.219  4.739   449.95   0.11   1.0   0.0    12.15   0.0   0.0 "

    def test_physics_object_number(self):
        new_physics_object = lhco_event.PhysicsObject(object_number=1)
        self.assertEqual(new_physics_object.object_number, 1)

    def test_physics_object_typ(self):
        new_physics_object = lhco_event.PhysicsObject(type=1)
        self.assertEqual(new_physics_object.type, 1)

    def test_physics_object_eta(self):
        new_physics_object = lhco_event.PhysicsObject(eta=1.0)
        self.assertEqual(new_physics_object.eta, 1.0)

    def test_physics_object_phi(self):
        new_physics_object = lhco_event.PhysicsObject(phi=1)
        self.assertEqual(new_physics_object.phi, 1.0)

    def test_physics_object_pt(self):
        new_physics_object = lhco_event.PhysicsObject(pt=1.0)
        self.assertEqual(new_physics_object.pt, 1.0)

    def test_physics_object_mass(self):
        new_physics_object = lhco_event.PhysicsObject(mass=1.0)
        self.assertEqual(new_physics_object.mass, 1.0)

    def test_physics_object_jmass_as_mass(self):
        new_physics_object = lhco_event.PhysicsObject(jmass=1.0)
        self.assertEqual(new_physics_object.mass, 1.0)

    def test_physics_object_jmass_as_mass(self):
        new_physics_object = lhco_event.PhysicsObject(jmass=1.0)
        self.assertEqual(new_physics_object.mass, 1.0)

#    def test_physics_object_jmass_as_jmass(self):
#        new_physics_object = lhco_event.PhysicsObject(jmass=1.0)
#        self.assertEqual(new_physics_object.jmass, 1.0)

    def test_physics_object_n_tracks(self):
        new_physics_object = lhco_event.PhysicsObject(n_tracks=1.0)
        self.assertEqual(new_physics_object.n_tracks, 1.0)

    def test_physics_object_ntrk_as_n_tracks(self):
        new_physics_object = lhco_event.PhysicsObject(ntrk=1.0)
        self.assertEqual(new_physics_object.n_tracks, 1.0)

#    def test_physics_object_ntrk_as_ntrk(self):
#        new_physics_object = lhco_event.PhysicsObject(ntrk=1.0)
#        self.assertEqual(new_physics_object.ntrk, 1.0)

    def test_physics_object_btag(self):
        new_physics_object = lhco_event.PhysicsObject(btag=1)
        self.assertEqual(new_physics_object.btag, 1.0)

    def test_physics_object_had_em(self):
        new_physics_object = lhco_event.PhysicsObject(had_em=1.0)
        self.assertEqual(new_physics_object.had_em, 1.0)

    def test_physics_object_dummy1(self):
        new_physics_object = lhco_event.PhysicsObject(dummy1=1.0)
        self.assertEqual(new_physics_object.dummy1, 1.0)

    def test_physics_object_dummy2(self):
        new_physics_object = lhco_event.PhysicsObject(dummy2=1.0)
        self.assertEqual(new_physics_object.dummy2, 1.0)


class TestLHCOEvent(unittest.TestCase):

    blank_object_register = {i: [] for i in range(lhco_event.num_object_types)}

    def test_object_register_exists(self):
        new_event = lhco_event.LHCOEvent()
        self.assertDictEqual(self.blank_object_register, new_event.object_register)

    def test_create_event_and_set_event_number(self):
        new_event = lhco_event.LHCOEvent(event_number=1)
        self.assertEqual(new_event.event_number, 1)

    def test_create_event_and_set_trigger_word(self):
        new_event = lhco_event.LHCOEvent(trigger_word=1)
        self.assertEqual(new_event.trigger_word, 1)

if __name__ == '__main__':
    unittest.main()