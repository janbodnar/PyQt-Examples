#!/usr/bin/python


from PyQt5.QtWidgets import (QWidget, QSpinBox, QHBoxLayout, QMessageBox,
                             QPushButton, QApplication, QSizePolicy)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout()

        self.sbox = QSpinBox(self)

        btn = QPushButton('Show', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.clicked.connect(self.showSpinboxValue)

        hbox.addWidget(self.sbox)
        hbox.addSpacing(15)
        hbox.addWidget(btn)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QSpinBox')
        self.show()

    def showSpinboxValue(self):

        val = self.sbox.value()
        QMessageBox.information(self, 'Value', f'Value: {val}')


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
