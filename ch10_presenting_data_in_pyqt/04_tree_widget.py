import sys
from PyQt6.QtWidgets import (QApplication, QWidget,
                             QTreeWidget, QTreeWidgetItem, QVBoxLayout)
from PyQt6.QtGui import QIcon


class MainWindow(QWidget):

    def __init__(self):
        """Constructor for Empty Window Class."""
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(500, 300)
        self.setWindowTitle("QTreeWidget Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        tree_widget = QTreeWidget()
        tree_widget.setColumnCount(2)
        tree_widget.setHeaderLabels(
            ["Fruit Type", "Description"])
        tree_widget.setColumnWidth(0, 160)

        category_1 = QTreeWidgetItem(tree_widget, ["Apples",
                                                   "Edible fruit produced by an apple tree"])

        apple_list = [
            ["Braeburn", "Yellow with red stripes or blush",
                "data/ch10/icons/braeburn.png"],
            ["Empire", "Solid red", "data/ch10/icons/empire.png"],
            ["Ginger Gold", "Green-yellow", "data/ch10/icons/ginger_gold.png"]]

        for i in range(len(apple_list)):
            category_1_child = QTreeWidgetItem(apple_list[i][:2])
            category_1_child.setIcon(0, QIcon(apple_list[i][2]))
            category_1.addChild(category_1_child)

        category_2 = QTreeWidgetItem(tree_widget,
                                     ["Oranges", "A type of citrus fruit"])

        orange_list = [
            ["Navel", "Sweet and slightly bitter", "data/ch10/icons/navel.png"],
            ["Blood Orange", "Juicy and tart", "data/ch10/icons/blood_orange.png"],
            ["Clementine", "Usually seedless", "data/ch10/icons/clementine.png"]
        ]

        for i in range(len(orange_list)):
            category_2_child = QTreeWidgetItem(orange_list[i][:2])
            category_2_child.setIcon(0, QIcon(orange_list[i][2]))
            category_2.addChild(category_2_child)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(tree_widget)
        self.setLayout(main_v_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
