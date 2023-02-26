from classes.ripple import Ripple


class Controller:
    def __init__(self, **kwargs):
        self._max_simulation_time = kwargs['max_simulation_time']
        self._canvas = kwargs['canvas']
        self._ripple_velocity = kwargs['ripple_velocity']
        self._ripples = []

    def add_ripple(self, new_coordinates, relative_time):
        self._ripples.append(
            Ripple(
                coordinates=new_coordinates,
                time=relative_time,
                velocity=self._ripple_velocity
            )
        )

    def simulate(self):
        for time_index in range(self._max_simulation_time):
            for ripple in self._ripples:
                ripple.move_one_step()
