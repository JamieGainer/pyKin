import unittest

import lhco_event_list

class TestLHCOEventList(unittest.TestCase):

    def test_lhco_event_list_from_file(self):
        event_list = lhco_event_list.LHCOEventList.from_file('demo.lhco')
        self.assertEqual(len(event_list.list), 3)

if __name__ == '__main__':
    unittest.main()