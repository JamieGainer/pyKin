import unittest
import lhco_event

class TestLHCOEvent(unittest.TestCase):

    def test_create_event(self):
        new_event = lhco_event.LHCOEvent()

    def test_create_event_and_set_event_number(self):
        new_event = lhco_event.LHCOEvent(event_number=1)
        self.assertEqual(new_event.event_number, 1)


if __name__ == '__main__':
    unittest.main()