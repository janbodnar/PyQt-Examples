#!/usr/bin/python

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLineEdit,
                             QWidget)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout()

        combo = QComboBox(self)
        combo.addItem('Left')
        combo.addItem('Center')
        combo.addItem('Right')

        combo.activated[str].connect(self.onActivated)

        self.qle = QLineEdit(self)

        hbox.addWidget(combo)
        hbox.setSpacing(20)
        hbox.addWidget(self.qle)

        self.setLayout(hbox)

        self.setWindowTitle('Text alignment')
        self.show()


    def onActivated(self, text):

        if text == 'Left':
            self.qle.setAlignment(Qt.AlignLeft)
        elif text == 'Center':
            self.qle.setAlignment(Qt.AlignCenter)
        else:
            self.qle.setAlignment(Qt.AlignRight)


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
