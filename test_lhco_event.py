import unittest
import lhco_event


class TestLHCOEvent(unittest.TestCase):

    def test_create_event_and_set_event_number(self):
        new_event = lhco_event.LHCOEvent(event_number=1)
        self.assertEqual(new_event.event_number, 1)

    def test_create_event_and_set_trigger_word(self):
        new_event = lhco_event.LHCOEvent(trigger_word=1)
        self.assertEqual(new_event.trigger_word, 1)

    def test_init_event_from_string(self):
        init_string = "  0             5   3587 "
        new_event = lhco_event.LHCOEvent.init_from_string(init_string)
        properties_list = [new_event.event_number, new_event.trigger_word]
        self.assertListEqual(properties_list, [5, 3587])

if __name__ == '__main__':
    unittest.main()