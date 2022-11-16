from operator import attrgetter


class Graph:
        def __init__(self, nodes, connections):
            self.nodes = nodes
            self.connections = connections

            # Add the connections to the nodes
            for connection in connections:
                connection.toNode.connections.append(connection)
                connection.fromNode.connections.append(connection)

        # Get a node's connections
        def getNodeConnections(self, node):
            return node.connections

        # Get the node with the given name
        def getNode(self, name):
            for node in self.nodes:
                if node.nodeNumber == name:
                    return node

            return None


    # The node class is used to read in the raw node data from a text file. It has the following fields:
    # identifier, node number, status  (1=unvisited, 2=open, 3=closed), 
    # cost so far, estimated heuristic, estimated total, previous node in path, 
    # location x, location z, number plot position, name plot position, node Name (optional)
class Node:
    def __init__(self, identifier, nodeNumber, status, costSoFar, 
    heuristic, total, previous, x, z, numberPlotPosition, namePlotPosition, nodeName):
        self.identifier = identifier
        self.nodeNumber = nodeNumber
        self.status = status
        self.costSoFar = costSoFar
        self.heuristic = heuristic
        self.total = total
        self.previous = previous
        self.x = x
        self.z = z
        self.numberPlotPosition = numberPlotPosition
        self.namePlotPosition = namePlotPosition
        self.nodeName = nodeName
        self.connections = []
        self.connection = None

    def __str__(self):
        return f"{self.identifier}, {self.nodeNumber}, {self.status}, {self.costSoFar}, {self.heuristic}, {self.total}, {self.previous}, {self.x}, {self.z}, {self.numberPlotPosition}, {self.namePlotPosition}, {self.nodeName}"
    
    # The RawConnection class is used to read in the raw node data from a text file. It has the following fields:
    # connection number, from node, to node, connection cost
class Connection:
    def __init__(self, identifier, connectionNumber, fromNode, 
    toNode, connectionCost, costPlotPosition, type, nodes):
        self.identifier = identifier
        self.connectionNumber = connectionNumber
        self.connectionCost = connectionCost
        self.costPlotPosition = costPlotPosition
        self.type = type

        self.toNodeRecord = None

        self.fromNode = next((node for node in nodes if node.nodeNumber == fromNode), None)
        self.toNode = next((node for node in nodes if node.nodeNumber == toNode), None)

    
    # Get the cost of the connection
    def getCost(self):
        return self.connectionCost

    def __str__(self):
        return f"{self.identifier}, {self.connectionNumber}, {self.fromNode.nodeNumber}, {self.toNode.nodeNumber}, {self.connectionCost}, {self.costPlotPosition}, {self.type}"
