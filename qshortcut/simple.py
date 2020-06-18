#!/usr/bin/python


from PyQt5.QtWidgets import QWidget, QShortcut, QApplication, QMessageBox
from PyQt5.QtGui import QKeySequence
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.msgSc = QShortcut(QKeySequence('Ctrl+M'), self)

        self.msgSc.activated.connect(lambda : QMessageBox.information(self,
            'Message', 'Ctrl + M initiated'))

        self.quitSc = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.quitSc.activated.connect(QApplication.instance().quit)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Shortcuts')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
