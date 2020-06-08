#!/usr/bin/python

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QHBoxLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout()

        hbox.addWidget(QLabel("falcon"))
        hbox.addWidget(QLabel("owl"))
        hbox.addWidget(QLabel("eagle"))
        hbox.addWidget(QLabel("skylark"))

        self.setLayout(hbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QLabel')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
