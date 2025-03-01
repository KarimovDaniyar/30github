from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class GayWindow(QMainWindow):
    def __init__(self):
        super(GayWindow, self).__init__()
        
        self.setWindowTitle("Yopta")
        self.setGeometry(300, 250, 350, 250)
        
        self.n_text = QtWidgets.QLabel(self)
        
        
        text = QtWidgets.QLabel(self)
        text.setText("WHY ARE YOU GAY ??? ")
        text.move(100, 100)
        text.adjustSize()
        
        self.knopka = QtWidgets.QPushButton(self)
        self.knopka.move(70, 150)
        self.knopka.setText("I'm not  gay")
        self.knopka.setFixedWidth(200)
        self.knopka.clicked.connect(self.add_label2)
        
        self.knopka2 = QtWidgets.QPushButton(self)
        self.knopka2.setText("I'm gay")
        self.knopka2.move(70, 200)
        self.knopka2.setFixedWidth(200)
        self.knopka2.clicked.connect(self.add_label)
    
            
    def add_label(self):
        self.n_text.setText("I'm also :-) ")
        self.n_text.move(100,50)
        self.n_text.adjustSize()

    def add_label2(self):
        self.n_text.setText("Don't worry , soon you join ass (us) ")
        self.n_text.move(100,50)
        self.n_text.adjustSize()
    
def application():
    app = QApplication(sys.argv)
    window = GayWindow()
    
    window.show()
    sys.exit(app.exec_())
   
 
application()