from node_graphics_edge import *


EDGE_TYPE_DIRECT = 1    # index for direct connection
EDGE_TYPE_BEZIER = 2    # index for curved connection

DEBUG = False           # for True can check the debuging stuff in the console

class Edge:

    def __init__(self, scene, start_socket, end_socket, edge_type=EDGE_TYPE_DIRECT):

        self.scene = scene

        self.start_socket = start_socket
        self.end_socket = end_socket

        self.start_socket.edge = self
        if self.end_socket is not None:
            self.end_socket.edge = self

        self.grEdge = QDMGraphicsEdgeDirect(self) if edge_type == EDGE_TYPE_DIRECT else QDMGraphicsEdgeBezier(self) # depending on which line type you want to take

        self.updatePositions()
        if DEBUG: print("Edge: ", self.grEdge.posSource, "to", self.grEdge.posDestination)
        self.scene.grScene.addItem(self.grEdge)

    # when we are actually creating an edge we wil definitly created in our window
    # when we dont know the end Socket yet and drag around the line
    def updatePositions(self):
        source_pos = self.start_socket.getSocketPosition()
        source_pos[0] += self.start_socket.node.grNode.pos().x()
        source_pos[1] += self.start_socket.node.grNode.pos().y()
        self.grEdge.setSource(*source_pos)
        if self.end_socket is not None:
            end_pos = self.end_socket.getSocketPosition()
            end_pos[0] += self.end_socket.node.grNode.pos().x()
            end_pos[1] += self.end_socket.node.grNode.pos().y()
            self.grEdge.setDestination(*end_pos)
        if DEBUG: print(" SS:", self.start_socket)
        if DEBUG: print(" ES:", self.end_socket)
        self.grEdge.update()

    def remove_from_sockets(self):
        if self.start_socket is not None:
            self.start_socket.edge = None
        if self.end_socket is not None:
            self.end_socket.edge = None
        self.end_socket = None
        self.start_socket = None

    # remove all the contact from the edges
    def remove(self):
        self.remove_from_sockets()
        self.scene.grScene.removeItem(self.grEdge)
        self.grEdge = None
        self.scene.removeEdge(self)