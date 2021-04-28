import unittest
from robot import Robot
import math
import numpy as np


class KinematicsTest(unittest.TestCase):
    def setUp(self):
        link1 = 150
        link2 = 150
        self.robot = Robot(link1, link2)

    def testForwardKinematics(self):
        # the coordinates from the forward kinematics function are rounded to 6 decimals
        # due to the fact of rounding errors in float numbers.
        # there is no particular reason to use exact 6 decimals, but I thought it has high enough accuracy.

        # theta1 = 0° and theta2 = 0°
        self.robot.forward_kinematics(math.radians(0), math.radians(0))
        self.robot.coord1 = np.array([np.round(self.robot.coord1[0], 6), np.round(self.robot.coord1[1], 6)])
        self.robot.coord2 = np.array([np.round(self.robot.coord2[0], 6), np.round(self.robot.coord2[1], 6)])

        self.assertEqual(self.robot.coord1.all(), np.array([150, 0]).all())
        self.assertEqual(self.robot.coord2.all(), np.array([300, 0]).all())

        # theta1 = 90° and theta2 = 90°
        self.robot.forward_kinematics(math.radians(90), math.radians(90))
        self.robot.coord1 = np.array([np.round(self.robot.coord1[0], 6), np.round(self.robot.coord1[1], 6)])
        self.robot.coord2 = np.array([np.round(self.robot.coord2[0], 6), np.round(self.robot.coord2[1], 6)])

        self.assertEqual(self.robot.coord1.all(), np.array([0, 150]).all())
        self.assertEqual(self.robot.coord2.all(), np.array([-150, 150]).all())

    def testInverseKinematics(self):
        # the angles from the inverse kinematics function are rounded to 6 decimals
        # due to the fact of rounding errors in float numbers.
        # there is no particular reason to use exact 6 decimals, but I thought it has high enough accuracy.

        # x = 0 and y = 300
        self.robot.inverse_kinematics(300, 0)
        self.assertEqual(np.round(self.robot.theta1, 6), np.round(math.radians(0), 6))
        self.assertEqual(np.round(self.robot.theta2, 6), np.round(math.radians(0), 6))

        # x = 150 and y = -150
        self.robot.inverse_kinematics(150, -150)
        self.assertEqual(np.round(self.robot.theta1, 6), np.round(math.radians(-90), 6))
        self.assertEqual(np.round(self.robot.theta2, 6), np.round(math.radians(90), 6))


if __name__ == "__main__":
    unittest.main()
