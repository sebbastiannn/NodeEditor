from PyQt5.QtWidgets import *

class QDMNodeContentWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()                 # class is used to construct vertical box layout objects
        self.layout.setContentsMargins(0, 0, 0, 0)  # distance from the margin
        self.setLayout(self.layout)                 # applies a layout to a widget

        self.wdg_label = QLabel("Some Title")       # defined the Label (with default = Some Title)
        self.layout.addWidget(self.wdg_label)       # addWidget Window for fix text writing
        self.layout.addWidget(QTextEdit("foo"))     # addWidget Window for text writing (with default = foo)
