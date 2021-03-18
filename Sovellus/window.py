import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        # setting up the window
        self.setWindowTitle("Robot hand")
        self.setGeometry(100, 100, 500, 400)

        # setting up the objects

        # setting up the docks
        self.set_manualdock()
        self.set_autodock()
        self.set_suctiondock()

        # setting up the graphics
        self.set_graphics()

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
        grid.addWidget(self.first_slider, 1, 0, 1, 2)
        self.first_slider.valueChanged.connect(self.first_slider_value_changed)

        # adding second label and slider for the layout
        label_second_slider = QLabel("2. joint \u03B8\u2082:")
        grid.addWidget(label_second_slider, 2, 0)
        self.label_second_theta = QLabel("{:.2f}\u00B0".format(0))
        grid.addWidget(self.label_second_theta, 2, 1)

        self.second_slider = QSlider(Qt.Horizontal)
        self.second_slider.setRange(0, 36000)  # 360 000 in order to have 0.01 increments from 0 to 360 degrees
        grid.addWidget(self.second_slider, 3, 0, 1, 2)
        self.second_slider.valueChanged.connect(self.second_slider_value_changed)

        # insert layout into the manual widget
        manualWidget.setLayout(grid)

    def first_slider_value_changed(self):
        theta_one = self.first_slider.value()*0.01  # from increments to degrees
        self.label_first_theta.setText("{:.2f}\u00B0".format(theta_one))
        # todo: save the theta 1 to robot class and update the coordinates of the joints
        #       of the robot using the robot.forward_kinematics function. After this,
        #       update the graphical object of the robot using the information from the robot class.

    def second_slider_value_changed(self):
        theta_two = self.second_slider.value()*0.01  # from increments to degrees
        self.label_second_theta.setText("{:.2f}\u00B0".format(theta_two))
        # todo: save the theta 2 to robot class and update the coordinates of the joints
        #       of the robot using the robot.forward_kinematics function. After this,
        #       update the graphical object of the robot using the information from the robot class.

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
        label_instruction = QLabel("Give the destination\ncoordinates in pixels.")
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
            if 0 <= int(self.x_line.text()) <= 5 and 0 <= int(self.y_line.text()) <= 5:
                self.label_reach.hide()
            else:
                self.label_reach.show()

    # setting up the suction dock
    def set_suctiondock(self):
        suctionDock = QDockWidget()
        suctionDock.setWindowTitle("Suction")
        # making the dock static and adding it to the left side
        suctionDock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(Qt.LeftDockWidgetArea, suctionDock)

        # adding Widget with button
        self.suction_button = QPushButton("Suck")
        suctionDock.setWidget(self.suction_button)

    # setting up the graphics for the robot and item
    def set_graphics(self):
        self.setCentralWidget(QTextEdit())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
