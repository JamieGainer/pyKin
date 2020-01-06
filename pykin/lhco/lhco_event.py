import logging

from pykin.lhco.physics_object import PhysicsObject

logger = logging.getLogger()

attributes_from_types = {0: 'photons', 1: 'electrons', 2: 'muons', 3: 'taus',
                         4: 'jets', 5: 'stable_charged_particles', 6: 'missing_energy'}

class LHCOEvent():

    def __init__(self, event_number=None, trigger_word=None):
        self._set_event_properties(event_number, trigger_word)
        self._initialize_event_physics_objects()
        logger.debug('Initialized event with event number {0} and trigger word {1}.',
                     event_number, trigger_word)

    def add_physics_object(self, physics_object):
        attribute = attributes_from_types[physics_object.type]
        if attribute == 'missing_energy':
            self.missing_energy = physics_object
        else:
            getattr(self, attribute).append(physics_object)

    def add_physics_object_from_string(self, string, add_four_vector_attributes=False):
        object = PhysicsObject.set_from_string(string)
        if add_four_vector_attributes:
            object.set_attributes_from_four_vector()
        self.add_physics_object(object)

    @classmethod
    def init_from_string(cls, string):
        fields = string.split()
        cls._check_for_problems_with_fields(fields)
        _, event_number, trigger_word = map(int, fields)
        return LHCOEvent(event_number=event_number, trigger_word=trigger_word)

    # method(s) for __init__
    def _set_event_properties(self, event_number, trigger_word):
        if event_number:
            self.event_number = event_number
            logger.debug('Set event number to {0}.', event_number)
        if trigger_word:
            self.trigger_word = trigger_word
            logger.debug('Set trigger word to {0}.', trigger_word)

    def _initialize_event_physics_objects(self):
        (self.photons, self.electrons, self.muons, self.taus, self.jets,
         self.stable_charged_particles) = [[] for _ in range(6)]
        self.missing_energy = None

    # method(s) for init_from_string
    @classmethod
    def _check_for_problems_with_fields(cls, fields):
        assert len(fields) == 3
        assert "".join(fields).isdigit()

