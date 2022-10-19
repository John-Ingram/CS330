# John Ingram 2022
# Written for Mr. Sebastian's CS 330 class
# Assignment 2

import math
from Character import Character

class Movement:
    def __init__(self, position, velocity, orientation):
        self.position = position
        self.velocity = velocity
        self.orientation = orientation

    # output the movement's data as position, velocity, orientation
    def __str__(self):
        return f"{self.position}, {self.velocity}, {self.orientation}"

# Steering output class
# contains liner acceleration (2d vector), and angular acceleration (float)
class SteeringOutput:
    def __init__(self):
        self.linear = Vector2(0, 0)
        self.angular = 0

# Vector2 class
# This class is used to represent a 2D vector, which can be used to represent position, velocity, and more.
class Vector2:
    def __init__(self, x, z):
        self.x = x
        self.z = z
    
    # Returns the magnitude of the vector
    def magnitude(self):
        return math.sqrt(self.x**2 + self.z**2)

    # Returns the normalized vector
    def normalized(self):
        magnitude = self.magnitude()
        return Vector2(self.x / magnitude, self.z / magnitude)

    # Normalize this vector
    def normalize(self):
        magnitude = self.magnitude()
        self.x /= magnitude
        self.z /= magnitude

    # Returns the dot product of this vector and the given vector
    def dot(self, other):
        return self.x * other.x + self.z * other.z

    # additon operator
    def __add__(self, other):
        return Vector2(self.x + other.x, self.z + other.z)

    # subtraction operator
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.z - other.z)
    
    # multiplication operator
    def __mul__(self, other):
        return Vector2(self.x * other, self.z * other) 

    # division operator
    def __truediv__(self, other):
        return Vector2(self.x / other, self.z / other)
    
    #output the vector's data as x, z
    def __str__(self):
        return f"{self.x}, {self.z}"

# Utility class
# This class contains utility functions
class Util:
    def __init__(self):
        pass
    
    # Find the point on a line segment that is closest to a given point
    def closestPoint(segmentStart, segmentEnd, point):
        segment = segmentEnd - segmentStart
        t = (point - segmentStart).dot(segment) / (segment).dot(segment)
        if t <= 0:
            return segmentStart
        elif t >= 1:
            return segmentEnd
        else:
            return segmentStart + (segment * t)