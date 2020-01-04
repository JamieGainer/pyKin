import unittest

import lhco_event_list

class TestLHCOEventList(unittest.TestCase):

    event_list = lhco_event_list.LHCOEventList.from_file('demo.lhco')

    def test_number_of_events_in_lhco_event_list_from_file(self):
        self.assertEqual(len(self.event_list.list), 3)

    def test_event_numbers_in_lhco_event_list_from_file(self):
        self.assertListEqual([x.event_number for x in self.event_list.list], [103, 5, 3])


if __name__ == '__main__':
    unittest.main()