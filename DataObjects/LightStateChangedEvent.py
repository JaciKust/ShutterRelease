from DataObjects.Event import Event


class LightStateChangedEVent(Event):
    def __init__(self, id, new_state, parent_id=None, in_time=None):
        super().__init__(id, "LightStateChangedEvent", parent_id)
        self.new_state = new_state
        self.in_time = in_time
