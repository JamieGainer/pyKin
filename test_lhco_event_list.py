import unittest

import lhco_event_list

class TestLHCOEventList(unittest.TestCase):

    event_list = lhco_event_list.LHCOEventList.from_file('demo.lhco')

    def test_number_of_events_in_lhco_event_list_from_file(self):
        self.assertEqual(len(self.event_list.list), 3)

    def test_event_numbers_in_lhco_event_list_from_file(self):
        self.assertListEqual([x.event_number for x in self.event_list.list], [103, 5, 3])

    def test_trigger_words_in_lhco_event_list_from_file(self):
        self.assertListEqual([x.trigger_word for x in self.event_list.list], [2563, 3587, 3599])

    def test_num_photons_lhco_event_list_from_file(self):
        self.assertListEqual([len(x.photons) for x in self.event_list.list], [0, 0, 0])

    def test_num_electrons_lhco_event_list_from_file(self):
        self.assertListEqual([len(x.electrons) for x in self.event_list.list], [0, 0, 2])

    def test_num_muons_lhco_event_list_from_file(self):
        self.assertListEqual([len(x.muons) for x in self.event_list.list], [1, 1, 0])

    def test_num_taus_lhco_event_list_from_file(self):
        self.assertListEqual([len(x.taus) for x in self.event_list.list], [0, 0, 0])

    def test_num_jets_lhco_event_list_from_file(self):
        self.assertListEqual([len(x.jets) for x in self.event_list.list], [2, 6, 5])

    def test_num_stable_charged_particles_lhco_event_list_from_file(self):
        self.assertListEqual([len(x.stable_charged_particles) for x in self.event_list.list], [0, 0, 0])


if __name__ == '__main__':
    unittest.main()