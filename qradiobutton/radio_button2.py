#!/usr/bin/python


from PyQt5.QtWidgets import (QWidget, QRadioButton, QHBoxLayout, QVBoxLayout,
                             QButtonGroup, QLabel, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()

        bg1 = QButtonGroup(self)

        rb1 = QRadioButton("Large", self)
        rb1.toggled.connect(self.updateLabel1)

        rb2 = QRadioButton("Middle", self)
        rb2.toggled.connect(self.updateLabel1)

        rb3 = QRadioButton("Small", self)
        rb3.toggled.connect(self.updateLabel1)


        hbox2 = QHBoxLayout()
        bg2 = QButtonGroup(self)

        rb4 = QRadioButton("Red", self)
        rb4.toggled.connect(self.updateLabel2)

        rb5 = QRadioButton("Green", self)
        rb5.toggled.connect(self.updateLabel2)

        rb6 = QRadioButton("Blue", self)
        rb6.toggled.connect(self.updateLabel2)

        self.label1 = QLabel('', self)
        self.label2 = QLabel('', self)

        bg1.addButton(rb1)
        bg1.addButton(rb2)
        bg1.addButton(rb3)

        bg2.addButton(rb4)
        bg2.addButton(rb5)
        bg2.addButton(rb6)

        hbox1.addWidget(rb1)
        hbox1.addWidget(rb2)
        hbox1.addWidget(rb3)

        hbox2.addWidget(rb4)
        hbox2.addWidget(rb5)
        hbox2.addWidget(rb6)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QRadioButton')
        self.show()

    def updateLabel1(self, value):

        rbtn = self.sender()

        if rbtn.isChecked() == True:
            self.label1.setText(rbtn.text())

    def updateLabel2(self, value):

        rbtn = self.sender()

        if rbtn.isChecked() == True:
            self.label2.setText(rbtn.text())


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
