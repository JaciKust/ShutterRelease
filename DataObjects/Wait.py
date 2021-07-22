from DataObjects.NamedDataObject import NamedDataObject


class WaitDataObject(NamedDataObject):
    def __init__(self, time):
        super().__init__('Wait')
        self.time = time
