from operator import attrgetter


class Graph:
        def __init__(self, nodes, connections):
            self.nodes = nodes
            self.connections = connections

            # Add the connections to the nodes
            for connection in connections:
                connection.toNode.connections.append(connection)
                connection.fromNode.connections.append(connection)

        # Add a node to the graph
        def addNode(self, node):
            self.nodes.append(node)

        # Get a node's connections
        def getNodeConnections(self, node):
            return node.connections

        # Get the connections for a given node
        def getConnections(self, nodeNumber):
            node = next((node for node in self.nodes if node.nodeNumber == nodeNumber), None)
            if node is None:
                return None
            else:
                return node.connections

        # Get the nodes in the graph
        def getNodes(self):
            return self.nodes

        # Get the connections in the graph
        def getConnections(self):
            return self.connections

        # Get the number of nodes in the graph
        def getNumNodes(self):
            return len(self.nodes)

        # Get the number of connections in the graph
        def getNumConnections(self):
            return len(self.connections)

        # Get the node with the given name
        def getNode(self, name):
            for node in self.nodes:
                if node.nodeNumber == name:
                    return node

            return None

        # Get the connection between the given nodes
        def getConnection(self, node1, node2):
            for connection in self.connections:
                if (connection.node1 == node1 and connection.node2 == node2) or (connection.node1 == node2 and connection.node2 == node1):
                    return connection

            return None

        # Get the connection with the given name
        def getConnectionByName(self, name):
            for connection in self.connections:
                if connection.name == name:
                    return connection

            return None

        # Get the node at the given index
        def getNodeByIndex(self, index):
            return self.nodes[index]

        # Get the connection at the given index
        def getConnectionByIndex(self, index):
            return self.connections[index]

        # Get the index of the given node
        def getNodeIndex(self, node):
            return self.nodes.index(node)

        # Get the index of the given connection
        def getConnectionIndex(self, connection):
            return self.connections.index(connection)

        # Get the index of the node with the given name
        def getNodeIndexByName(self, name):
            for i in range(len(self.nodes)):
                if self.nodes[i].name == name:
                    return i



    # The RawNode class is used to read in the raw node data from a text file. It has the following fields:
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

    # Get the connections for the node
    def getConnections(self):
        return self.connections

    # Get the number of connections for the node
    def getNumConnections(self):
        return len(self.connections)

    # Get the connection at the given index
    def getConnectionByIndex(self, index):
        return self.connections[index]

    # Get the index of the given connection
    def getConnectionIndex(self, connection):
        return self.connections.index(connection)

    # Add a connection to the node
    def addConnection(self, connection):
        self.connections.append(connection)

    # Remove a connection from the node
    def removeConnection(self, connection):
        self.connections.remove(connection)

    # Remove all connections from the node
    def removeAllConnections(self):
        self.connections = []

    # Get the connection with the given index
    def getConnectionByIndex(self, index):
        return self.connections[index]

    # Get the index of the given connection
    def getConnectionIndex(self, connection):
        return self.connections.index(connection)


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

        self.fromNodeRecord = None
        self.toNodeRecord = None

        self.fromNode = next((node for node in nodes if node.nodeNumber == fromNode), None)
        self.toNode = next((node for node in nodes if node.nodeNumber == toNode), None)

    # Get the name of the connection
    def getName(self):
        return self.connectionNumber
    
    # Get the cost of the connection
    def getCost(self):
        return self.connectionCost

    def __str__(self):
        return f"{self.identifier}, {self.connectionNumber}, {self.fromNode.nodeNumber}, {self.toNode.nodeNumber}, {self.connectionCost}, {self.costPlotPosition}, {self.type}"


    # The Path class is used to store the path found by the A* algorithm. It has the following fields:
    # Start node, end node, total cost, list of nodes in the path
class Path:
    def __init__(self, startNode, endNode):
        self.startNode = startNode
        self.endNode = endNode
        self.totalCost = 0.0
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)

    def smallestElement(self):
        return min(self.nodes, key=attrgetter())

    # Get the start node of the path
    def getStartNode(self):
        return self.startNode
    
    # Get the end node of the path
    def getEndNode(self):
        return self.endNode
    
    # Get the total cost of the path
    def getTotalCost(self):
        return self.totalCost

    # Get the list of nodes in the path
    def getNodes(self):
        return self.nodes
    
    # Reverse the path
    def reverse(self):
        self.nodes.reverse()
    