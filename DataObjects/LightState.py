from DataObjects.NamedDataObject import NamedDataObject


class LightState(NamedDataObject):
    def __init__(self, state, pins=None, in_time=None):
        super().__init__(1, 'LightState')
        self.state = state
        self.in_time = in_time

