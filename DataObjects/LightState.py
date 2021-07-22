from DataObjects.NamedDataObject import NamedDataObject


class LightState(NamedDataObject):
    def __init__(self, state):
        super().__init__('LightState')
        self.state = state

