from PyQt5 import QtWidgets
from game import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
x=0
y=0
j=8
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonText1.clicked.connect(self.btnClicked1)
        self.ui.pushButtonText2.clicked.connect(self.btnClicked2)
        self.ui.pushButtonText3.clicked.connect(self.btnClicked3)
        self.ui.pushButtonText4.clicked.connect(self.btnClicked4)
        self.ui.pushButtonText5.clicked.connect(self.btnClicked5)
        self.ui.pushButtonText6.clicked.connect(self.btnClicked6)
        self.ui.pushButtonText7.clicked.connect(self.btnClicked7)
        self.ui.pushButtonText8.clicked.connect(self.btnClicked8)
        self.ui.pushButton_level_1.clicked.connect(self.start_level1)
    def start_level1(self):
        g=[1,3,5,6]
        h=[2,4,7,8]
        self.ui.pushButtonText1.show()
        self.ui.pushButtonText2.show()
        self.ui.pushButtonText3.show()
        self.ui.pushButtonText4.show()
        self.ui.pushButtonText5.show()
        self.ui.pushButtonText6.show()
        self.ui.pushButtonText7.show()
        self.ui.pushButtonText8.show()
        self.ui.pushButtonText1.setText('ждать')
        self.ui.pushButtonText2.setText('дожидаться')
        self.ui.pushButtonText3.setText('флора')
        self.ui.pushButtonText4.setText('растительность')
        self.ui.pushButtonText5.setText('союз')
        self.ui.pushButtonText6.setText('быт')
        self.ui.pushButtonText7.setText('альянс')
        self.ui.pushButtonText8.setText('повседневность')
        self.ui.label_errors.setText('3')
        self.ui.label_number_of_level.setText('1 уровень')
        j=8
    def btnClicked1(self):
         if x==0:
            x=1
            z=z-1
         else:
            y=1
            z=z-1
            for i in range(0,3):
               if x==g(i) and y==h(i):
                   j=j-2
                   x=0
                   y=0
         self.ui.pushButtonText1.hide()
    def btnClicked2(self):
        if x==0:
            x=2
        else:
            y=2
        self.ui.pushButtonText2.hide()
    def btnClicked3(self):
        if x==0:
            x=3
        else:
            y=3
        self.ui.pushButtonText3.hide()
    def btnClicked4(self):
        if x==0:
            x=4
        else:
            y=4
        self.ui.pushButtonText4.hide()
    def btnClicked5(self):
        if x==0:
            x=5
        else:
            y=5
        self.ui.pushButtonText5.hide()
    def btnClicked6(self):
        if x==0:
            x=6
        else:
            y=6
        self.ui.pushButtonText6.hide()
    def btnClicked7(self):
        if x==0:
            x=7
        else:
            y=7
        self.ui.pushButtonText7.hide()
    def btnClicked8(self):
        if x==0:
            x=8
        else:
            y=8
        self.ui.pushButtonText8.hide()
    
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())

