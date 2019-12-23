import unittest
import lhco_event

class TestLHCOEvent(unittest.TestCase):

    def test_create_event(self):
        new_event = lhco_event.LHCOEvent()


if __name__ == '__main__':
    unittest.main()