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


        print("\nFinding Paths:", end="")
        # Run the A* algorithm
        graph = Graph(nodes, connections)

        Utilities.aStarPrint(graph, 1, 29)
        Utilities.aStarPrint(graph, 1, 38)
        Utilities.aStarPrint(graph, 11, 1)
        Utilities.aStarPrint(graph, 33, 66)
        Utilities.aStarPrint(graph, 58, 43)



class Utilities:
    def __init__(self):
        pass
        
    def aStarPrint(graph, start, end):
        output = Utilities.findPathAStar(graph, start, end)
        path = output[0]
        cost = output[1]
        
        print(f"\nPath from {start} to {end} path =", end="")

        for node in path:
            print(f" {node.nodeNumber}", end="")

        # Print the cost of the path
        print(f" Cost = {cost}")

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
    def findPathAStar(graph, startNodeNumber, goalNodeNumber):
        startNode = graph.getNode(startNodeNumber)
        goal = graph.getNode(goalNodeNumber)
        heuristic = Heuristic(goal)
        startRecord = NodeRecord(startNode)
        startRecord.costSoFar = 0
        startRecord.estimatedTotalCost = heuristic.estimate(startNode)

        open = PathFindingList()
        open.add(startRecord)

        closed = PathFindingList()

        while open.length() > 0:
            # Get the node with the lowest estimated total cost
            current = open.smallestElement()

            # If the current node is the goal, then exit the loop
            if current.node == goal: 
                break
            
            # Get the current node's connections
            connections = graph.getNodeConnections(current.node)
            
            # Loop through the connections
            for connection in connections:
                toNode = connection.toNode
                toNodeCost = current.costSoFar + connection.getCost()
                
                # Check if the node is in the closed list
                if closed.containsNode(toNode):
                    toNodeRecord = closed.getNodeRecord(toNode)
                    # If the node is in the closed list, 
                    # and the cost is less than the cost in the closed list, 
                    # then remove the node from the closed list
                    if toNodeRecord.costSoFar <= toNodeCost:
                        continue

                    closed.remove(toNodeRecord) # Remove the node from the closed list because the new path is better
                    toNodeHeuristic = toNodeRecord.estimatedTotalCost - toNodeRecord.costSoFar
                elif open.containsNode(toNode):
                    toNodeRecord = open.getNodeRecord(toNode)
                    # If the node is in the open list, 
                    # and the cost is less than the cost in the open list, 
                    # then remove the node from the open list
                    if toNodeRecord.costSoFar <= toNodeCost:
                        continue

                    toNodeHeuristic = toNodeRecord.estimatedTotalCost - toNodeRecord.costSoFar
                else:
                    toNodeRecord = NodeRecord(toNode)
                    toNodeHeuristic = heuristic.estimate(toNode)
                
                # Update the Node record
                toNodeRecord.setCostSoFar(toNodeCost)
                toNodeRecord.setConnection(connection)
                toNodeRecord.estimatedTotalCost = toNodeCost + toNodeHeuristic

                if not open.containsNode(toNode):
                    open.add(toNodeRecord)
            
            open.remove(current)
            closed.add(current)
        
        if current.node != goal:
            print("No path found")
            return None
            
        else:
            # Asseble the path
            path = []

            currentNode = current.node
            while currentNode != startNode:
                path.append(currentNode)
                currentNode = currentNode.connection.fromNode
            
            path.append(startNode)

            path.reverse()

            return [path, path[-1].costSoFar]

class Heuristic:
    def __init__(self, goal):
        self.goal = goal
        pass

    # This function estimates the cost between the given node and the goal node
    # Using the Euclidean distance
    def estimate(self, node):
        return math.sqrt((node.x - self.goal.x)**2 + (node.z - self.goal.z)**2)


class PathFindingList:
    def __init__(self):
        self.list = []

    def add(self, nodeRecord):
        self.list.append(nodeRecord)

    def remove(self, nodeRecord):
        self.list.remove(nodeRecord)

    def containsNode(self, node):
        for nodeRecord in self.list:
            if nodeRecord.node == node:
                return True
        return False

    def getNodeRecord(self, node):
        for nodeRecord in self.list:
            if nodeRecord.node == node:
                return nodeRecord
        return None

    # Returns the node record with the lowest estimated total cost
    def smallestElement(self):
        return min(self.list, key=lambda x: x.estimatedTotalCost)

    def length(self):
        return len(self.list)

    # prints each node in the list
    def __str__(self):
        string = "[ "
        for nodeRecord in self.list:
            string += f"{nodeRecord.node.nodeNumber}, "
        return string + "]"

       

         
class NodeRecord:
    def __init__(self, node):
        self.node = node
        self.connection = None
        self.cost = 0
        self.costSoFar = 0.0
        self.estimatedTotalCost = 0.0

        self.node.connection = self.connection

    def setCostSoFar(self, cost):
        self.costSoFar = cost
        self.node.costSoFar = cost

    def setConnection(self, connection):
        self.connection = connection
        self.node.connection = connection

    def __str__(self):
        return f"Node: {self.node}, Connection: {self.connection}, CostSoFar: {self.costSoFar}, EstimatedTotalCost: {self.estimatedTotalCost}"

if __name__ == "__main__":
    Main.run()
