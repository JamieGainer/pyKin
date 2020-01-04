import logging

import lhco_event

logger = logging.getLogger()

class LHCOEventList():

    def __init__(self, list_of_events):
        self.list = list_of_events

    @classmethod
    def from_file(cls, file_name):
        list_of_events = []
        with open(file_name, 'r') as event_file:
            for line in event_file:
                try:
                    list_of_events.append(lhco_event.LHCOEvent.init_from_string(line))
                except:
                    try:
                        list_of_events[-1].add_physics_object_from_string(line, add_four_vector_attributes=True)
                    except:
                        if line.strip() != '':
                            logger.warning('Line: ' + line + " ignored.")
        return LHCOEventList(list_of_events)