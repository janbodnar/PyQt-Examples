#!/usr/bin/python


from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QApplication, 
    QPushButton, QMessageBox, QSizePolicy)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout()

        msgBtn = QPushButton('&Show message', self)
        msgBtn.clicked.connect(lambda : QMessageBox.information(self, 
            'Message', 'Information message'))

        hbox.addWidget(msgBtn)
        msgBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        hbox.setAlignment(Qt.AlignLeft)

        self.setLayout(hbox)

        self.move(300, 300)
        self.setWindowTitle('Shortcuts')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
