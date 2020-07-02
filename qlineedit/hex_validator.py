#!/usr/bin/python

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QSizePolicy,
    QHBoxLayout, QApplication)
from PyQt5.QtGui import QRegExpValidator, QPalette, QColor
from PyQt5.QtCore import QRegExp


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout()

        label = QLabel('HEX colour:', self)

        self.qle = QLineEdit(self)
        validator = QRegExpValidator(QRegExp("[0-9A-Fa-f]{6}"))
        self.qle.setValidator(validator)

        self.qle.editingFinished.connect(self.onEditingFinished)

        self.colLabel = QLabel(self)
        self.colLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.colLabel.setAutoFillBackground(True)

        hbox.addWidget(label)
        hbox.addSpacing(20)
        hbox.addWidget(self.qle)
        hbox.addSpacing(20)

        hbox.addWidget(self.colLabel)
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor('#333333'))
        self.colLabel.setPalette(pal)

        self.setLayout(hbox)
        self.resize(450, 200)
        self.setWindowTitle('Validator')
        self.show()

    def onEditingFinished(self):

        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(f'#{self.qle.text()}'))
        self.colLabel.setPalette(pal)


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
