from DataObjects.NamedDataObject import NamedDataObject


class LightState(NamedDataObject):
    def __init__(self, id, state):
        super().__init__('LightState')
        self.id = id
        self.state = state

