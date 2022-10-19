# John Ingram 2022
# Written for Mr. Sebastian's CS 330 class
# Assignment 2

from Utilities import *


# Pathpoint class
# This class is used to represent a point on a path
# It contains a Vector2 position, and a float path parameter
class PathPoint:
    def __init__(self, position, pathParameter):
        self.position = position
        self.pathParameter = pathParameter

    # output the pathpoint's data as position, path parameter
    def __str__(self):
        return f"At: {self.position}, Param: {self.pathParameter}\n"


# Path class
# This class is used to represent a path, which is a list of 2D vectors
class Path:
    def __init__(self, points):
        self.length = 0
        # assemble the path from the given points
        for i in points:
            if i == points[0]:
                self.path = [PathPoint(i, 0)]
            else:
                self.length += (i - points[points.index(i) - 1]).magnitude()
                self.path.append(PathPoint(i, self.length))
        
        # normalize the path parameter
        for i in self.path:
            i.pathParameter /= self.length
            

    # Returns the first point on the path
    def getStart(self):
        return self.path[0]

    # Returns the last point on the path
    def getEnd(self):
        return self.path[len(self.path) - 1]

    # Calculates the position on the path at the given path parameter
    def getPosition(self, pathParameter):
        if pathParameter < 0 or pathParameter > 1:
            if pathParameter < 0:
                return self.path[0].position
            else:
                return self.getEnd().position

        # find the two points on the path that the path parameter is between
        for i in self.path:
            if i.pathParameter > pathParameter:
                point1 = self.path[self.path.index(i) - 1]
                point2 = i
                break

        # calculate the position on the path at the given path parameter
        position = point1.position + (point2.position - point1.position) * (pathParameter - point1.pathParameter) / (point2.pathParameter - point1.pathParameter)
        return position

    # Calculates the path parameter at the given position
    def getParam(self, position):
        closestPoint = self.path[0].position
        segment = [self.path[0], self.path[1]]
        distance = 90000000
        for i in self.path:
            tempSegment = [self.path[self.path.index(i) - 1], i]
            tempClosestPoint = Util.closestPoint(tempSegment[0].position, tempSegment[1].position, position)
            tempDistance = (tempClosestPoint - position).magnitude()
            if tempDistance <= distance:
                distance = tempDistance
                closestPoint = tempClosestPoint
                segment = tempSegment
            
        # calculate the path parameter at the given position
        t = (closestPoint - segment[0].position).magnitude() / (segment[1].position - segment[0].position).magnitude()
        pathParameter = segment[0].pathParameter + t * (segment[1].pathParameter - segment[0].pathParameter)
        return pathParameter

    # Returns the path as a string
    def __str__(self):
        return f"{self.path}"
        