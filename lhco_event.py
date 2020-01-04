import logging

logger = logging.getLogger()

class LHCOEvent():

    def __init__(self, event_number=None, trigger_word=None):
        self._set_event_properties(event_number, trigger_word)
        (self.photons, self.electrons, self.muons, self.taus, self.jets,
         self.stable_charged_particles) = [[] for _ in range(6)]
        logger.debug('Initialized event with event number {0} and trigger word {1}.',
                     event_number, trigger_word)

    def _set_event_properties(self, event_number, trigger_word):
        if event_number:
            self.event_number = event_number
            logger.debug('Set event number to {0}.', event_number)
        if trigger_word:
            self.trigger_word = trigger_word
            logger.debug('Set trigger word to {0}.', trigger_word)

    @classmethod
    def init_from_string(cls, string):
        fields = string.split()
        cls._check_for_problems_with_fields(fields)
        _, event_number, trigger_word = map(int, fields)
        return LHCOEvent(event_number=event_number, trigger_word=trigger_word)

    @classmethod
    def _check_for_problems_with_fields(cls, fields):
        assert len(fields) == 3
        assert "".join(fields).isdigit()

