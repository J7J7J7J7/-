from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt

class TreeVisualizer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.root = None
        self.highlighted_node = None
        self.highlighted_path = []

    def set_tree(self, root):
        self.root = root
        self.update()

    def set_highlighted_node(self, node):
        self.highlighted_node = node
        self.update()

    def set_highlighted_path(self, path):
        self.highlighted_path = path
        self.update()

    def paintEvent(self, event):
        if not self.root:
            return

        painter = QPainter(self)
        self._draw_tree(painter, self.root, self.width() // 2, 50, self.width() // 4, 50)

    def _draw_tree(self, painter, node, x, y, h_spacing, v_spacing):
        if not node:
            return

        if node.left:
            painter.drawLine(x, y, x - h_spacing, y + v_spacing)
            self._draw_tree(painter, node.left, x - h_spacing, y + v_spacing, h_spacing // 2, v_spacing)

        if node.right:
            painter.drawLine(x, y, x + h_spacing, y + v_spacing)
            self._draw_tree(painter, node.right, x + h_spacing, y + v_spacing, h_spacing // 2, v_spacing)

        rect = (x - 15, y - 15, 30, 30)
        if node in self.highlighted_path:
            painter.setBrush(QBrush(Qt.yellow))
        elif node == self.highlighted_node:
            painter.setBrush(QBrush(Qt.red))
        else:
            painter.setBrush(QBrush(Qt.white))

        painter.drawEllipse(*rect)
        painter.drawText(*rect, Qt.AlignCenter, str(node.key))

