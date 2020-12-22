import sys
from PyQt5.QtWidgets import ( QApplication, QWidget, QToolTip, QPushButton )
from PyQt5.QtGui import ( QIcon, QFont )
from PyQt5.QtCore import QCoreApplication

class Example( QWidget ):

    def __init__( self ):
        super().__init__()

        self.unitUI()


    def unitUI( self ):

        QToolTip.setFont( QFont('SansSerif',10) )
        self.setToolTip( 'This is a <b>QWidget</b> widget' )

        btn = QPushButton( 'Button',self )
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(440,200)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect( QCoreApplication.instance().quit )
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(440,300)

        self.setGeometry( 300, 300, 1000, 500 )
        self.setWindowTitle( 'XXX' )
        self.setWindowIcon(QIcon( "D:\python-projects_Not_Git\интерфейс\skull.png" ))

        self.show()


if __name__ == '__main__':

    app = QApplication( sys.argv )
    ex = Example()
    sys.exit( app.exec_() )
