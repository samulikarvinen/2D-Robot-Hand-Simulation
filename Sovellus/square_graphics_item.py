from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class SquareGraphicsItem(QGraphicsRectItem):
    def __init__(self, square):
        # initializing a square which some nice color
        super(SquareGraphicsItem, self).__init__()
        self.square = square
        self.setRect(0, 0, self.square.width, self.square.height)
        self.setPos(self.square.location[0]-self.square.width/2, self.square.location[1]-self.square.height/2)
        self.setBrush(QBrush(QGradient(QGradient.JuicyCake)))
        self.setRotation(self.square.rotation)

    def update_pose(self):
        # update based on the new values
        self.setPos(self.square.location[0]-self.square.width/2, self.square.location[1]-self.square.height/2)
        self.setTransformOriginPoint(self.square.width/2, self.square.height/2)
        self.setRotation(self.square.rotation)
