import copy

_attributes_from_types = {0: 'photons', 1: 'electrons', 2: 'muons', 3: 'taus',
                         4: 'jets', 5: 'stable_charged_particles', 6: 'missing_energy'}

_types_from_attributes = {attribute: type for type, attribute in _attributes_from_types.items()}

class SimpleEventFilter()

    def __init__(self, event, object_type, filter_value):
        self.event, self.object_type, self.filter_value = event, object_type, filter_value
        self._return_attribute_or_raise_value_error()
        self._make_filtered_object_list()
        self._make_new_event()

    def filter(self):
        return self.new_event

    def _return_attribute_or_raise_value_error(self):
        if self.object_type in _attributes_from_types and self.object_type != 6:
            return _attributes_from_types[self.object_type]
        if self.object_type in _types_from_attributes and self.object_type != 'missing_energy':
            return self.object_type
        raise ValueError('Applying pt cut to invalid object type: ' + self.object_type)

    def _make_filtered_object_list(self):
        raise NotImplementedError

    def _make_new_event(self):
        self.new_event = copy.deepcopy(self.event)
        setattr(self.new_event, self.attribute, self.filtered_object_list)


class PT_Filter(SimpleEventFilter):

    def _make_filtered_object_list(self):
        return [x for x in getattr(self.event, self.attribute) if x.pt > self.filter_value]

class EtaFilter(SimpleEventFilter):

    def _make_filtered_object_list(self):
        return [x for x in getattr(self.event, self.attribute) if abs(x.eta) < self.filter_value]

def apply_pt_min_cut_for_object(event, object_type, pt_min): # -> event
    return PT_Filter(event, object_type, pt_min).filter()

def apply_abs_eta_cut_for_object(event, object_type, eta_max): # -> event
    return EtaFilter(event, object_type, eta_max).filter()



def apply_isolation_of_type_A_from_type_B(event, type_A, type_B, pt_min_type_B = 0,
                                          eta_max_type_B = float("inf"), delta_R_cut): # -> event
    pass

def prune_non_isolated_lower_pT_objects_of_type_A(event, type_A, delta_R_cut): # -> event
    pass