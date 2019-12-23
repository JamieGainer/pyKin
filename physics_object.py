class PhysicsObject():

    lhco_order_of_fields = ["object_number", "type", "eta", "phi", "pt", "mass", "n_tracks", "btag",
                            "had_em", "dummy1", "dummy2"]
    other_valid_fields = ['energy', 'px', 'py', 'pz', 'p', 'theta']
    attributes_to_rename = {'jmass': 'mass', 'ntrk': 'n_tracks', 'e': 'energy', 'momentum': 'p'}

    def __init__(self, **kwargs):
        self.possible_attributes = set(self.lhco_order_of_fields)
        self.possible_attributes.update(self.other_valid_fields)
        for attribute in kwargs:
            if attribute in self.possible_attributes:
                setattr(self, attribute, kwargs[attribute])
            elif attribute in self.attributes_to_rename:
                correct_name = self.attributes_to_rename[attribute]
                setattr(self, correct_name, kwargs[attribute])
            else:
                raise ValueError(attribute + ' is not a valid attribute of PhysicsObject.')