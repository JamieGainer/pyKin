num_object_types = 7

class LHCOEvent():

    def __init__(self, event_number=None, trigger_word=None):
        self._set_event_properties(event_number, trigger_word)
        self.object_register = {i: [] for i in range(num_object_types)}

    def _set_event_properties(self, event_number, trigger_word):
        if event_number:
            self.event_number = event_number
        if trigger_word:
            self.trigger_word = trigger_word