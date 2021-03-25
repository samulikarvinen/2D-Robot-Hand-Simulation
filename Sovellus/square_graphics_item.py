from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class SquareGraphicsItem(QGraphicsRectItem):
    def __init__(self, square):
        super(SquareGraphicsItem, self).__init__()
        self.square = square
        self.setRect(self.square.location[0], self.square.location[1], self.square.width, self.square.height)
        self.setBrush(QBrush(QColor(0, 255, 0)))
        # todo: add information from the square class so that the square can be drawn to the scene


    def update_position(self):
        # todo: update position, which is changed if the suction is on.
        pass
