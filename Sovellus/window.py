import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Robot hand")

        self.setGeometry(100, 100, 500, 400)
        self.set_graphics()
        self.set_manualdock()
        self.set_autodock()
        self.set_suctiondock()

    # setting up the graphics for the robot and item
    def set_graphics(self):
        self.setCentralWidget(QTextEdit())

    # setting up the manual dock
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
        self.label_first_slider = QLabel("1. joint \u03B8\u2081: {:.2f}\u00B0".format(0))
        grid.addWidget(self.label_first_slider, 0, 0)
        first_slider = QSlider(Qt.Horizontal)
        # todo: add functionality for the slider
        first_slider.setRange(0, 360)

        grid.addWidget(first_slider, 1, 0)

        # adding second label and slider for the layout
        self.label_second_slider = QLabel("2. joint \u03B8\u2082: {:.2f}\u00B0".format(0))
        grid.addWidget(self.label_second_slider, 3, 0)
        second_slider = QSlider(Qt.Horizontal)
        # todo: add functionality for the slider
        second_slider.setRange(0, 360)

        grid.addWidget(second_slider, 4, 0)

        # insert layout into the manual widget
        manualWidget.setLayout(grid)

    # setting up the auto dock
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

        # adding the x coordinate sections
        label_x_line = QLabel("x:")
        grid.addWidget(label_x_line, 0, 0)
        x_line = QLineEdit()
        x_line.setValidator(QIntValidator())
        # todo: add functionality for the x_line
        grid.addWidget(x_line, 0, 1)

        # adding the y coordinate sections
        label_y_line = QLabel("y:")
        grid.addWidget(label_y_line, 1, 0)
        y_line = QLineEdit()
        y_line.setValidator(QIntValidator())
        # todo: add functionality for the y_line
        grid.addWidget(y_line, 1, 1)

        # insert layout into the auto widget
        autoWidget.setLayout(grid)

    # setting up the suction dock
    def set_suctiondock(self):
        suctionDock = QDockWidget()
        suctionDock.setWindowTitle("Suction")
        # making the dock static and adding it to the left side
        suctionDock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(Qt.LeftDockWidgetArea, suctionDock)

        # adding Widget
        self.suctionButton = QPushButton("Suck")
        suctionDock.setWidget(self.suctionButton)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
