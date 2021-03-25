from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class SquareGraphicsItem(QGraphicsRectItem):
    def __init__(self, square):
        super(SquareGraphicsItem, self).__init__()
        self.square = square
        self.setRect(0, 0, self.square.width, self.square.height)
        self.setPos(self.square.location[0]-self.square.width/2, self.square.location[1]-self.square.height/2)
        self.setBrush(QBrush(QGradient(QGradient.JuicyCake)))

    def update_position(self):
        self.setPos(self.square.location[0]-self.square.width/2, self.square.location[1]-self.square.height/2)
