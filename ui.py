from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import keyboard
import pymem
import os
import pymem.process
import requests
import time

chams = 0
trigger = 0

offsets = 'https://raw.githubusercontent.com/Tumpok/offsets/main/csgo.json'
response = requests.get(offsets).json()

dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
dwEntityList = int(response["signatures"]["dwEntityList"])
m_iTeamNum = int(response["netvars"]["m_iTeamNum"])
m_clrRender = int(response["netvars"]["m_clrRender"])
model_ambient_min = int(response["signatures"]["model_ambient_min"])
m_iCrosshairId = int(response["netvars"]["m_iCrosshairId"])
dwForceAttack = int(response["signatures"]["dwForceAttack"])
m_fFlags = int(response["netvars"]["m_fFlags"])

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 403)
        MainWindow.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 20, 201, 51))
        self.checkBox.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.checkB1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 90, 201, 51))
        self.checkBox_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 160, 201, 51))
        self.checkBox_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.stateChanged.connect(self.checkB3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 230, 201, 51))
        self.checkBox_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 300, 201, 51))
        self.checkBox_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_5.setObjectName("checkBox_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Trigger Bot"))
        self.checkBox_2.setText(_translate("MainWindow", "Radar Hack"))
        self.checkBox_3.setText(_translate("MainWindow", "Chams"))
        self.checkBox_4.setText(_translate("MainWindow", "Bhop"))
        self.checkBox_5.setText(_translate("MainWindow", "Glow ESP"))
    
    def checkB1(self, state):
        global trigger
        if state == QtCore.Qt.Checked:
            trigger = 1 
            print("trigger on")
        else:
            trigger = 0
            print("trigger off")
            
    def checkB3(self, state):
        global chams
        if state == QtCore.Qt.Checked:
            chams = 1 
            print("chams on")
        else:
            chams = 0
            print("chams off")
    
def thread1(threadname):

    while True:
        #print("th1")
        while trigger == 1:
            #print("trg")
            if not  keyboard.is_pressed('j'):
                time.sleep(0.1)
            if  keyboard.is_pressed('j'):
                player = pm.read_int(client + dwLocalPlayer)
                entity_id = pm.read_int(player + m_iCrosshairId)
                entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

                entity_team = pm.read_int(entity + m_iTeamNum)
                player_team = pm.read_int(player + m_iTeamNum)

                if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                    pm.write_int(client + dwForceAttack, 6)

                time.sleep(0.006)
            
        
def thread3(threadname): 
  
    rgbT = [255, 51, 0]
    rgbCT = [0, 51, 255]
    while True:
        while chams == 1:
    
            #if keyboard.is_pressed('end'):
            #    exit(0)
            #print("chms")
            try:
                for i in range(32):
                    entity = pm.read_int(client + dwEntityList + i * 0x10)
                    if entity:
                        entity_team_id = pm.read_int(entity + m_iTeamNum)
                    
                        if entity_team_id == 2:
                            pm.write_int(entity + m_clrRender, (rgbT[0]))
                            pm.write_int(entity + m_clrRender + 0x1, (rgbT[1]))
                            pm.write_int(entity + m_clrRender + 0x2, (rgbT[2]))
                        
                        elif entity_team_id == 3:
                            pm.write_int(entity + m_clrRender, (rgbCT[0]))
                            pm.write_int(entity + m_clrRender + 0x1, (rgbCT[1]))
                            pm.write_int(entity + m_clrRender + 0x2, (rgbCT[2]))
                    else:
                        pass
            except Exception as e:
                print(e)
                
def thread0(threadname):
    while True:
        global chams
        global trigger
        chams = 1
        trigger = 1
        time.sleep(0.3)
        chams = 0
        trigger = 0
        print("fffffffff")
        break



if __name__ == "__main__":
    thread0 = Thread(target=thread0, args=("Thread0",))
    thread0.start()
    thread1 = Thread(target=thread1, args=("Thread1",))
    thread1.start()
    thread3 = Thread(target=thread3, args=("Thread3",))
    thread3.start()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    #chams = 0
    #trigger = 0
    #if checkBox.isChecked() == True:
    #    chams = 1
    #else:
    #    chams = 0
        
    app.exec_()
    os.abort() 