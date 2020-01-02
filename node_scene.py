from node_graphics_scene import QDMGraphicsScene

class Scene:
    def __init__(self):
        self.node = []
        self.edges = []

        self.scene_width = 64000
        self.scene_height = 64000

        self.initUI()

    def initUI(self):
        self.grScene = QDMGraphicsScene(self)
        self.grScene.setGrScene(self.scene_width, self.scene_height)


    def addNode(self, node):
        self.node.append(node)

    def addEdge(self, edge):
        self.node.append(edge)

    def removeNote(self, node):
        self.node.remove(node)

    def removeEdge(self, edge):
        self.node.remove(edge)
