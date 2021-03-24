from PyQt5.QtWidgets import *


class SquareGraphicsItem(QGraphicsItem):
    def __init__(self, square):
        super(SquareGraphicsItem, self).__init__()
        self.square = square
        # todo: add information from the square class so that the square can be drawn to the scene
        pass

    def update_position(self):
        # todo: update position, which is changed if the suction is on.
        pass
