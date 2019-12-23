import unittest
import lhco_event


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