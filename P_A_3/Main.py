# John Ingram 2022
# Written for Mr. Sebastian's CS 330 class
# Assignment 3

import math
from Graph import *

class Main:

    def __init__(self):
        pass
    def run():
        print("Nodes: \n")

        nodes = Utilities.readNodes("P_A_3/Nodes.txt")

        for node in nodes:
            print(node)

        print("Connections: \n")

        connections = Utilities.readConnections("P_A_3/Connections.txt", nodes)

        for connection in connections:
            print(connection)


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



class Utilities:
    def __init__(self):
        pass
        
    # Read Nodes from a file
    def readNodes(filename):
        nodes = []
        with open(filename, "r") as file:
            for line in file:
                if line[0] == "#":
                    continue
                else:
                    line = line.split(",")
                    nodes.append(Node(str(line[0]).strip('\"') , int(line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5]), 
                    int(line[6]), float(line[7]), float(line[8]), 
                    int(line[9]), int(line[10]), str(line[11]).strip('\"\n').strip(' \"')))
                    
        return nodes

    # Read the Connections from a file, and return a list of connections
    def readConnections(filename, nodes):
        connections = []
        with open(filename, "r") as file:
            for line in file:
                if line[0] == "#":
                    continue
                else:
                    line = line.split(",")
                    connections.append(Connection(str(line[0]).strip('\"'), int(line[1]), int(line[2]), int(line[3]), 
                    int(line[4]), int(line[5]), int(line[6]), nodes))
                    
        return connections

    # findPathAStar
    # This function finds a path from the start node to the end node using the A* algorithm
    def findPathAStar(graph, startNode, endNode, heuristic):
         


if __name__ == "__main__":
    Main.run()
