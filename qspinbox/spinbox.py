#!/usr/bin/python


from PyQt5.QtWidgets import (QWidget, QSpinBox, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout()

        sbox = QSpinBox(self)

        sbox.valueChanged.connect(self.updateLabel)

        self.label = QLabel('0', self)

        hbox.addWidget(sbox)
        hbox.addSpacing(15)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QSpinBox')
        self.show()

    def updateLabel(self, value):

        self.label.setText(str(value))


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
