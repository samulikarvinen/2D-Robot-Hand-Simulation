import sys
from math import *
from robot import Robot
from robot_graphics_item import RobotGraphicsItem
from square import Square
from square_graphics_item import SquareGraphicsItem
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        # setting up the window
        self.setWindowTitle("Robot hand 9000")
        self.setFixedSize(QSize(1080, 720))

        # setting up the objects
        link1 = 150
        link2 = 150
        radius = link1 + link2
        square_width = 50
        square_height = 50

        self.robot = Robot(link1, link2)  # lengths of the links
        self.square = Square(square_width, square_height, radius)  # add size

        # setting up the docks
        self.set_manualdock()
        self.set_autodock()
        self.set_suctiondock()

        # setting up the graphics
        self.set_graphics()

    '''---------------------------------------------------------------------'''
    '''Setting up the manual dock with its buttons and their functionalities'''
    def set_manualdock(self):
        manualDock = QDockWidget()
        manualDock.setWindowTitle("Manual Control")
        # making the dock static and adding it to the left side
        manualDock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(Qt.LeftDockWidgetArea, manualDock)

        # adding Widget for the dock
        manualWidget = QWidget(self)
        manualDock.setWidget(manualWidget)

        # building layout
        grid = QGridLayout()

        # adding first label and slider for the layout
        label_first_slider = QLabel("1. joint \u03B8\u2081:")
        grid.addWidget(label_first_slider, 0, 0)
        self.label_first_theta = QLabel("{:.2f}\u00B0".format(0))
        grid.addWidget(self.label_first_theta, 0, 1)

        self.first_slider = QSlider(Qt.Horizontal)
        self.first_slider.setRange(0, 36000)  # 360 000 in order to have 0.01 increments from 0 to 360 degrees
        self.first_slider.setTickPosition(QSlider.TicksAbove)
        self.first_slider.setTickInterval(3600)
        grid.addWidget(self.first_slider, 1, 0, 1, 2)
        self.first_slider.valueChanged.connect(self.first_slider_value_changed)

        # adding second label and slider for the layout
        label_second_slider = QLabel("2. joint \u03B8\u2082:")
        grid.addWidget(label_second_slider, 2, 0)
        self.label_second_theta = QLabel("{:.2f}\u00B0".format(0))
        grid.addWidget(self.label_second_theta, 2, 1)

        self.second_slider = QSlider(Qt.Horizontal)
        self.second_slider.setRange(0, 36000)  # 360 000 in order to have 0.01 increments from 0 to 360 degrees
        self.second_slider.setTickPosition(QSlider.TicksAbove)
        self.second_slider.setTickInterval(3600)
        grid.addWidget(self.second_slider, 3, 0, 1, 2)
        self.second_slider.valueChanged.connect(self.second_slider_value_changed)

        # insert layout into the manual widget
        manualWidget.setLayout(grid)

    def first_slider_value_changed(self):
        theta1 = self.first_slider.value()*0.01  # from increments to degrees
        self.label_first_theta.setText("{:.2f}\u00B0".format(theta1))
        self.robot.move_with_angles(self.robot_graphics, self.square, self.square_graphics, theta1, self.robot.theta2)

    def second_slider_value_changed(self):
        theta2 = self.second_slider.value()*0.01  # from increments to degrees
        self.label_second_theta.setText("{:.2f}\u00B0".format(theta2))
        self.robot.move_with_angles(self.robot_graphics, self.square, self.square_graphics, self.robot.theta1, theta2)

    '''--------------------------------------------------------------'''
    '''Setting up the auto dock its buttons and their functionalities'''
    def set_autodock(self):
        autoDock = QDockWidget()
        autoDock.setWindowTitle("Auto Control")
        # making the dock static and adding it to the left side
        autoDock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(Qt.LeftDockWidgetArea, autoDock)

        # adding Widget
        autoWidget = QWidget(self)
        autoDock.setWidget(autoWidget)

        # build layout
        grid = QGridLayout()

        # adding the instructions label
        label_instruction = QLabel("Give the destination\ncoordinates from origin.")
        label_instruction.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        grid.addWidget(label_instruction, 0, 0, 1, 2)

        # adding the x coordinate sections
        label_x_line = QLabel("x:")
        grid.addWidget(label_x_line, 1, 0)
        self.x_line = QLineEdit('0')
        self.x_line.setValidator(QIntValidator())
        grid.addWidget(self.x_line, 1, 1)

        # adding the y coordinate sections
        label_y_line = QLabel("y:")
        grid.addWidget(label_y_line, 2, 0)
        self.y_line = QLineEdit('0')
        self.y_line.setValidator(QIntValidator())
        grid.addWidget(self.y_line, 2, 1)

        '''adding the move button section'''
        # label
        self.label_reach = QLabel("Out of reach!")
        self.label_reach.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        self.label_reach.hide()
        grid.addWidget(self.label_reach, 3, 0, 1, 2)

        # button
        move_button = QPushButton("Move")
        grid.addWidget(move_button, 4, 0, 1, 2)
        move_button.pressed.connect(self.move_button_pressed)

        # insert layout into the auto widget
        autoWidget.setLayout(grid)

    def move_button_pressed(self):
        # checking if the lines have numbers in them
        if self.x_line.text() and self.y_line.text():
            x = int(self.x_line.text())
            y = int(self.y_line.text())
            if sqrt(x**2 + y**2) <= (self.robot.len1 + self.robot.len2):
                self.label_reach.hide()
            # TODO: add info to robot which updates the graphics
            else:
                self.label_reach.show()

    '''-----------------------------------------------------------------'''
    '''Setting up the suction dock its buttons and their functionalities'''
    def set_suctiondock(self):
        suctionDock = QDockWidget()
        suctionDock.setWindowTitle("Suction")
        # making the dock static and adding it to the left side
        suctionDock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(Qt.LeftDockWidgetArea, suctionDock)

        # setting widget to the dock
        suctionWidget = QWidget(self)
        suctionDock.setWidget(suctionWidget)

        # building layout
        grid = QGridLayout()

        # adding button into layout
        self.suction_button = QPushButton("Suck")
        self.suction_button.setCheckable(True)
        grid.addWidget(self.suction_button)
        self.suction_button.pressed.connect(self.suction_button_pressed)

        # adding layout into widget
        suctionWidget.setLayout(grid)

    def suction_button_pressed(self):
        # Checking if the button is already pressed
        if self.suction_button.isChecked():
            self.robot.suction = False
            self.suction_button.setStyleSheet("background-color: rgb(225,225,225)")  # Neutral color
        else:
            # checking if the end-effector of the robot arm is touching the square item
            if self.robot_graphics.endeff.collidesWithItem(self.square_graphics):
                self.robot.suction = True
                # the difference between the robot hand and the square angles, in order to keep the rotation natural.
                self.square.rotation_difference = self.square.rotation - (self.robot.theta1 + self.robot.theta2)
                self.suction_button.setStyleSheet("background-color: green")  # Green color = success
            else:
                self.suction_button.setStyleSheet("background-color: rgb(171,46,70)")  # Red color = failure

    '''-------------------------------------------------------------------------'''
    '''setting up the central widget as graphics view, scene and add graphic items'''
    def set_graphics(self):
        # setting up the central widget as graphics view
        self.graphicsview = QGraphicsView()
        self.setCentralWidget(self.graphicsview)

        # setting up the graphical items
        self.square_graphics = SquareGraphicsItem(self.square)
        self.robot_graphics = RobotGraphicsItem(self.robot)

        # setting up the scene and add items
        self.scene = QGraphicsScene()
        self.scene.addItem(self.square_graphics)
        self.scene.addItem(self.robot_graphics)

        # setting the scene to the view
        self.graphicsview.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
