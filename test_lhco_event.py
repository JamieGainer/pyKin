import unittest

import lhco_event


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