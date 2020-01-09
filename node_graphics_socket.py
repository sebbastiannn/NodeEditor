from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QDMGraphicsSocket(QGraphicsItem):
    def __init__(self, socket, socket_type=1):
        self.socket = socket
        super().__init__(socket.node.grNode)

        self.radius = 6.0           # radius of the circle from the socket
        self.outline_width = 1.0    # width of the Outlines of the circle
        # color of the circles
        self._colors = [
            QColor("#FFFF7700"),    # orange
            QColor("#FF52e220"),    # green
            QColor("#FF0056a6"),    # blue
            QColor("#FFa86db1"),    # purple
            QColor("#FFb54747"),    # red
            QColor("#FFdbe220"),    # yellow
        ]
        self._color_background = self._colors[socket_type]
        self._color_outline = QColor("#FF000000")   # black for the outlines

        self._pen = QPen(self._color_outline)
        self._pen.setWidthF(self.outline_width)
        self._brush = QBrush(self._color_background)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        # painting circle
        painter.setBrush(self._brush)
        painter.setPen(self._pen)
        painter.drawEllipse(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)

    def boundingRect(self):
        return QRectF(
            - self.radius - self.outline_width,
            - self.radius - self.outline_width,
            2 * (self.radius + self.outline_width),
            2 * (self.radius + self.outline_width),
        )
