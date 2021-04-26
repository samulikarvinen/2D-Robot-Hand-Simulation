from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np


class TextGraphicsItem(QGraphicsItemGroup):
    def __init__(self, robot, square):
        super(TextGraphicsItem, self).__init__()
        self.robot = robot
        self.square = square

        # add the coordinate of the end-effector as a text item
        text = "(" + str(round(self.robot.coord2[0])) + ", " + str(round(self.robot.coord2[1])) + ")"
        self.endeff_text = QGraphicsSimpleTextItem(text)
        self.endeff_text.setBrush(QBrush(QColor("cyan")))
        self.endeff_text.setPos(self.robot.coord2[0], self.robot.coord2[1])
        self.addToGroup(self.endeff_text)

        # add the coordinate of the square as a text item
        text = "(" + str(round(self.square.location[0])) + ", " + str(round(self.square.location[1])) + ")"
        self.square_text = QGraphicsSimpleTextItem(text)
        self.square_text.setBrush(QBrush(QColor("red")))
        self.square_text.setPos(self.square.location[0], self.square.location[1])
        self.addToGroup(self.square_text)

    def update_text(self):
        # update the coordinate text of the end-effector
        self.endeff_text.setText("(" + str(round(self.robot.coord2[0])) + ", " + str(round(self.robot.coord2[1])) + ")")
        self.endeff_text.setPos(self.robot.coord2[0], self.robot.coord2[1])

        # update the coordinate text of the square
        self.square_text.setText("(" + str(round(self.square.location[0])) + ", "
                                 + str(round(self.square.location[1])) + ")")
        self.square_text.setPos(self.square.location[0], self.square.location[1])

