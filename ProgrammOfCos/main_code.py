import sys
import math
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*

def theoremCos(side1,side2,corner,sideOut,corner1,corner2):
    firstSide = int(side1.text())
    secondSide = int(side2.text())
    Corner = (int(corner.text())*math.pi/180)
    output = str(round((firstSide**2 + secondSide**2 - (2*firstSide*secondSide*math.cos(Corner)))**0.5,1))
    cornerA = math.cos((secondSide**2+int(output)**2-firstSide**2)/(2*secondSide*int(output)))
    cornerB = 180-int(corner.text())-cornerA
    sideOut.setText(f'{output}')
    cornerA.setText(f'{cornerA}')
    cornerB.setText(f'{cornerB}')

class Example( QWidget ):

    def __init__( self ):
        super().__init__()

        self.unitUI()

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    # triangle
    def drawLines(self, qp):

        pen = QPen(Qt.black, 2, Qt.SolidLine)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(250, 350, 650, 350)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(500, 100, 250, 350)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(500, 100, 650, 350)


    # graphical interface
    def unitUI( self ):

        QToolTip.setFont( QFont('SansSerif',10) )
        self.setToolTip( 'This is a <b>QWidget</b> widget' )

        # input sides and corners of triangle
        sideA = QLineEdit(self)
        sideA.move(440, 360)
        sideA.resize(60, 30)

        sideB = QLineEdit(self)
        sideB.move(300, 200)
        sideB.resize(60, 30)

        sideC = QLineEdit(self)
        sideC.move(590, 200)
        sideC.resize(60, 30)

        cornerF = QLineEdit(self)
        cornerF.move(475, 130)
        cornerF.resize(40, 30)

        cornerE = QLineEdit(self)
        cornerE.move(590, 315)
        cornerE.resize(40, 30)

        cornerG = QLineEdit(self)
        cornerG.move(290, 315)
        cornerG.resize(40, 30)

        def function():
            if sideB.text().strip() and sideA.text().strip() and cornerG.text().strip():
                 theoremCos(sideB,sideA,cornerG,sideC,cornerE,cornerF)

            elif sideB.text().strip() and sideC.text().strip() and cornerF.text().strip():
                 theoremCos(sideB,sideC,cornerF,sideA)

            elif sideC.text().strip() and sideA.text().strip() and cornerE.text().strip():
                theoremCos(sideC,sideA,cornerE,sideB)


        btn = QPushButton( 'найти сторону',self )
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(20,320)
        btn.clicked.connect(function)


        qbtn = QPushButton('Выйти', self)
        qbtn.clicked.connect( QCoreApplication.instance().quit )
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(20,360)

        #icon and size of window
        self.setGeometry( 300, 300, 1000, 500 )
        self.setWindowTitle( 'XXX' )
        self.setWindowIcon(QIcon( "D:\python-projects_Not_Git\интерфейс\skull.png" ))

        self.show()

if __name__ == '__main__':

    app = QApplication( sys.argv )
    ex = Example()
    sys.exit( app.exec_() )
