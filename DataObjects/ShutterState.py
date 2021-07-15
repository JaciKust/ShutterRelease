from DataObjects.NamedDataObject import NamedDataObject


class ShutterState(NamedDataObject):
    def __init__(self, id, state, in_time=None):
        super().__init__(id, 'ShutterState')
        self.state = state
        self.in_time = in_time

