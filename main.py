import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QWidget, QMessageBox
from tree import BinarySearchTree
from visualizer import TreeVisualizer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("二叉排序树与标记最近公共祖先_矫润祺")
        self.bst = BinarySearchTree()

        # 设置界面
        layout = QGridLayout() #网格布局
        self.visualizer = TreeVisualizer()

        self.input_x = QLineEdit(self)
        self.input_x.setPlaceholderText("输入节点 X")
        self.input_y = QLineEdit(self)
        self.input_y.setPlaceholderText("输入节点 Y")
        self.insert_input = QLineEdit(self)
        self.insert_input.setPlaceholderText("输入要插入的节点值")

        self.insert_btn = QPushButton("插入随机节点", self)
        self.manual_insert_btn = QPushButton("手动插入节点", self)
        self.find_lca_btn = QPushButton("标记最近公共祖先", self)

        layout.addWidget(self.visualizer, 0, 0, 1, 2)  # 视觉区域占据网格的第一行，跨两列
        layout.addWidget(self.insert_input, 1, 0)
        layout.addWidget(self.manual_insert_btn, 1, 1)
        layout.addWidget(self.input_x, 2, 0)
        layout.addWidget(self.input_y, 2, 1)
        layout.addWidget(self.find_lca_btn, 2, 2)
        layout.addWidget(self.insert_btn, 3, 0)


        container = QWidget()
        container.setLayout(layout)
        container.setFixedSize(1600,1000)
        self.setCentralWidget(container)

        # 信号和槽
        self.insert_btn.clicked.connect(self.insert_nodes)
        self.manual_insert_btn.clicked.connect(self.manual_insert)
        self.find_lca_btn.clicked.connect(self.find_lca)


    def insert_nodes(self):
        import random
        for _ in range(10):  # 插入10个随机节点
            self.bst.insert(random.randint(1, 100))
        self.visualizer.set_tree(self.bst.root)

    def manual_insert(self):
        try:
            value = int(self.insert_input.text())
        except ValueError:
            QMessageBox.warning(self, "输入错误", "请输入有效的整数值！")
            return

        self.bst.insert(value)
        self.visualizer.set_tree(self.bst.root)
        self.insert_input.clear()

    def find_lca(self):
        try:
            x = int(self.input_x.text())
            y = int(self.input_y.text())
        except ValueError:
            QMessageBox.warning(self, "输入错误", "请输入有效的整数值！")
            return

        if not self._is_node_in_tree(self.bst.root, x) or not self._is_node_in_tree(self.bst.root, y):
            QMessageBox.warning(self, "节点不存在", "输入的节点值不在树中，请检查！")
            return

        lca = self.bst.find_lca(x, y)
        if lca:
            self.visualizer.set_highlighted_node(lca)  # 高亮最近公共祖先
            self.visualizer.set_highlighted_path([])  # 清除路径高亮

    def _is_node_in_tree(self, node, value):
        if not node:
            return False
        if node.key == value:
            return True
        if value < node.key:
            return self._is_node_in_tree(node.left, value)
        return self._is_node_in_tree(node.right, value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
