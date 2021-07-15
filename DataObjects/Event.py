from DataObjects.NamedDataObject import NamedDataObject


class Event(NamedDataObject):
    def __init__(self, id, name='Event', parent_id=None):
        super().__init__(id, name)
        self.parent_id = parent_id

