from classes.canvas import Canvas
from classes.controller import Controller


if __name__ == '__main__':
    canvas = Canvas(
        size=(100, 100)
    )

    controller = Controller(
        canvas=canvas,
        max_simulation_time=100,
        ripple_velocity=1
    )

    controller.add_ripple(
        (1, 1), 0
    )

    controller.simulate()