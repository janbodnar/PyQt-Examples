#!/usr/bin/python

import sys
from PyQt5.QtWidgets import (QHBoxLayout, QPushButton, QWidget, 
    QApplication, QVBoxLayout, QMessageBox)
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout()

        self.webEngineView = QWebEngineView()
        self.loadPage()

        expBtn = QPushButton('Export', self)
        expBtn.clicked.connect(self.onClicked)

        hbox.addWidget(expBtn)

        vbox.addWidget(self.webEngineView)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QWebEngineView')
        self.show()

    def onClicked(self):

        self.webEngineView.page().printToPdf('myfile.pdf')
        QMessageBox.information(self, 'info', 'page exported')

    def loadPage(self):

        with open('test.html', 'r') as f:

            html = f.read()
            self.webEngineView.setHtml(html)

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
