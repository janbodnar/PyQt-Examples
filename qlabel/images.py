#!/usr/bin/python


import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QHBoxLayout
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout()

        lbl1 = QLabel()
        lbl1.setPixmap(QPixmap("cpu.png"))

        lbl2 = QLabel()
        lbl2.setPixmap(QPixmap("drive.png"))

        lbl3 = QLabel()
        lbl3.setPixmap(QPixmap("laptop.png"))

        lbl4 = QLabel()
        lbl4.setPixmap(QPixmap("player.png"))

        hbox.addWidget(lbl1)
        hbox.addWidget(lbl2)
        hbox.addWidget(lbl3)
        hbox.addWidget(lbl4)

        self.setLayout(hbox)

        self.move(300, 300)
        self.setWindowTitle('Images')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
