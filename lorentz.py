import numpy as np

class FourVector():

    def __init__(self, E, p_x, p_y, p_z, phi_range=(0, 2 * np.pi), theta_range=(0, np.pi)):
        self._set_values(E, p_x, p_y, p_z, phi_range, theta_range)
        self._set_p_pt_and_M()
        self._obtain_phi()
        self._obtain_theta_and_eta()

    @classmethod
    def from_eta_phi_pt_M(cls, eta, phi, p_T, M, phi_range=(0, 2 * np.pi), theta_range=(0, np.pi)):
        p_x, p_y = [p_T * np.cos(phi), p_T * np.sin(phi)]
        theta = 2. * np.arctan(np.exp(-eta))
        p_z = p_T / np.tan(theta)
        E = np.sqrt(M**2 + p_T**2 + p_z**2)
        return FourVector(E, p_x, p_y, p_z, phi_range, theta_range)

    def _set_values(self, E, p_x, p_y, p_z, phi_range, theta_range):
        self.E, self.p_x, self.p_y, self.p_z = E, p_x, p_y, p_z
        self.phi_range, self.theta_range = phi_range, theta_range

    def _set_p_pt_and_M(self):
        self.p_T = np.sqrt(self.p_x**2 + self.p_y**2)
        self.p = np.sqrt(self.p_T**2 + self.p_z**2)
        self.M = np.sqrt(self.E**2 - self.p**2)

    def _obtain_phi(self):
        self.phi = np.arctan2(self.p_y, self.p_x)
        if not self._in(self.phi, self.phi_range):
            self.phi -= np.floor(self.phi / (2 * np.pi)) * 2 * np.pi

    def _obtain_theta_and_eta(self):
        self.theta = np.arctan2(self.p_T, self.p_z)
        self.eta = -np.log(np.tan(self.theta / 2))

    def _in(self, value, range):
        if value < range[0] or value > range[1]:
            return False
        return True

# No test coverage below this line

class LHCOEvent():

    def __init__(self, line_string):
        ints = [int(x) for x in line_string.split()]
        try:
            assert len(ints) == 3 and ints[0] == 0
        except AssertionError:
            raise ValueError("Not the first line of an event")
        self.event_number, self.trigger_word = ints[1:]
        self.object_dict = {object_type: [] for object_type in range(7)}

    def add_line(self, line_string):
        floats = [float(x) for x in line_string.split()]
        try:
            assert len(floats) == 11
        except AssertionError:
            raise ValueError("Not a valid physics object line")
        number, object_type, eta, phi, p_T, jet_mass, n_tracks, b_tag, had_em, dummy_1, dummy_2 = floats
        if object_type in [0, 1, 2]:
            mass = {0: 0., 1: 0.000511, 2: 0.105}[object_type]
        else:
            mass = jet_mass
        physics_object = FourVector.from_eta_phi_pt_M(eta, phi, p_T, mass)
        (physics_object.number, physics_object.n_tracks,
         physics_object.b_tag, physics_object.had_em,
         physics_object.dummy_1, physics_object.dummy_2) = number, n_tracks, b_tag, had_em, dummy_1, dummy_2
        self.object_dict[object_type].append(physics_object)

    def finish_event(self):
        for object_type, object_list in self.object_dict:
            object_list.sort(key=lambda x: x.p_T, reverse=True)

def lhco_event_list_from_file(file):
    events = []
    in_event = False
    for line in file:
        if in_event:
            try:
                events[-1].add_line(line)
            except ValueError:
                in_event = False
                try:
                    events.append(LHCOEvent(line))
                    in_event = True
                except ValueError:
                    continue
        else:
            try:
                events.append(LHCOEvent(line))
                in_event = True
            except ValueError:
                continue