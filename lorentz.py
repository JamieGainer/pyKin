import numpy as np

class FourVector():

    def __init__(self, E, p_x, p_y, p_z):
        self.E, self.p_x, self.p_y, self.p_z = E, p_x, p_y, p_z
        self.p_T = np.sqrt(self.p_x**2 + self.p_y**2)
        self.p = np.sqrt(self.p_T**2 + self.p_z**2)
        self.M = np.sqrt(self.E**2 - self.p**2)
        self.phi = np.arctan2(self.p_y, self.p_x)
        #self.theta =
        #self.eta =
        #self.phi =
