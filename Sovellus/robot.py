import math


class Robot:
    # initializing the robot information
    def __init__(self, len1, len2):
        # adding the 'physical' information about the robot arm
        self.len1 = len1
        self.len2 = len2
        self.theta1 = 0  # first angle in degrees
        self.theta2 = 0  # second in degrees
        self.coord1 = self.len1, 0  # second angle initial position
        self.coord2 = self.len1 + self.len2, 0   # end-effector initial position
        self.suction = False

    def move_with_angles(self, robot_graphics, square, square_graphics, theta1, theta2):
        # updating the angles
        self.theta1 = theta1
        self.theta2 = theta2

        # updates the coordinates of the robot based on the new angles
        self.forward_kinematics(square, self.theta1, self.theta2)

        # update the robot graphics and square graphics item
        robot_graphics.update_pose()
        square_graphics.update_position()

    def move_with_coordinates(self, window, x, y):
        # todo: Linear movement towards the destined coordinate; update graphics in each loop
        #       Use the inverse_kinematics function.
        pass

    def forward_kinematics(self, square, theta1, theta2):
        # changing into radians for easier calculation
        theta1 = math.radians(theta1)
        theta2 = math.radians(theta2)

        # calculating the coordinates of the second joint (forward kinematics)
        x1 = self.len1 * math.cos(theta1)
        y1 = self.len1 * math.sin(theta1)

        # changing the coordinates of the second joint
        self.coord1 = x1, y1

        # calculating the coordinates of the end-effector (forward kinematics)
        x2 = x1 + self.len2 * math.cos(theta1 + theta2)
        y2 = y1 + self.len2 * math.sin(theta1 + theta2)

        # changing the coordinates of the end-effector
        self.coord2 = x2, y2

        # if suction is True, it means that the square has been sucked by the robot --> same coordinate as end-effector
        if self.suction:
            square.set_location(self.coord2)

    def inverse_kinematics(self, coordinates):
        # todo: Change joint angles in degrees based on the given coordinates
        pass
