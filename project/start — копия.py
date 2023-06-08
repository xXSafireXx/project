from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from game import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import playsound
with open('words.txt','r') as w:
    g=w.readline(0).split(',')
    h=w.readline(1).split(',')
with open('settings.txt','r+') as f:
 x=f.read()
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.player=QMediaPlayer(self)
        self.player.setVolume(int(x))
        media=QMediaContent(QUrl.fromLocalFile("game.mp3"))
        self.player.setMedia(media)
        self.player.play()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.ui.pushButtonText1.clicked.connect(self.btnClicked1)
        self.ui.pushButtonText2.clicked.connect(self.btnClicked2)
        self.ui.pushButtonText3.clicked.connect(self.btnClicked3)
        self.ui.pushButtonText4.clicked.connect(self.btnClicked4)
        self.ui.pushButtonText5.clicked.connect(self.btnClicked5)
        self.ui.pushButtonText6.clicked.connect(self.btnClicked6)
        self.ui.pushButtonText7.clicked.connect(self.btnClicked7)
        self.ui.pushButtonText8.clicked.connect(self.btnClicked8)
        self.ui.pb_proverka.clicked.connect(self.proverka)
        self.ui.pushButton_level_1.clicked.connect(self.start_level1)
        self.ui.pushButton_level_1.clicked.connect(self.start_level)
        self.ui.pushButton_level_1.clicked.connect(self.start_timer)
        
        self.ui.pushButton_level_2.clicked.connect(self.start_level2)
        self.ui.pushButton_level_2.clicked.connect(self.start_level)
        self.ui.pushButton_level_2.clicked.connect(self.start_timer)
        
        self.ui.pushButton_level_3.clicked.connect(self.start_level3)
        self.ui.pushButton_level_3.clicked.connect(self.start_level)
        self.ui.pushButton_level_3.clicked.connect(self.start_timer)
        
        self.ui.pushButton_level_4.clicked.connect(self.start_level4)
        self.ui.pushButton_level_4.clicked.connect(self.start_level)
        self.ui.pushButton_level_4.clicked.connect(self.start_timer)
        
        self.ui.pushButton_level_5.clicked.connect(self.start_level5)
        self.ui.pushButton_level_5.clicked.connect(self.start_level)
        self.ui.pushButton_level_5.clicked.connect(self.start_timer)
        self.ui.label_words.hide()
        self.ui.progressBarVolume.valueChanged.connect(self.player.setVolume)
        self.ui.progressBarVolume_2.valueChanged.connect(self.player.setVolume)
        self.ui.progressBarVolume.valueChanged.connect(self.saveVolume)
        self.ui.progressBarVolume_2.valueChanged.connect(self.saveVolume)
        self.ui.progressBarVolume.valueChanged.connect(self.ui.progressBarVolume_2.setValue)

    def saveVolume(self):
        with open('settings.txt','w') as f:
         f.write(str(self.player.volume()))
    def start_timer(self):
        self.timer.start(1000)   # запуск таймера с интервалом в 1 секунду
    def update_label(self):
        time = int(self.ui.label_time.text()) + 1   # увеличение времени на 1 секунду
        self.ui.label_time.setText(str(time))
    def start_level5(self):
        global g,h
        g=['модель','шутить','дом','сражение']
        h=['эталон','чудить','изба','бой']
        self.ui.label_number_of_level.setText('5 уровень')
    def start_level4(self):
        global g,h
        g=['грязный','тяжелый','смирный','неизвестный']
        h=['нечистый','весомый','послушный','незнакомый']
        self.ui.label_number_of_level.setText('4 уровень')
    def start_level3(self):
        global g,h
        g=['худой','смелый','забавный','злой']
        h=['тощий','храбрый','веселый','сердитый']
        self.ui.label_number_of_level.setText('3 уровень')
    def start_level2(self):
        global g,h
        g=['ветер','делать','красивый','глупо']
        h=['вихрь','создавать','симпатичный','неразумно']
        self.ui.label_number_of_level.setText('2 уровень') 
    def start_level1(self):
        global g,h
        g=['ждать','флора','союз','быт']
        h=['дожидаться','растительность','альянс','повседневность']
        self.ui.label_number_of_level.setText('1 уровень') 
    def start_level(self):
        global g
        global h
        self.ui.label_time.setText('0')
        self.ui.label_words.setText('8')
        self.ui.pushButtonText1.show()
        self.ui.pushButtonText2.show()
        self.ui.pushButtonText3.show()
        self.ui.pushButtonText4.show()
        self.ui.pushButtonText5.show()
        self.ui.pushButtonText6.show()
        self.ui.pushButtonText7.show()
        self.ui.pushButtonText8.show()
        self.ui.pushButtonText1.setText(g[0])
        self.ui.pushButtonText2.setText(h[0])
        self.ui.pushButtonText3.setText(g[1])
        self.ui.pushButtonText4.setText(g[2])
        self.ui.pushButtonText5.setText(h[1])
        self.ui.pushButtonText6.setText(g[3])
        self.ui.pushButtonText7.setText(h[2])
        self.ui.pushButtonText8.setText(h[3])
        self.ui.label_errors.setText('3')   
    def proverka(self):
            global g,h
            y=2
            x=int(self.ui.label_words.text())
            if self.ui.label_word_1.text()!='' and self.ui.label_word_2.text()!='':
                for i in range(0,len(g)):
                 if (self.ui.label_word_1.text()==g[i] and self.ui.label_word_2.text()==h[i]) or (self.ui.label_word_1.text()==h[i] and self.ui.label_word_2.text()==g[i]):
                   if self.ui.label_word_1.text()==self.ui.pushButtonText1.text() or self.ui.label_word_2.text()==self.ui.pushButtonText1.text():
                             self.ui.pushButtonText1.hide()
                             y=y-1
                             x=x-1
                 if (self.ui.label_word_1.text()==g[i] and self.ui.label_word_2.text()==h[i]) or (self.ui.label_word_1.text()==h[i] and self.ui.label_word_2.text()==g[i]):
                   if self.ui.label_word_1.text()==self.ui.pushButtonText2.text() or self.ui.label_word_2.text()==self.ui.pushButtonText2.text():
                             self.ui.pushButtonText2.hide()
                             y=y-1
                             x=x-1
                 if (self.ui.label_word_1.text()==g[i] and self.ui.label_word_2.text()==h[i]) or (self.ui.label_word_1.text()==h[i] and self.ui.label_word_2.text()==g[i]):
                   if self.ui.label_word_1.text()==self.ui.pushButtonText3.text() or self.ui.label_word_2.text()==self.ui.pushButtonText3.text():
                             self.ui.pushButtonText3.hide()
                             y=y-1
                             x=x-1
                 if (self.ui.label_word_1.text()==g[i] and self.ui.label_word_2.text()==h[i]) or (self.ui.label_word_1.text()==h[i] and self.ui.label_word_2.text()==g[i]):
                   if self.ui.label_word_1.text()==self.ui.pushButtonText4.text() or self.ui.label_word_2.text()==self.ui.pushButtonText4.text():
                             self.ui.pushButtonText4.hide()
                             y=y-1
                             x=x-1
                 if (self.ui.label_word_1.text()==g[i] and self.ui.label_word_2.text()==h[i]) or (self.ui.label_word_1.text()==h[i] and self.ui.label_word_2.text()==g[i]):
                   if self.ui.label_word_1.text()==self.ui.pushButtonText5.text() or self.ui.label_word_2.text()==self.ui.pushButtonText5.text():
                             self.ui.pushButtonText5.hide()
                             y=y-1
                             x=x-1
                 if (self.ui.label_word_1.text()==g[i] and self.ui.label_word_2.text()==h[i]) or (self.ui.label_word_1.text()==h[i] and self.ui.label_word_2.text()==g[i]):
                   if self.ui.label_word_1.text()==self.ui.pushButtonText6.text() or self.ui.label_word_2.text()==self.ui.pushButtonText6.text():
                             self.ui.pushButtonText6.hide()
                             y=y-1
                             x=x-1
                 if (self.ui.label_word_1.text()==g[i] and self.ui.label_word_2.text()==h[i]) or (self.ui.label_word_1.text()==h[i] and self.ui.label_word_2.text()==g[i]):
                   if self.ui.label_word_1.text()==self.ui.pushButtonText7.text() or self.ui.label_word_2.text()==self.ui.pushButtonText7.text():
                             self.ui.pushButtonText7.hide()
                             y=y-1
                             x=x-1
                 if (self.ui.label_word_1.text()==g[i] and self.ui.label_word_2.text()==h[i]) or (self.ui.label_word_1.text()==h[i] and self.ui.label_word_2.text()==g[i]):
                   if self.ui.label_word_1.text()==self.ui.pushButtonText8.text() or self.ui.label_word_2.text()==self.ui.pushButtonText8.text():
                             self.ui.pushButtonText8.hide()
                             y=y-1
                             x=x-1
                if y<2:
                       self.ui.label_word_1.setText('')
                       self.ui.label_word_2.setText('')
                       self.ui.label_words.setText(str(x))
                       exit
                else:
                     if self.ui.label_errors.text()!='1':
                      if self.ui.label_word_1.text()!='' or self.ui.label_word_2.text()!='':  
                        z=self.ui.label_errors.text()
                        z=int(z)-1
                        self.ui.label_errors.setText(str(z))
                        self.ui.label_word_1.setText('')
                        self.ui.label_word_2.setText('')
                      else:
                       self.ui.label_word_1.setText('')
                       self.ui.label_word_2.setText('')
                     else:
                        self.ui.widget_lose.show()
                        self.ui.widget_level.hide()
            if x==0:
                self.ui.label_time_win.setText('за '+self.ui.label_time.text()+" секунд")
                self.ui.widget_win.show()
                self.ui.widget_level.hide()
    def btnClicked1(self):
        global g,h
        if self.ui.label_word_1.text()!=g[0] and self.ui.label_word_2.text()!=g[0]:
          if self.ui.label_word_1.text()!='':
            self.ui.label_word_2.setText(g[0])
          else:
            self.ui.label_word_1.setText(g[0])
    def btnClicked2(self):
        global g,h
        if self.ui.label_word_1.text()!=h[0] and self.ui.label_word_2.text()!=h[0]:
         if self.ui.label_word_1.text()!='':
            self.ui.label_word_2.setText(h[0])
         else:
            self.ui.label_word_1.setText(h[0])
    def btnClicked3(self):
        global g,h
        if self.ui.label_word_1.text()!=g[1] and self.ui.label_word_2.text()!=g[1]:
         if self.ui.label_word_1.text()!='':
            self.ui.label_word_2.setText(g[1])
         else:
            self.ui.label_word_1.setText(g[1])
    def btnClicked4(self):
        global g,h
        if self.ui.label_word_1.text()!=g[2] and self.ui.label_word_2.text()!=g[2]:
         if self.ui.label_word_1.text()!='':
            self.ui.label_word_2.setText(g[2])
         else:
            self.ui.label_word_1.setText(g[2])
    def btnClicked5(self):
        global g,h
        if self.ui.label_word_1.text()!=h[1] and self.ui.label_word_2.text()!=h[1]:
         if self.ui.label_word_1.text()!='':
            self.ui.label_word_2.setText(h[1])
         else:
            self.ui.label_word_1.setText(h[1])
    def btnClicked6(self):
        global g,h
        if self.ui.label_word_1.text()!=g[3] and self.ui.label_word_2.text()!=g[3]:
         if self.ui.label_word_1.text()!='':
            self.ui.label_word_2.setText(g[3])
         else:
            self.ui.label_word_1.setText(g[3])
    def btnClicked7(self):
        global g,h
        if self.ui.label_word_1.text()!=h[2] and self.ui.label_word_2.text()!=h[2]:
          if self.ui.label_word_1.text()!='':
            self.ui.label_word_2.setText(h[2])
          else:
            self.ui.label_word_1.setText(h[2])
    def btnClicked8(self):
        global g,h
        if self.ui.label_word_1.text()!=h[3] and self.ui.label_word_2.text()!=h[3]:
          if self.ui.label_word_1.text()!='':
            self.ui.label_word_2.setText(h[3])
          else:
            self.ui.label_word_1.setText(h[3])
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
