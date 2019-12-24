import four_vector

class PhysicsObject():

    def __init__(self, **kwargs):
        self._set_attribute_lists_and_dicts()
        self._set_attributes_from_kwargs(kwargs)
        self._set_attributes_from_four_vector()

    def __getattr__(self, attribute):
        if attribute in self.attributes_to_rename:
            return getattr(self, self.attributes_to_rename[attribute])
        else:
            return self._find_and_get_similarly_named_attribute_or_raise_value_error(attribute)

    # method(s) in __init__
    def _set_attribute_lists_and_dicts(self):
        self.lhco_order_of_fields = ["object_number", "type", "eta", "phi", "pt", "mass", "n_tracks", "btag",
                                     "had_em", "dummy1", "dummy2"]
        self.other_valid_fields = ['energy', 'px', 'py', 'pz', 'p', 'theta']
        self.possible_attributes = self.lhco_order_of_fields + self.other_valid_fields
        self.attributes_to_rename = {'jmass': 'mass', 'ntrk': 'n_tracks', 'e': 'energy', 'momentum': 'p'}
        self.set_attributes = []

    def _set_attributes_from_kwargs(self, kwargs):
        for attribute in kwargs:
            self._set_attribute(attribute, kwargs)

    def _set_attributes_from_four_vector(self):
        try:
            vector = four_vector.FourVector.from_eta_phi_pt_M(self.eta, self.phi, self.pt, self.mass)
        except AttributeError:
            try:
                vector = four_vector.FourVector.from_eta_phi_pt_M(self.eta, self.phi, self.pt, 0.)
            except:
                return
        ### need to generalize this
        self.energy = vector.E
        self.p = vector.p
        self.theta = vector.theta

    # method(s) in _set_attributes
    def _set_attribute(self, attribute, kwargs):
        if attribute in self.possible_attributes:
            self._set_possible_attribute(attribute, kwargs)
        elif attribute in self.attributes_to_rename:
            self._find_correct_name_and_set_attribute(attribute, kwargs)
        else:
            self._find_and_set_similarly_named_attribute_or_raise_value_error(attribute, kwargs)

    # method(s) in _set_attribute
    def _set_possible_attribute(self, attribute, kwargs):
        setattr(self, attribute, kwargs[attribute])
        self.set_attributes.append(attribute)

    def _find_correct_name_and_set_attribute(self, attribute, kwargs):
        correct_name = self.attributes_to_rename[attribute]
        setattr(self, correct_name, kwargs[attribute])
        self.set_attributes.append(correct_name)

    def _find_and_set_similarly_named_attribute_or_raise_value_error(self, attribute, kwargs):
        possible_attribute = self._find_similarly_named_attribute_or_raise_value_error(attribute)
        setattr(self, possible_attribute, kwargs[attribute])
        self.set_attributes.append(possible_attribute)

    # method(s) in _find_and_set_similarly_named_attribute_or_raise_value_error
    def _find_similarly_named_attribute_or_raise_value_error(self, attribute):
        stripped_attribute = self._strip_hyphens_slashes_and_underscores(attribute)
        for possible_attribute in self.possible_attributes:
            stripped_possible_attribute = self._strip_hyphens_slashes_and_underscores(possible_attribute)
            if stripped_attribute == stripped_possible_attribute:
                self.attributes_to_rename[attribute] = possible_attribute
                return possible_attribute
        else:
            raise ValueError(attribute + ' is not a valid attribute of PhysicsObject.')

    # method(s) in _find_similarly_named_attribute_or_raise_value_error
    def _strip_hyphens_slashes_and_underscores(self, string):
        for char in ['-', '/', '\'', '_']:
            string = string.replace(char, '')
        return string.lower()

    # method(s) in __getattr__
    def _find_and_get_similarly_named_attribute_or_raise_value_error(self, attribute):
        try:
            possible_attribute = self._find_similarly_named_attribute_or_raise_value_error(attribute)
            if possible_attribute in self.set_attributes:
                return getattr(self, possible_attribute)
            else:
                raise AttributeError(attribute + " (or " + possible_attribute + ') is not set')
        except ValueError:
            raise AttributeError(attribute + ' is not a valid attribute of PhysicsObject.')
