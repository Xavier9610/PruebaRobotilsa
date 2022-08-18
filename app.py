from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QVBoxLayout, QLabel,QPushButton,QListWidget,QListWidgetItem,QMenu,QAction
from PyQt5.QtCore import QTimer, QTime, Qt,QEvent,QDate,QPoint,QThread
import sys
import requests
import threading
      
class Ui(QtWidgets.QMainWindow):

    X = ""
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('gui_app.ui', self) # Load the .ui file
        #Mapping controls
        self.name=""
        self.lblHour = self.findChild(QLabel,"lblHour")
        self.lblDate = self.findChild(QLabel,"lblDate")
        self.btnRequest = self.findChild(QPushButton,"pBtnRequest")
        self.lstW = self.findChild(QListWidget,"lstWPersons")
        # eventen btbRequest
        self.btnRequest.clicked.connect(self.Request)
        # event right button 
        self.lstW.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lstW.customContextMenuRequested.connect( self.listItemRightClicked)
        self.lstW.itemSelectionChanged.connect(self.selectionChanged)
        # creating a timer 
        timer =  QTimer(self)
        # adding action to timer
        timer.timeout.connect(self.showTime)
        # update the timer every second
        timer.start(1000) 
        self.show() # Show the GUI-
        
    def showTime(self):
        # getting current timeqq
        current_time =  QTime.currentTime()
        # creating a date object
        date =QDate.currentDate()
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
        self.lblDate.setText(date.toString('dd/MM/yyyy'))
        # showing it to the label
        self.lblHour.setText(label_time)
    # method called by timer
    
    
    def Request(self):
  
        # changing the text of label after button get clicked
        url="https://swapi.dev/api/people/"
        args = {'name','height','mass','hair_color','skin_color','eye_color','birth_year','gender'}
        for i in range(10):
            print(url+str(i+1))
            response = requests.get(url+str(i+1))
            
            if response.status_code ==200:
                response_json = response.json()#Dic
                listWidgetItem = QListWidgetItem(response_json['name'])
                self.lstW.addItem(listWidgetItem);
    # Crear una función de menú de clave de derecha
    
    
    def listItemRightClicked(self, QPos): 
        self.listMenu= QMenu()
        menu_item = self.listMenu.addAction("Información del personaje")
        menu_item.triggered.connect(self.OpenInfo)
        parentPosition = self.lstW.mapToGlobal(QPoint(0, 0))        
        self.listMenu.move(parentPosition + QPos)
        self.listMenu.show() 
    
   
    def OpenInfo(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('info.ui', self) # Load the .ui file
        self.height = self.findChild(QLabel,"height")
        self.mass = self.findChild(QLabel,"mass")
        self.hairColor = self.findChild(QLabel,"hairColor")
        self.skinColor = self.findChild(QLabel,"skinColor")
        self.eyeColor = self.findChild(QLabel,"eyeColor")
        self.birthColor = self.findChild(QLabel,"bithYear")
        self.gender = self.findChild(QLabel,"gender")
        s = self.lstW.currentItem().text()
        url="https://swapi.dev/api/people/"
        self.height.setText("Prueba")
        self.mass.setText("Prueba")
        args = {'name','height','mass','hair_color','skin_color','eye_color','birth_year','gender'}
        for i in range(82):
            response = requests.get(url+str(i+1))
            
            if response.status_code ==200:
                response_json = response.json()#Dic
                listWidgetItem = QListWidgetItem(response_json['name'])
                if str(response_json['name']) == self.name:
                    self.height.setText(str(response_json['height']) )
                    self.mass.setText(str(response_json['mass']))
                    self.hairColor.setText(str(response_json['hair_color']))
                    self.skinColor.setText(str(response_json['skin_color']) )
                    self.eyeColor.setText(str(response_json['eye_color']) )
                    self.birthColor.setText(str(response_json['birth_year']) )
                    self.gender.setText(str(response_json['gender']) )
                    self.show()
                    return
        
    def selectionChanged(self):
        self.name = self.lstW.currentItem().text()
                    
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

