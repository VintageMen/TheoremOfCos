import sys
import math
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*

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

        label = QLabel(self)
        label.move(10,50)
        label.resize(500,50)
        label.setText("ПРОТИВОПОЛОЖНАЯ СТОРОНА:")
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
                side1 = int(sideB.text())
                side2 = int(sideA.text())
                corner = (int(cornerG.text())*math.pi/180)

             elif sideB.text().strip() and sideC.text().strip() and cornerF.text().strip():
                side1 = int(sideB.text())
                side2 = int(sideC.text())
                corner = (int(cornerF.text())*math.pi/180)

             elif sideC.text().strip() and sideA.text().strip() and cornerE.text().strip():
                 side1 = int(sideC.text())
                 side2 = int(sideA.text())
                 corner = (int(cornerE.text())*math.pi/180)

             output = str((side1**2 + side2**2 - (2*side1*side2*math.cos(corner)))**0.5)
             label.setText(f'ПРОТИВОПОЛОЖНАЯ СТОРОНА = {output}')

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
