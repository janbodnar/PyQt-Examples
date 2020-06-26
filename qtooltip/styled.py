#!/usr/bin/python

import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QApplication
from PyQt5.QtGui import QFont, QPalette, QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setStyleSheet('''QToolTip { 
                           background-color: #8ad4ff; 
                           color: black; 
                           border: #8ad4ff solid 1px
                           }''')

        QToolTip.setFont(QFont('Georgia', 11))
        
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor('#348ceb'))
        self.setPalette(pal)

        self.setToolTip('This is QWidget')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Styled QToolTip')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
