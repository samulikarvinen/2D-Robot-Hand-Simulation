from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np


class SquareGraphicsItem(QGraphicsRectItem):
    def __init__(self, square):
        # Initializing a square which some nice color
        super(SquareGraphicsItem, self).__init__()
        self.square = square
        self.setRect(0, 0, self.square.width, self.square.height)
        self.setPos(self.square.location[0]-self.square.width/2, self.square.location[1]-self.square.height/2)
        self.setBrush(QBrush(QGradient(QGradient.JuicyCake)))
        self.setRotation(self.square.rotation)

        # add the coordinate of the square as a text item
        text = "(" + str(round(self.square.location[0])) + ", " + str(round(self.square.location[1])) + ")"
        self.square_text = QGraphicsSimpleTextItem(text, self)
        self.square_text.setBrush(QBrush(QColor("red")))

    def update_pose(self):
        # update based on the new values
        self.setPos(self.square.location[0]-self.square.width/2, self.square.location[1]-self.square.height/2)
        self.setTransformOriginPoint(self.square.width/2, self.square.height/2)
        self.setRotation(self.square.rotation)

        # update the coordinate text
        self.square_text.setText("(" + str(round(self.square.location[0])) + ", " + str(round(self.square.location[1])) + ")")
