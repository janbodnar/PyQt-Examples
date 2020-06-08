#!/usr/bin/python

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QHBoxLayout
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        
        hbox = QHBoxLayout()

        link = QLabel('<a href="http://zetcode.com">zetcode.com</a>')
        link.setOpenExternalLinks(True)

        hbox.addWidget(link)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('HTML link')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
