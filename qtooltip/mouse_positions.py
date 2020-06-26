#!/usr/bin/python


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QToolTip


class MyWidget(QWidget):
    
    def __init__(self, parent):
        super().__init__()


        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('QWidget { background: #007AA5; border-radius: 3px;}')
        self.setMouseTracking(True)

    
    def mouseMoveEvent(self, e):

        self.x = e.x()
        self.y = e.y()

        p = self.mapToGlobal(e.pos())

        QToolTip.showText(p, f'{self.x}:{self.y}') 


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()

        self.w1 = MyWidget(self)
        self.w2 = MyWidget(self)
        self.w3 = MyWidget(self)
        self.w4 = MyWidget(self)
        self.w5 = MyWidget(self)
        self.w6 = MyWidget(self)
        self.w7 = MyWidget(self)
        self.w8 = MyWidget(self)
        self.w9 = MyWidget(self)

        grid.addWidget(self.w1, 0, 0)
        grid.addWidget(self.w2, 0, 1)
        grid.addWidget(self.w3, 0, 2)
        grid.addWidget(self.w4, 1, 0)
        grid.addWidget(self.w5, 1, 1)
        grid.addWidget(self.w6, 1, 2)
        grid.addWidget(self.w7, 2, 0)
        grid.addWidget(self.w8, 2, 1)
        grid.addWidget(self.w9, 2, 2)

        self.setLayout(grid)

        self.setGeometry(300, 300, 500, 350)
        self.setWindowTitle('Mouse positions')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
