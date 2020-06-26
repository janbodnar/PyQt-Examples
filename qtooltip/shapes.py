#!/usr/bin/python

import sys

from PyQt5.QtCore import QEvent, QPoint, QPointF, Qt
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QPolygonF
from PyQt5.QtWidgets import QApplication, QToolTip, QWidget


class Shape(object):

    def __init__(self):

        self.mypath = QPainterPath()
        self.col  = QColor()
        self.toottip = ''

    def path(self):
        return self.mypath

    def color(self):
        return self.col

    def toolTip(self):
        return self.toottip

    def setPath(self, path):
        self.mypath = path

    def setToolTip(self, tooltip):
        self.toottip = tooltip

    def setPosition(self, position):
        self.pos = position

    def setColor(self, color):
        self.col = color


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.circlePath = QPainterPath()
        self.squarePath = QPainterPath()
        self.trianglePath = QPainterPath()
        self.pentagonPath = QPainterPath()
        self.shapes = []

        self.circlePath.addEllipse(30, 50, 100, 100)
        self.squarePath.addRect(180, 50, 100, 100)

        x = self.trianglePath.currentPosition().x()
        y = self.trianglePath.currentPosition().y()

        self.trianglePath.moveTo(320, 150)
        self.trianglePath.lineTo(450, 150)
        self.trianglePath.lineTo(415, 50)
        self.trianglePath.lineTo(320, 150)

        polygon = QPolygonF()
        polygon.append(QPoint(130,  240))
        polygon.append(QPoint(100,  280))
        polygon.append(QPoint(50,   280))
        polygon.append(QPoint(20,  240))
        polygon.append(QPoint(75,  200))

        self.pentagonPath.addPolygon(polygon)

        self.createShape(self.circlePath, 'Circle', QColor('#c72602'))
        self.createShape(self.squarePath, 'Square', QColor('#32a852'))
        self.createShape(self.trianglePath, 'Triangle', QColor('#205f6e'))
        self.createShape(self.pentagonPath, 'Pentagon', QColor('#e0b107'))

        self.setWindowTitle('Shapes')
        self.resize(480, 300)
        self.show()

    def event(self, e):

        if e.type() == QEvent.ToolTip:

            index = self.itemIndexAt(e.pos())

            if index != -1:
                QToolTip.showText(e.globalPos(),
                        self.shapes[index].toolTip())
            else:
                QToolTip.hideText()
                e.ignore()

            return True

        return super(Example, self).event(e)


    def paintEvent(self, e):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        for shape in self.shapes:

            painter.setBrush(shape.color())
            painter.drawPath(shape.path())


    def itemIndexAt(self, pos):

        for i in range(len(self.shapes)):

            item = self.shapes[i]

            if item.path().contains(QPointF(pos)):
                
                return i

        return -1


    def createShape(self, path, toolTip, color):

        shape = Shape()
        shape.setPath(path)
        shape.setToolTip(toolTip)
        shape.setColor(color)

        self.shapes.append(shape)
 

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
