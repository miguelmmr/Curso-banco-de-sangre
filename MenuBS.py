import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget
from PyQt5.QtGui import QFont
#from PyQt5.QtCore import QTimer ,QDateTime

import random

c= random.randint(0,15)
s= random.randint(0,3)
#t=1
p1=0
p2=0
h1=0
h2=0

class UIWindow(object):
    
    # def tick(self):
    #     global t
    #     self.tlabel.setText(str(t))
    #     t=t+1
    # def showTime(self):
    #     time=QDateTime.currentDateTime()
    #     timeDisplay=time.toString('yyyy-MM-dd hh:mm:ss dddd')
    #     self.tlabel.setText(timeDisplay)
    
    def setupUI(self, MainWindow):
        
             
        MainWindow.setObjectName("Banco de Sangre")
        MainWindow.resize(850, 380)
        #self.setStyleSheet("background-color: yellow;") 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MenuLabel = QtWidgets.QLabel(self.centralwidget)
        self.MenuLabel.setGeometry(QtCore.QRect(370, 110, 111, 51))
        self.MenuLabel.setTextFormat(QtCore.Qt.RichText)
        self.MenuLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MenuLabel.setFont(QFont('Arial font', 13))
        self.MenuLabel.setObjectName("MenuLabel")
        
        self.Option1Button = QtWidgets.QPushButton(self.centralwidget)
        self.Option1Button.setGeometry(QtCore.QRect(290, 200, 85, 50))
        self.Option1Button.setFont(QFont('Arial font', 13))
        self.Option1Button.setObjectName("Option1Button")
        
        self.Option2Button = QtWidgets.QPushButton(self.centralwidget)
        self.Option2Button.setFont(QFont('Arial font', 13))
        self.Option2Button.setGeometry(QtCore.QRect(470, 200, 85, 50))
        self.Option2Button.setObjectName("Option2Button")
                
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Banco de Sangre"))
        self.MenuLabel.setText(_translate("MainWindow", "Menu"))
        self.Option1Button.setText(_translate("MainWindow", "Sin RH"))
        self.Option2Button.setText(_translate("MainWindow", "Con RH"))
        
    

class Ui_Option2(object):
    
    # def tick(self):
    #     global t
    #     self.tlabel.setText(str(t))
    #     t=t+1
    def sum_point(self):
        global p2
        global h2
        p2=p2+1
        self.plabel.setText('Racha actual: '+ str(p2) ) 
        if h2 < p2:
            h2=h2+1
            self.hlabel.setText('High score: '+ str(h2) )                 
        
    def break_streak(self):
        global p2
        p2=0
        self.plabel.setText('Racha actual: '+ str(p2) ) 
            
    def show_image(self):
        global c
        if c==0:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/a+p.jpg"))
        elif c==1:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/a-p.jpg"))
        elif c==2:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/b+p.jpg"))
        elif c==3:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/b-p.jpg"))
        elif c==4:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/ab+p.jpg"))
        elif c==5:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/ab-p.jpg"))
        elif c==6:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/o+p.jpg"))
        elif c==7:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/o-p.jpg"))
        elif c==8:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/a+copia.jpg"))
        elif c==9:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/a-copia.jpg"))
        elif c==10:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/b+copia.jpg"))
        elif c==11:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/b-copia.jpg"))
        elif c==12:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/ab+copia.jpg"))
        elif c==13:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/ab-copia.jpg"))
        elif c==14:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/o+copia.jpg"))
        elif c==15:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/o-copia.jpg"))        
    
    def setupUI(self, MainWindow):
               
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # self.tlabel = QtWidgets.QLabel(self.centralwidget)
        # self.tlabel.setText('0000000000')
        # self.timer=QTimer()
        # self.timer.timeout.connect(self.tick)
        # self.timer.start(1000)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(225, 0, 391, 231))
        self.label.setText("")
        
        self.plabel = QtWidgets.QLabel(self.centralwidget)
        self.plabel.setGeometry(QtCore.QRect(5, 60,215, 50))
        self.plabel.setFont(QFont('Arial font', 11))
        self.plabel.setText('Racha actual: '+ str(p2) ) 
        
        self.hlabel = QtWidgets.QLabel(self.centralwidget)
        self.hlabel.setGeometry(QtCore.QRect(5, 25,215, 50))
        self.hlabel.setFont(QFont('Arial font', 11))
        self.hlabel.setText('High score: '+ str(h2) )         
        
        
        self.show_image()
            
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(700, 50, 75, 23))
        self.back.setFont(QFont('Arial font', 10))
        self.back.setObjectName("back")                
        
        self.aplus = QtWidgets.QPushButton(self.centralwidget)
        self.aplus.setGeometry(QtCore.QRect(155, 260, 75, 23))
        self.aplus.setFont(QFont('Arial font', 11))
        self.aplus.setObjectName("aplus")
        self.aminus = QtWidgets.QPushButton(self.centralwidget)
        self.aminus.setGeometry(QtCore.QRect(155, 300, 75, 23))
        self.aminus.setFont(QFont('Arial font', 11))
        self.aminus.setObjectName("aminus")
        self.bplus = QtWidgets.QPushButton(self.centralwidget)
        self.bplus.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.bplus.setFont(QFont('Arial font', 11))
        self.bplus.setObjectName("bplus")
        self.bminus = QtWidgets.QPushButton(self.centralwidget)
        self.bminus.setGeometry(QtCore.QRect(300, 300, 75, 23))
        self.bminus.setFont(QFont('Arial font', 11))
        self.bminus.setObjectName("bminus")
        self.abplus = QtWidgets.QPushButton(self.centralwidget)
        self.abplus.setGeometry(QtCore.QRect(445, 260, 75, 23))
        self.abplus.setFont(QFont('Arial font', 11))
        self.abplus.setObjectName("abplus")
        self.abminus = QtWidgets.QPushButton(self.centralwidget)
        self.abminus.setGeometry(QtCore.QRect(445, 300, 75, 23))
        self.abminus.setFont(QFont('Arial font', 11))
        self.abminus.setObjectName("abminus")
        self.oplus = QtWidgets.QPushButton(self.centralwidget)
        self.oplus.setGeometry(QtCore.QRect(590, 260, 75, 23))
        self.oplus.setFont(QFont('Arial font', 11))
        self.oplus.setObjectName("oplus")
        self.ominus = QtWidgets.QPushButton(self.centralwidget)
        self.ominus.setGeometry(QtCore.QRect(590, 300, 75, 23))
        self.ominus.setFont(QFont('Arial font', 11))
        self.ominus.setObjectName("ominus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.aplus.clicked.connect(self.press_aplus)
        self.aminus.clicked.connect(self.press_aminus)
        self.bplus.clicked.connect(self.press_bplus)
        self.bminus.clicked.connect(self.press_bminus)
        self.abplus.clicked.connect(self.press_abplus)
        self.abminus.clicked.connect(self.press_abminus)
        self.oplus.clicked.connect(self.press_oplus)
        self.ominus.clicked.connect(self.press_ominus)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Banco de Sangre"))
        self.aplus.setText(_translate("MainWindow", "A+"))
        self.aminus.setText(_translate("MainWindow", "A-"))
        self.bplus.setText(_translate("MainWindow", "B+"))
        self.bminus.setText(_translate("MainWindow", "B-"))
        self.abplus.setText(_translate("MainWindow", "AB+"))
        self.abminus.setText(_translate("MainWindow", "AB-"))
        self.oplus.setText(_translate("MainWindow", "O+"))
        self.ominus.setText(_translate("MainWindow", "O-"))
        self.back.setText(_translate("MainWindow", "Menu"))

    def press_aplus(self):
        global c
        if c ==0 or c==8:
            self.sum_point()
            c= random.randint(0,15)
            while c==0 or c==8:
                c= random.randint(0,15)
            self.show_image()
        else:
            self.break_streak()
        
    def press_aminus(self):
        global c
        if c ==1 or c==9:
            self.sum_point()
            c= random.randint(0,15)
            while c==1 or c==9:
                c= random.randint(0,15)
            self.show_image()
        else:
            self.break_streak()            
                
    def press_bplus(self):
        global c
        if c ==2 or c==10:
            self.sum_point()
            c= random.randint(0,15)
            while c==2 or c==10:
                c= random.randint(0,15)
            self.show_image()
        else:
            self.break_streak()      
            
    def press_bminus(self):
        global c
        if c==3 or c==11:
            self.sum_point()
            c= random.randint(0,15)
            while c==3 or c==11:
                c= random.randint(0,15)
            self.show_image()
        else:
            self.break_streak()          
            
    def press_abplus(self):
        global c
        if c ==4 or c==12:
            self.sum_point()
            c= random.randint(0,15)
            while c==4 or c==12:
                c= random.randint(0,15)
            self.show_image()
        else:
            self.break_streak()          
            
    def press_abminus(self):
        global c
        if c ==5 or c==13:
            self.sum_point()
            c= random.randint(0,15)
            while c==5 or c==13:
                c= random.randint(0,15)
            self.show_image()
        else:
            self.break_streak()                
                
    def press_oplus(self):
        global c
        if c ==6 or c==14:
            self.sum_point()
            c= random.randint(0,15)
            while c==6 or c==14:
                c= random.randint(0,15)
            self.show_image()
        else:
            self.break_streak()                
                
    def press_ominus(self):
        global c
        if c ==7 or c==15:
            self.sum_point()
            c= random.randint(0,15)
            while c==7 or c==15:
                c= random.randint(0,15)
            self.show_image()
        else:
            self.break_streak()


class Ui_Option1(object):
    
    def sum_point(self):
        global p1
        global h1
        p1=p1+1
        self.plabel.setText('Racha actual: '+ str(p1) ) 
        if h1 < p1:
            h1=h1+1
            self.hlabel.setText('High score: '+ str(h1) )                 
        
    def break_streak(self):
        global p1
        p1=0
        self.plabel.setText('Racha actual: '+ str(p1) ) 
        
    def show_image(self):
        global s
        if s==0:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/a.jpg"))
        elif s==1:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/b.jpg"))
        elif s==2:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/ab.jpg"))
        elif s==3:
            self.label.setPixmap(QtGui.QPixmap("Imagenes/o.jpg"))        
    
    
    def setupUI(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 0, 451, 231))
        self.label.setText("")
        
        self.show_image()
            
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.plabel = QtWidgets.QLabel(self.centralwidget)
        self.plabel.setGeometry(QtCore.QRect(5, 60,195, 50))
        self.plabel.setFont(QFont('Arial font', 11))
        self.plabel.setText('Racha actual: '+ str(p1) ) 
        
        self.hlabel = QtWidgets.QLabel(self.centralwidget)
        self.hlabel.setGeometry(QtCore.QRect(5, 25,195, 50))
        self.hlabel.setFont(QFont('Arial font', 11))
        self.hlabel.setText('High score: '+ str(h1) ) 
        
        self.dlabel = QtWidgets.QLabel(self.centralwidget)
        self.dlabel.setGeometry(QtCore.QRect(670, 75,140, 120))
        self.dlabel.setFont(QFont('Bauhaus 93', 10))
        self.dlabel.setText('Grupos sanguíneos \ncon control salino \nen la primera gota ' ) 
        
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(700, 50, 75, 23))
        self.back.setFont(QFont('Times font', 10))
        self.back.setObjectName("back")                   
        
        self.a = QtWidgets.QPushButton(self.centralwidget)
        self.a.setGeometry(QtCore.QRect(290, 260, 75, 23))
        self.a.setFont(QFont('Arial font', 11))
        self.a.setObjectName("a")
        self.b = QtWidgets.QPushButton(self.centralwidget)
        self.b.setGeometry(QtCore.QRect(290, 300, 75, 23))
        self.b.setFont(QFont('Arial font', 11))
        self.b.setObjectName("b")
        self.ab = QtWidgets.QPushButton(self.centralwidget)
        self.ab.setGeometry(QtCore.QRect(420, 260, 75, 23))
        self.ab.setFont(QFont('Arial font', 11))
        self.ab.setObjectName("ab")
        self.o = QtWidgets.QPushButton(self.centralwidget)
        self.o.setGeometry(QtCore.QRect(420, 300, 75, 23))
        self.o.setFont(QFont('Arial font', 11))
        self.o.setObjectName("o")
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.a.clicked.connect(self.press_a)
        self.b.clicked.connect(self.press_b)
        self.ab.clicked.connect(self.press_ab)
        self.o.clicked.connect(self.press_o)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Banco de Sangre"))
        self.a.setText(_translate("MainWindow", "A"))
        self.b.setText(_translate("MainWindow", "B"))
        self.ab.setText(_translate("MainWindow", "AB"))
        self.o.setText(_translate("MainWindow", "O"))
        self.back.setText(_translate("MainWindow", "Menu"))


    def press_a(self):
        global s
        if s ==0:
            self.sum_point()
            s= random.randint(0,3)
            while s==0:
                s= random.randint(0,3)
            self.show_image()
        else:
            self.break_streak()

        
    def press_b(self):
        global s
        if s ==1:
            self.sum_point()
            s = random.randint(0,3)
            while s==1:
                s= random.randint(0,3)
            self.show_image()
        else:
            self.break_streak()

                
    def press_ab(self):
        global s
        if s ==2:
            self.sum_point()
            s= random.randint(0,3)
            while s ==2:
                s = random.randint(0,3)
            self.show_image()
        else:
            self.break_streak()

            
    def press_o(self):
        global s
        if s==3:
            self.sum_point()
            s= random.randint(0,3)
            while s==3:
                s= random.randint(0,3)
            self.show_image()
        else:
            self.break_streak()
            


class UI_CloseWindow(object):
    
    def setupUI(self, MainWindow):
        
             
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 282)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MenuLabel = QtWidgets.QLabel(self.centralwidget)
        self.MenuLabel.setGeometry(QtCore.QRect(260, 30, 111, 51))
        self.MenuLabel.setTextFormat(QtCore.Qt.RichText)
        self.MenuLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MenuLabel.setObjectName("MenuLabel")
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MenuLabel.setText(_translate("MainWindow", str(p2)))

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setStyleSheet("background-color: cyan;") 
        self.uiWindow = UIWindow()
        
        self.uioption2 = Ui_Option2()
        self.uioption1 = Ui_Option1() 
        self.uiclosewin = UI_CloseWindow()
        self.startUIWindow()
        
    def startUICloseWin(self):
        self.uiclosewin.setupUI(self)
        self.show()
    
    def startUIOption2(self):
        global t
        self.uioption2.setupUI(self)
        self.uioption2.back.clicked.connect(self.startUIWindow)
        self.show()
        
    def startUIOption1(self):
        self.uioption1.setupUI(self)
        self.uioption1.back.clicked.connect(self.startUIWindow)
        self.show()

    def startUIWindow(self):
        self.uiWindow.setupUI(self)
        self.uiWindow.Option2Button.clicked.connect(self.startUIOption2)
        self.uiWindow.Option1Button.clicked.connect(self.startUIOption1)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
