import math
import numpy as np
import decimal
from time import sleep


class Robot:
    # initializing the robot information
    def __init__(self, len1, len2):
        # adding the 'physical' information about the robot arm
        self.len1 = len1
        self.len2 = len2
        self.theta1 = 0  # first angle in degrees
        self.theta2 = 0  # second in degrees
        self.coord1 = np.array([self.len1, 0])  # second angle initial position
        self.coord2 = np.array([self.len1 + self.len2, 0])   # end-effector initial position
        self.suction = False
        self.automatic = False

    def move_with_angles(self, robot_graphics, square, square_graphics, theta1, theta2):
        # updating the angles
        self.theta1 = theta1
        self.theta2 = theta2

        # updates the coordinates of the robot based on the new angles
        self.forward_kinematics(self.theta1, self.theta2)

        # if suction is True, it means that the square has been sucked by the robot --> same coordinate as end-effector
        if self.suction:
            square.set_pose(self.coord2, self.theta1, self.theta2)

        # update the robot graphics and square graphics item
        robot_graphics.update_pose()
        square_graphics.update_pose()

    def move_with_coordinates(self, window, app, robot_graphics, square, square_graphics, x, y):
        # the initial and final coordinate of the end-effector
        coord_initial = self.coord2
        coord_final = np.array([x, y])

        # this variable is used to determine how to move the arm
        theta2_initial = self.theta2

        # using a variable to distinguish between the user and automatic movement for the slider
        self.automatic = True

        # update graphics in each loop
        for s in np.arange(0, 1.01, 0.01):
            # change in end-effector coordinate
            self.coord2 = (1 - s) * coord_initial + s * coord_final

            # use inverse kinematics to update the new angles for the joints
            self.inverse_kinematics(self.coord2[0], self.coord2[1], theta2_initial)

            # calculating the joint coordinate of the second joint using forward kinematics
            self.coord1[0] = self.len1 * math.cos(self.theta1)
            self.coord1[1] = self.len1 * math.sin(self.theta1)

            # if suction is True, it means that the square has been sucked by the robot
            # --> same coordinate as end-effector
            if self.suction:
                square.set_pose(self.coord2, self.theta1, self.theta2)

            # changing joint angles in degrees for better interpretation
            self.theta1 = math.degrees(self.theta1)
            self.theta2 = math.degrees(self.theta2)

            # update the sliders
            window.first_slider.setValue(self.theta1 * 100)
            window.second_slider.setValue(self.theta2 * 100)

            # update the robot graphics and square graphics item
            robot_graphics.update_pose()
            square_graphics.update_pose()

            # show graphics
            app.processEvents()

            # wait for a certain time so that the animation looks smoother
            sleep(0.01)

        # Back to the user control
        self.automatic = False

    def forward_kinematics(self, theta1, theta2):
        # changing into radians for easier calculation
        theta1 = math.radians(theta1)
        theta2 = math.radians(theta2)

        # calculating the coordinates of the second joint (forward kinematics)
        x1 = self.len1 * math.cos(theta1)
        y1 = self.len1 * math.sin(theta1)

        # changing the coordinates of the second joint
        self.coord1 = np.array([x1, y1])

        # calculating the coordinates of the end-effector (forward kinematics)
        x2 = x1 + self.len2 * math.cos(theta1 + theta2)
        y2 = y1 + self.len2 * math.sin(theta1 + theta2)

        # changing the coordinates of the end-effector
        self.coord2 = np.array([x2, y2])

    def inverse_kinematics(self, x, y, theta2_initial):
        # calculating the angles in radians
        if x == 0:
            if theta2_initial < 0:
                self.theta2 = math.acos((x**2 + y**2 - self.len1**2 - self.len2**2) / (2 * self.len1 * self.len2))
                self.theta1 = math.pi / 2 + math.atan2((self.len2 * math.sin(self.theta2)), (self.len1 + self.len2 * math.cos(self.theta2)))
            else:
                self.theta2 = math.acos((x ** 2 + y ** 2 - self.len1 ** 2 - self.len2 ** 2) / (2 * self.len1 * self.len2))
                self.theta1 = math.pi / 2 - math.atan2((self.len2 * math.sin(self.theta2)), (self.len1 + self.len2 * math.cos(self.theta2)))
        else:
            if theta2_initial < 0:
                self.theta2 = math.acos((x**2 + y**2 - self.len1**2 - self.len2**2) / (2 * self.len1 * self.len2))
                self.theta1 = math.atan2(y, x) + math.atan2((self.len2 * math.sin(self.theta2)), (self.len1 + self.len2 * math.cos(self.theta2)))
            else:
                self.theta2 = math.acos((x ** 2 + y ** 2 - self.len1 ** 2 - self.len2 ** 2) / (2 * self.len1 * self.len2))
                self.theta1 = math.atan2(y, x) - math.atan2((self.len2 * math.sin(self.theta2)), (self.len1 + self.len2 * math.cos(self.theta2)))


