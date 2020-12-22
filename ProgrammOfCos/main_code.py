import sys
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


    def drawLines(self, qp):
    # triangle
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

        cornerA = QLineEdit(self)
        cornerA.move(475, 130)
        cornerA.resize(40, 30)

        cornerB = QLineEdit(self)
        cornerB.move(590, 315)
        cornerB.resize(40, 30)

        cornerC = QLineEdit(self)
        cornerC.move(290, 315)
        cornerC.resize(40, 30)



        btn = QPushButton( 'найти сторону',self )
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(20,320)

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
