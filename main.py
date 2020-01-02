import sys
from PyQt5.QtWidgets import *

from node_editor_wnd import NodeEditorWnd

if __name__=='__main__':
    app = QApplication(sys.argv)
    # open window
    wnd = NodeEditorWnd()
    # quits the application
    sys.exit(app.exec_())


