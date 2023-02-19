

class Canvas:
    def __init__(self, **kwargs):
        self._resolution = kwargs['resolution']
        self._drops = []
        self._simulation_time = kwargs['max_simulation_time']
        self._fps = kwargs['fps']

    # Add a new drop to the existing canvas
    def add_new_drop(self, drop):
        self._drops.append(drop)

    # Simulate ripples due to water drops
    def ripple(self):
        pass

    # Convert the simulated ripples to an array of raster images according to target fps
    def convert_simulation_to_image(self):
        pass