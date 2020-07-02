#!/usr/bin/python

import sys
from PyQt5.QtWidgets import (QWidget, QComboBox, QPushButton, QLineEdit, 
    QHBoxLayout, QApplication, QMessageBox)
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout()

        combo = QComboBox(self)
        combo.addItem('Normal')
        combo.addItem('Password')
        combo.addItem('PasswordEchoOnEdit')
        combo.addItem('NoEcho')

        combo.activated[str].connect(self.onActivated)

        self.qle = QLineEdit(self)

        showBtn = QPushButton('Show', self)
        showBtn.clicked.connect(self.onClicked)

        hbox.addWidget(combo)
        hbox.setSpacing(20)
        hbox.addWidget(self.qle)
        hbox.setSpacing(20)
        hbox.addWidget(showBtn)

        self.setLayout(hbox)

        self.setWindowTitle('Echo mode')
        self.show()


    def onActivated(self, text):

        if text == 'Normal':
            self.qle.setEchoMode(QLineEdit.EchoMode.Normal)
        elif text == 'Password':
            self.qle.setEchoMode(QLineEdit.EchoMode.Password)
        elif text == 'PasswordEchoOnEdit':
            self.qle.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        elif text == 'NoEcho':
            self.qle.setEchoMode(QLineEdit.EchoMode.NoEcho)


    def onClicked(self):

        text = self.qle.text()
        QMessageBox.information(self, 'info', text)


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
