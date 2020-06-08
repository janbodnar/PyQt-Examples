#!/usr/bin/python


import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QGridLayout
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        grid = QGridLayout()

        lbl1 = QLabel()
        lbl1.setStyleSheet("background-color:firebrick; border-radius:5px")

        lbl2 = QLabel()
        lbl2.setStyleSheet("background-color:gold; border-radius:5px")
        
        lbl3 = QLabel()
        lbl3.setStyleSheet("background-color:seagreen; border-radius:5px")

        lbl4 = QLabel()
        lbl4.setStyleSheet("background-color:royalblue; border-radius:5px")

        lbl5 = QLabel()
        lbl5.setStyleSheet("background-color:crimson; border-radius:5px")

        lbl6 = QLabel()
        lbl6.setStyleSheet("background-color:salmon; border-radius:5px")

        lbl7 = QLabel()
        lbl7.setStyleSheet("background-color:deeppink; border-radius:5px")

        lbl8 = QLabel()
        lbl8.setStyleSheet("background-color:tomato; border-radius:5px")

        lbl9 = QLabel()
        lbl9.setStyleSheet("background-color:darkkhaki; border-radius:5px")

        lbl10 = QLabel()
        lbl10.setStyleSheet("background-color:cornflowerblue; border-radius:5px")

        lbl11 = QLabel()
        lbl11.setStyleSheet("background-color:rosybrown; border-radius:5px")

        lbl12 = QLabel()
        lbl12.setStyleSheet("background-color:chocolate; border-radius:5px")

        lbl13 = QLabel()
        lbl13.setStyleSheet("background-color:slategray; border-radius:5px")

        grid.addWidget(lbl1, 0, 0)
        grid.addWidget(lbl2, 0, 1)
        grid.addWidget(lbl3, 0, 2)
        grid.addWidget(lbl4, 0, 3)
        grid.addWidget(lbl5, 1, 0)
        grid.addWidget(lbl6, 1, 1)
        grid.addWidget(lbl8, 1, 2)
        grid.addWidget(lbl9, 1, 3)
        grid.addWidget(lbl10, 2, 0)
        grid.addWidget(lbl11, 2, 1)
        grid.addWidget(lbl12, 2, 2)
        grid.addWidget(lbl13, 2, 3)

        self.setLayout(grid)

        self.setGeometry(300, 300, 420, 200)
        self.setWindowTitle('Colours')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
