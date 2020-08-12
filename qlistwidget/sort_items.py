#!/usr/bin/python

import sys
from PyQt5.QtWidgets import (QCheckBox, QListWidget, QPushButton, QWidget, 
    QHBoxLayout, QApplication, QVBoxLayout)
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout()

        self.listWidget = QListWidget(self)

        self.listWidget.addItems(['sparrow', 'robin', 'crow', 'raven',
            'woopecker', 'hummingbird'])

        self.sortOrder = QCheckBox('Ascending', self)

        sortBtn = QPushButton('Sort', self)
        sortBtn.clicked.connect(self.onSorted)

        vbox.addWidget(self.listWidget)
        hbox.addWidget(self.sortOrder)
        hbox.addWidget(sortBtn)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Sorting items')
        self.show()


    def onSorted(self):

        if self.sortOrder.isChecked():
            order = Qt.AscendingOrder
        else:
            order = Qt.DescendingOrder

        self.listWidget.sortItems(order)


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
