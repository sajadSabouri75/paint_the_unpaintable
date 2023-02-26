

class Ripple:
    def __init__(self, **kwargs):
        self._coordinates = kwargs['coordinates']
        self._time = kwargs['time']
        self._velocity = kwargs['velocity']

    def move_one_step(self, ):
