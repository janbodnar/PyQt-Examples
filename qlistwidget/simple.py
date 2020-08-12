#!/usr/bin/python

import sys
from PyQt5.QtWidgets import (QListWidget, QWidget, QMessageBox, 
    QApplication, QVBoxLayout)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        listWidget = QListWidget(self)
            
        listWidget.addItem("sparrow") 
        listWidget.addItem("robin")
        listWidget.addItem("crow")
        listWidget.addItem("raven")
        listWidget.addItem("woodpecker")
        listWidget.addItem("hummingbird")
            
        listWidget.itemDoubleClicked.connect(self.onClicked)
        
        vbox.addWidget(listWidget)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QListWidget')
        self.show()

    def onClicked(self, item):

        QMessageBox.information(self, "Info", item.text())


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
