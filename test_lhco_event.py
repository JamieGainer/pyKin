import unittest

import lhco_event
import physics_object

class TestLHCOEvent(unittest.TestCase):

    # tests
    def test_create_event_and_set_event_number(self):
        new_event = lhco_event.LHCOEvent(event_number=1)
        self.assertEqual(new_event.event_number, 1)

    def test_create_event_and_set_trigger_word(self):
        new_event = lhco_event.LHCOEvent(trigger_word=1)
        self.assertEqual(new_event.trigger_word, 1)

    def test_init_event_from_string(self):
        event_number, trigger_word = [5, 3587]
        init_string = self.make_basic_string_with_event_number_and_trigger_word(event_number, trigger_word)
        self.verify_init_event_from_valid_string(init_string, event_number, trigger_word)

    def test_init_event_from_string_with_newline(self):
        event_number, trigger_word = [5, 3587]
        init_string = self.make_basic_string_with_event_number_and_trigger_word(event_number, trigger_word) + '\n'
        self.verify_init_event_from_valid_string(init_string, event_number, trigger_word)

    def test_wrong_number_of_fields_raises_exception(self):
        self.assert_assertion_error_raised_by_string("  0      2      5   3587 \n")

    def test_non_digit_character_raises_exception(self):
        self.assert_assertion_error_raised_by_string("#       5   3587 \n")

    def test_create_event_with_photon_from_strings(self):
        init_string = "   0           103   2563  \n"
        object_string = "   1    2   -1.219  4.739   449.95   0.11   1.0   0.0    12.15   0.0   0.0\n"
        event = lhco_event.LHCOEvent.init_from_string(init_string)
        event.add_physics_object()

    # helper methods
    def make_basic_string_with_event_number_and_trigger_word(self, event_number, trigger_word):
        return "  0             {0}   {1} ".format(event_number, trigger_word)

    def assert_assertion_error_raised_by_string(self, init_string):
        with self.assertRaises(AssertionError):
            new_event = lhco_event.LHCOEvent.init_from_string(init_string)

    def verify_init_event_from_valid_string(self, init_string, event_number, trigger_word):
        new_event = lhco_event.LHCOEvent.init_from_string(init_string)
        self.assertListEqual([new_event.event_number, new_event.trigger_word], [event_number, trigger_word])

if __name__ == '__main__':
    unittest.main()