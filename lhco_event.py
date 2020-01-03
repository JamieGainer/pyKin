class LHCOEvent():

    def __init__(self, event_number=None, trigger_word=None):
        self._set_event_properties(event_number, trigger_word)
        (self.photons, self.electrons, self.muons, self.taus, self.jets,
         self.stable_charged_particles) = [[] for _ in range(6)]

    def _set_event_properties(self, event_number, trigger_word):
        if event_number:
            self.event_number = event_number
        if trigger_word:
            self.trigger_word = trigger_word

    @classmethod
    def init_from_string(cls, string):
        fields = string.split()
        #assert len(fields) == 3
        #assert "".join(fields).isdigit()
        _, event_number, trigger_word = map(lambda x: int(x), fields)
        return LHCOEvent(event_number=event_number, trigger_word=trigger_word)