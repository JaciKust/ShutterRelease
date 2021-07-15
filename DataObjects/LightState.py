from DataObjects.NamedDataObject import NamedDataObject


class LightState(NamedDataObject):
    def __init__(self, id, state, pins=None, in_time=None):
        super().__init__(id, 'LightState')
        self.state = state
        self.in_time = in_time

