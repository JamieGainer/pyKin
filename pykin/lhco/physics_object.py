import logging

from pykin.core import FourVector

logger = logging.getLogger()
lhco_order_of_fields = ["object_number", "type", "eta", "phi", "pt", "mass", "n_tracks", "btag",
                        "had_em", "dummy1", "dummy2"]

class PhysicsObject():

    def __init__(self, **kwargs):
        self._set_attribute_lists_and_dicts()
        self._set_attributes_from_kwargs(kwargs)

    def __getattr__(self, attribute):
        if attribute.lower() in self.attributes_to_rename:
            return getattr(self, self.attributes_to_rename[attribute.lower()])
        else:
            return self._find_and_get_similarly_named_attribute_or_raise_value_error(attribute.lower())

    @classmethod
    def set_from_string(cls, string):
        fields = string.split()
        cls._check_for_invalid_fields(fields)
        kwargs = cls._make_physics_object_kwargs(fields)
        return PhysicsObject(**kwargs)

    def set_attributes_from_four_vector(self):
        vector = FourVector.from_eta_phi_pt_M(self.eta, self.phi, self.pt, self.mass)
        for field in ['p', 'theta']:
            setattr(self, field, getattr(vector, field))
        field_names = {'px': 'p_x', 'py': 'p_y', 'pz': 'p_z', 'energy': 'E'}
        for object_field_name, vector_field_name in field_names.items():
            setattr(self, object_field_name, getattr(vector, vector_field_name))

    # method(s) in __init__
    def _set_attribute_lists_and_dicts(self):
        self.other_valid_fields = ['energy', 'px', 'py', 'pz', 'p', 'theta']
        self.possible_attributes = lhco_order_of_fields + self.other_valid_fields
        self.attributes_to_rename = {'jmass': 'mass', 'ntrk': 'n_tracks', 'e': 'energy', 'momentum': 'p',
                                     'm': 'mass'}
        self.set_attributes = []

    def _set_attributes_from_kwargs(self, kwargs):
        for attribute in kwargs:
            self._set_attribute(attribute, kwargs)

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

    # methods in set_from_string
    @classmethod
    def _check_for_invalid_fields(cls, fields):
        assert len(fields) == len(lhco_order_of_fields)
        assert "".join(fields).replace('.', '').replace('-', '').isdigit()

    @classmethod
    def _make_physics_object_kwargs(cls, fields):
        values = [float(field) if "." in field else int(field) for field in fields]
        kwargs = {attr: value for attr, value in zip(lhco_order_of_fields, values)}
        return kwargs
