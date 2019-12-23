num_object_types = 7

class PhysicsObject():

    lhco_order_of_fields = ["object_number", "type", "eta", "phi", "pt", "mass", "n_tracks", "btag",
                            "had_em", "dummy1", "dummy2"]
    attributes_to_rename = {'jmass': 'mass', 'ntrk': 'n_tracks', 'e': 'energy'}

    def __init__(self, **kwargs):
        self.possible_attributes = set(self.lhco_order_of_fields)
        self.possible_attributes.update(['energy', 'px', 'py', 'pz'])
        for attribute in kwargs:
            if attribute in self.possible_attributes:
                setattr(self, attribute, kwargs[attribute])
            elif attribute in self.attributes_to_rename:
                correct_name = self.attributes_to_rename[attribute]
                setattr(self, correct_name, kwargs[attribute])




class LHCOEvent():

    def __init__(self, event_number=None, trigger_word=None):
        self._set_event_properties(event_number, trigger_word)
        self.object_register = {i: [] for i in range(num_object_types)}

    def _set_event_properties(self, event_number, trigger_word):
        if event_number:
            self.event_number = event_number
        if trigger_word:
            self.trigger_word = trigger_word