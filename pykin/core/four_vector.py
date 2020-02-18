import logging

import numpy as np

logger = logging.getLogger()

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

    # helper method(s) for __init__
    def _set_values(self, E, p_x, p_y, p_z, phi_range, theta_range):
        self.E, self.p_x, self.p_y, self.p_z = E, p_x, p_y, p_z
        self.phi_range, self.theta_range = phi_range, theta_range

    def _set_p_pt_and_M(self):
        self.p_T = np.sqrt(self.p_x**2 + self.p_y**2)
        self.p = np.sqrt(self.p_T**2 + self.p_z**2)
        self._set_M()

    def _obtain_phi(self):
        self.phi = np.arctan2(self.p_y, self.p_x)
        if not self._in(self.phi, self.phi_range):
            self.phi -= np.floor(self.phi / (2 * np.pi)) * 2 * np.pi

    def _obtain_theta_and_eta(self):
        self.theta = np.arctan2(self.p_T, self.p_z)
        self.eta = -np.log(np.tan(self.theta / 2))

    # helper method(s) for _set_p_pt_and_M
    def _set_M(self):
        M_squared = self.E**2 - self.p**2
        if M_squared < 0.:
            logger.warning("Mass squared less than 0, setting mass to 0 when E = " +
                           str(self.E) + ', p = ' + str(self.p) + '.')
            self.M = 0.
        else:
            self.M = np.sqrt(M_squared)

    def _in(self, value, range):
        if value < range[0] or value > range[1]:
            return False
        return True