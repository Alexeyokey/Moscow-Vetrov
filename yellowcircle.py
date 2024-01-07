from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
import random
import sys

class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.label.setPixmap(QtGui.QPixmap(800, 800))
        self.setCentralWidget(self.label)
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 800)
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)
        self.pushButton.move(350, 400)
        self.color = QColor("yellow")

    def draw(self):
        qp = QPainter(self.label.pixmap())
        qp.setPen(self.color)
        size = random.randint(1, 200)
        coords = (random.randint(0, 750), random.randint(0, 750))
        qp.drawEllipse(*coords, size, size)
        qp.begin(self)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    examp = Circle()
    examp.show()
    sys.exit(app.exec())
