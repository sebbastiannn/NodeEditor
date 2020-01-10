from PyQt5.QtWidgets import *


class QDMNodeContentWidget(QWidget):
    def __init__(self, node, parent=None):
        self.node = node
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()                 # class is used to construct vertical box layout objects
        self.layout.setContentsMargins(0, 0, 0, 0)  # distance from the margin
        self.setLayout(self.layout)                 # applies a layout to a widget

        self.wdg_label = QLabel("Some Title")       # defined the Label (with default = Some Title)
        self.layout.addWidget(self.wdg_label)       # addWidget Window for fix text writing
        self.layout.addWidget(QDMTextEdit("test"))    # addWidget Window for text writing (with default = foo)

    def setEditingFlag(self, value):
        self.node.scene.grScene.views()[0].editingFlag = value


class QDMTextEdit(QTextEdit):
    def focusInEvent(self, event):
        self.parentWidget().setEditingFlag(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)
