import unittest

import numpy as np

from pykin.lhco import lhco_event_list


class TestLHCOEventList(unittest.TestCase):

    # tests
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

    def test_missing_energy_eta_lhco_event_list_from_file(self):
        self.assertListEqual([x.missing_energy.eta for x in self.event_list.list], [0., 0., 0.])

    def test_missing_energy_phi_lhco_event_list_from_file(self):
        self.assertListEqual([x.missing_energy.phi for x in self.event_list.list], [4.857, 1.926, 2.612])

    def test_missing_energy_pt_lhco_event_list_from_file(self):
        self.assertListEqual([x.missing_energy.pt for x in self.event_list.list], [275.16, 12.42, 11.76])

    def test_missing_energy_E_lhco_event_list_from_file(self):
        self.assertListAlmostEqual([x.missing_energy.E for x in self.event_list.list], [275.16, 12.42, 11.76])

    def test_missing_energy_p_lhco_event_list_from_file(self):
        self.assertListAlmostEqual([x.missing_energy.p for x in self.event_list.list], [275.16, 12.42, 11.76])

    def test_missing_energy_px_lhco_event_list_from_file(self):
        self.assertListAlmostEqual([x.missing_energy.pt * np.cos(x.missing_energy.phi) for x in self.event_list.list],
                                   [x.missing_energy.px for x in self.event_list.list])

    def test_second_jet_eta_lhco_event_list_from_file(self):
        self.assertListEqual([x.jets[1].eta for x in self.event_list.list], [-0.829, 1.207, -0.036])

    def test_second_jet_phi_lhco_event_list_from_file(self):
        self.assertListEqual([x.jets[1].phi for x in self.event_list.list], [2.540, 4.216, 1.763])

    def test_second_jet_pt_lhco_event_list_from_file(self):
        self.assertListEqual([x.jets[1].pt for x in self.event_list.list], [67.26, 306.56, 13.38])

    def test_second_jet_p_lhco_event_list_from_file(self):
        self.assertListAlmostEqual([x.jets[1].p for x in self.event_list.list],
                                   [x.jets[1].pt * np.cosh(x.jets[1].eta) for x in self.event_list.list])

    def test_second_jet_E_lhco_event_list_from_file(self):
        self.assertListAlmostEqual([x.jets[1].E for x in self.event_list.list],
                                   [np.sqrt(x.jets[1].p**2 + x.jets[1].M**2) for x in self.event_list.list])

    def test_second_jet_px_lhco_event_list_from_file(self):
        self.assertListAlmostEqual([x.jets[1].pt * np.cos(x.jets[1].phi) for x in self.event_list.list],
                                   [x.jets[1].px for x in self.event_list.list])

    # helper methods
    event_list = lhco_event_list.LHCOEventList.from_file('demo.lhco')

    def assertListAlmostEqual(self, list_1, list_2):
        self.assertEqual(len(list_1), len(list_2))
        for a, b in zip(list_1, list_2):
            self.assertAlmostEqual(a, b)

if __name__ == '__main__':
    unittest.main()