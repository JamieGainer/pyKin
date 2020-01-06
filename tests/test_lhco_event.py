import unittest

from pykin.lhco import LHCOEvent


class TestLHCOEvent(unittest.TestCase):

    # tests
    def test_create_event_and_set_event_number(self):
        new_event = LHCOEvent(event_number=1)
        self.assertEqual(new_event.event_number, 1)

    def test_create_event_and_set_trigger_word(self):
        new_event = LHCOEvent(trigger_word=1)
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
        type_number = 0
        answer_list, event, the_answer_list = self._obtain_event_the_answer_list_and_answer_list(type_number)
        answer_list += [event.photons[0].eta, event.photons[0].pt, event.photons[0].phi]
        self.assertListEqual(answer_list, the_answer_list)

    def test_create_event_with_electron_from_strings(self):
        type_number = 1
        answer_list, event, the_answer_list = self._obtain_event_the_answer_list_and_answer_list(type_number)
        answer_list += [event.electrons[0].eta, event.electrons[0].pt, event.electrons[0].phi]
        self.assertListEqual(answer_list, the_answer_list)

    def test_create_event_with_muon_from_strings(self):
        type_number = 2
        answer_list, event, the_answer_list = self._obtain_event_the_answer_list_and_answer_list(type_number)
        answer_list += [event.muons[0].eta, event.muons[0].pt, event.muons[0].phi]
        self.assertListEqual(answer_list, the_answer_list)

    def test_create_event_with_tau_from_strings(self):
        type_number = 3
        answer_list, event, the_answer_list = self._obtain_event_the_answer_list_and_answer_list(type_number)
        answer_list += [event.taus[0].eta, event.taus[0].pt, event.taus[0].phi]
        self.assertListEqual(answer_list, the_answer_list)

    def test_create_event_with_jet_from_strings(self):
        type_number = 4
        answer_list, event, the_answer_list = self._obtain_event_the_answer_list_and_answer_list(type_number)
        answer_list += [event.jets[0].eta, event.jets[0].pt, event.jets[0].phi]
        self.assertListEqual(answer_list, the_answer_list)

    def test_create_event_with_stable_charged_particle_from_strings(self):
        type_number = 5
        answer_list, event, the_answer_list = self._obtain_event_the_answer_list_and_answer_list(type_number)
        answer_list += [event.stable_charged_particles[0].eta, event.stable_charged_particles[0].pt,
                        event.stable_charged_particles[0].phi]
        self.assertListEqual(answer_list, the_answer_list)

    def test_create_event_with_missing_energy_from_strings(self):
        type_number = 6
        answer_list, event, the_answer_list = self._obtain_event_the_answer_list_and_answer_list(type_number)
        answer_list += [event.missing_energy.eta, event.missing_energy.pt,
                        event.missing_energy.phi]
        the_answer_list[8] = event.missing_energy
        self.assertListEqual(answer_list, the_answer_list)

    def test_create_event_with_two_photons_from_strings(self):
        type_number = 0
        answer_list, event, the_answer_list = self._obtain_event_the_answer_list_and_answer_list(type_number)
        answer_list += [event.photons[0].eta, event.photons[0].pt, event.photons[0].phi]
        second_photon_string = " 2    0   -1.729  1.557   687.76 592.46  37.0   0.0     4.41   0.0   0.0"
        event.add_physics_object_from_string(second_photon_string)
        answer_list += [event.photons[1].eta, event.photons[1].pt, event.photons[1].phi]
        the_answer_list += [-1.729, 687.76, 1.557]
        self.assertListEqual(answer_list, the_answer_list)

    def test_create_event_with_a_photon_and_a_jet_from_strings(self):
        type_number = 0
        answer_list, event, the_answer_list = self._obtain_event_the_answer_list_and_answer_list(type_number)
        answer_list += [event.photons[0].eta, event.photons[0].pt, event.photons[0].phi]
        second_photon_string = " 2    4   -1.729  1.557   687.76 592.46  37.0   0.0     4.41   0.0   0.0"
        event.add_physics_object_from_string(second_photon_string)
        answer_list += [event.jets[0].eta, event.jets[0].pt, event.jets[0].phi]
        the_answer_list += [-1.729, 687.76, 1.557]
        self.assertListEqual(answer_list, the_answer_list)

    def _obtain_event_the_answer_list_and_answer_list(self, type_number):
        event = self._initialize_event(type_number)
        the_answer_list = self._obtain_answer_list(type_number)
        answer_list = self._make_answer_list(event)
        return answer_list, event, the_answer_list

    def _make_answer_list(self, event):
        event_info_list = [event.event_number, event.trigger_word]
        answer_list = event_info_list + [len(event.photons), len(event.electrons),
                                         len(event.muons), len(event.taus), len(event.jets),
                                         len(event.stable_charged_particles)]
        return answer_list + [event.missing_energy]

    def _initialize_event(self, type_number):
        init_string = "   0           103   2563  \n"
        object_string = ("   1    " +
                         "{0}   -1.219  4.739   449.95   0.11   1.0   0.0    12.15   0.0   0.0\n".format(type_number))
        event = LHCOEvent.init_from_string(init_string)
        event.add_physics_object_from_string(object_string)
        return event

    def _obtain_answer_list(self, type_number):
        return [103, 2563] + [1 if i == type_number else 0 for i in range(6)] + [None, -1.219, 449.95, 4.739]

    # helper methods
    def make_basic_string_with_event_number_and_trigger_word(self, event_number, trigger_word):
        return "  0             {0}   {1} ".format(event_number, trigger_word)

    def assert_assertion_error_raised_by_string(self, init_string):
        with self.assertRaises(AssertionError):
            new_event = LHCOEvent.init_from_string(init_string)

    def verify_init_event_from_valid_string(self, init_string, event_number, trigger_word):
        new_event = LHCOEvent.init_from_string(init_string)
        self.assertListEqual([new_event.event_number, new_event.trigger_word], [event_number, trigger_word])

if __name__ == '__main__':
    unittest.main()