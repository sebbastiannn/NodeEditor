from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from node_scene import Scene
from node_node import Node
from node_edge import Edge, EDGE_TYPE_BEZIER, EDGE_TYPE_DIRECT
from node_graphics_view import QDMGraphicsView

class NodeEditorWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stylesheet_filename = 'qss/nodestyle.qss'
        self.loadStylesheet(self.stylesheet_filename) # loads style sheet for the nodes

        self.initUI() # start User Interface

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)                    # set Geometry of the Window
        self.layout = QVBoxLayout()                             # 1 so that your graphic scene is as big as the window
        self.layout.setContentsMargins(0, 0, 0, 0)              #removes the frame (Rahmen) from the editor/ sets it to 0
        self.setLayout(self.layout)
    # create graphic scene
        self.scene = Scene()
        self.addNodes()                                         # add Nodes to the scene
    # create graphic view
        self.view = QDMGraphicsView(self.scene.grScene, self)

        self.layout.addWidget(self.view)                        # 1 so that your graphic scene is as big as the window

        self.setWindowTitle("Node Editor")                      # set Title of Window to Node Editor
        self.show()

    def addNodes(self):
        node1 = Node(self.scene, "My Awesome Node 1", inputs=[0, 0, 0], outputs=[1])
        node2 = Node(self.scene, "My Awesome Node 2", inputs=[3, 3, 3], outputs=[1])
        node3 = Node(self.scene, "My Awesome Node 3", inputs=[2, 2, 2], outputs=[1])
        node1.setPos(-350, -250)                                                        # set the positions of the node
        node2.setPos(-75, 0)
        node3.setPos(200, -150)

        edge1 = Edge(self.scene, node1.outputs[0], node2.inputs[0], edge_type=EDGE_TYPE_BEZIER)
        edge2 = Edge(self.scene, node2.outputs[0], node3.inputs[0], edge_type=EDGE_TYPE_BEZIER)

    # just a test how everthing work
    # self.addDebugContent()
    def addDebugContent(self):
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        rect = self.grScene.addRect(-100, -100, 80, 100, outlinePen, greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        text = self.grScene.addText("This is my Awesome text!", QFont("Ubuntu"))
        text.setFlag(QGraphicsItem.ItemIsSelectable)
        text.setFlag(QGraphicsItem.ItemIsMovable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0))

        widget1 = QPushButton("Hello World")
        proxy1 = self.grScene.addWidget(widget1)
        proxy1.setFlag(QGraphicsItem.ItemIsMovable)
        proxy1.setPos(0, 30)

        widget2 = QTextEdit()
        proxy2 = self.grScene.addWidget(widget2)
        proxy2.setFlag(QGraphicsItem.ItemIsSelectable)
        proxy2.setPos(0, 60)

        line = self.grScene.addLine(-200, -200, 400, -100, outlinePen)
        line.setFlag(QGraphicsItem.ItemIsMovable)
        line.setFlag(QGraphicsItem.ItemIsSelectable)

    def loadStylesheet(self, filename):
        print('STYLE loading:', filename)
        file = QFile(filename)
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll()
        QApplication.instance().setStyleSheet(str(stylesheet, encoding='utf-8'))




