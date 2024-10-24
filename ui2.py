from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import keyboard
import pymem
import os
import pymem.process
import requests
import time
import psutil

chams = 0
trigger = 0
radar = 0
bhop = 0
glow = 0
third = 0   
lnfov = 120
infov = 120
fov = 0
deffov = 0

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
m_bSpotted = int(response["netvars"]["m_bSpotted"])
dwForceJump = int(response["signatures"]["dwForceJump"])
dwGlowObjectManager = int(response["signatures"]["dwGlowObjectManager"])
m_iGlowIndex = int(response["netvars"]["m_iGlowIndex"])
m_iObserverMode = int(response["netvars"]["m_iObserverMode"])
m_iDefaultFOV = int(response["netvars"]["m_iDefaultFOV"])

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(366, 520)
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
        self.checkBox_2.stateChanged.connect(self.checkB2)
        
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 160, 201, 51))
        self.checkBox_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.stateChanged.connect(self.checkB3)
        
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 230, 201, 51))
        self.checkBox_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.stateChanged.connect(self.checkB4)
        
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 300, 201, 51))
        self.checkBox_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_5.stateChanged.connect(self.checkB5)
        
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 370, 201, 51))
        self.checkBox_6.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_6.stateChanged.connect(self.checkB6)
        
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(30, 440, 91, 51))
        self.checkBox_7.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_7.stateChanged.connect(self.checkB7)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 350, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 30, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 50, 121, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 440, 81, 51))
        self.lineEdit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 440, 71, 51))
        self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fovapp)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tumperror 1.2"))
        self.checkBox.setText(_translate("MainWindow", "Trigger Bot"))
        self.checkBox_2.setText(_translate("MainWindow", "Radar Hack"))
        self.checkBox_3.setText(_translate("MainWindow", "Chams"))
        self.checkBox_4.setText(_translate("MainWindow", "Bhop"))
        self.checkBox_5.setText(_translate("MainWindow", "Glow ESP"))
        self.checkBox_6.setText(_translate("MainWindow", "Thirdperson"))
        self.checkBox_7.setText(_translate("MainWindow", "FOV"))
        self.label.setText(_translate("MainWindow", "Created by Tumpok"))
        self.label_2.setText(_translate("MainWindow", "Trigger key is"))
        self.label_3.setText(_translate("MainWindow", " \"mid mouse button\""))
        self.lineEdit.setText(_translate("MainWindow", "120"))
        self.pushButton.setText(_translate("MainWindow", "apply"))
    
    def checkB1(self, state):
        global trigger
        if state == QtCore.Qt.Checked:
            trigger = 1 
            os.startfile("input.exe")
            #print("trigger on")
        else:
            trigger = 0 
            for process in (process for process in psutil.process_iter() if process.name()=="input.exe"):
                process.kill()
            #print("trigger off")
            
    def checkB2(self, state):
        global radar
        if state == QtCore.Qt.Checked:
            radar = 1 
            #print("radar on")
        else:
            radar = 0
            #print("radar off")
            
    def checkB3(self, state):
        global chams
        if state == QtCore.Qt.Checked:
            chams = 1 
            #print("chams on")
        else:
            chams = 0
            #print("chams off")
            
    def checkB4(self, state):
        global bhop
        if state == QtCore.Qt.Checked:
            bhop = 1 
            #print("bhop on")
        else:
            bhop = 0
            #print("bhop off")
            
    def checkB5(self, state):
        global glow
        if state == QtCore.Qt.Checked:
            glow = 1 
            #print("glow on")
        else:
            glow = 0
            #print("glow off")
            
    def checkB6(self, state):
        global third
        if state == QtCore.Qt.Checked:
            third = 1 
            #print("third on")
        else:
            third = 0
            #print("third off")
            
    def checkB7(self, state):
        global fov
        if state == QtCore.Qt.Checked:
            fov = 1 
            #print("third on")
        else:
            fov = 0
            #print("third off")
    
    def fovapp(self, state):
        global infov
        lnfov = self.lineEdit.text()
        infov = int(lnfov)
        #print(lnfov)
    
def thread1(threadname):

    while True:
        time.sleep(0.5)
        while trigger == 1:
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
    
def thread2(threadname):

    while True:
        time.sleep(0.5)
        while radar == 1:
            for i in range(1, 32):
                entity = pm.read_int(client + dwEntityList + i * 0x10)
                if entity:
                    pm.write_uchar(entity + m_bSpotted, 1)

                
def thread3(threadname): 
  
    rgbT = [255, 51, 0]
    rgbCT = [0, 51, 255]
    while True:
        time.sleep(0.5)
        while chams == 1:
            try:
                for i in range(32):
                    player = pm.read_int(client + dwLocalPlayer)
                    entity = pm.read_int(client + dwEntityList + i * 0x10)
                    team  = pm.read_int(player + m_iTeamNum)
                    if entity:
                        entity_team_id = pm.read_int(entity + m_iTeamNum)
                    
                        if entity_team_id != team:
                            pm.write_int(entity + m_clrRender, (rgbT[0]))
                            pm.write_int(entity + m_clrRender + 0x1, (rgbT[1]))
                            pm.write_int(entity + m_clrRender + 0x2, (rgbT[2]))
                        
                        elif entity_team_id == team: #elif entity_team_id == 3:
                            pm.write_int(entity + m_clrRender, (rgbCT[0]))
                            pm.write_int(entity + m_clrRender + 0x1, (rgbCT[1]))
                            pm.write_int(entity + m_clrRender + 0x2, (rgbCT[2]))
                    else:
                        pass
            except Exception as e:
                print(e)
                
def thread4(threadname):

    while True:
        time.sleep(0.5)
        while bhop == 1:
            if pm.read_int(client + dwLocalPlayer):
                player = pm.read_int(client + dwLocalPlayer)
                force_jump = client + dwForceJump
                on_ground = pm.read_int(player + m_fFlags)

                if keyboard.is_pressed("space"):
                    if on_ground == 257:
                        pm.write_int(force_jump, 5)
                        time.sleep(0.17)
                        pm.write_int(force_jump, 4)
                        
def thread5(threadname):

    while True:
        time.sleep(0.5)
        while glow == 1:
            player = pm.read_int(client + dwLocalPlayer)
            glow_manager = pm.read_int(client + dwGlowObjectManager)

            if (player):
                team  = pm.read_int(player + m_iTeamNum)
            
                for i in range(1, 32):
                    entity = pm.read_int(client + dwEntityList + i * 0x10)
                
                    if (entity):
                        entity_team_id = pm.read_int(entity + m_iTeamNum)
                        entity_glow = pm.read_int(entity + m_iGlowIndex)
                    
                        if (entity_team_id != team):
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))
                        
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)
                        
            #time.sleep(0.01)
            
def thread6(threadname):
    
    switch = 0
    while True:
        time.sleep(0.5)
        while third == 1:
            #print(lnfov)
            localplayer = pm.read_int(client + dwLocalPlayer)
            if keyboard.is_pressed("Caps_Lock") and switch == 0:
                pm.write_int(localplayer + m_iObserverMode, 1)
                switch = 1
                time.sleep(0.5)
            elif keyboard.is_pressed("Caps_Lock") and switch == 1:
                pm.write_int(localplayer + m_iObserverMode, 0)
                switch = 0
                time.sleep(0.5)
                
def thread7(threadname):
    
    switch = 0
    player = pm.read_int(client + dwEntityList)
    deffov = pm.read_int(player + m_iDefaultFOV)
    while True:
        time.sleep(0.5)
        while fov == 1:
            if keyboard.is_pressed("v") and switch == 0:
                pm.write_int(player + m_iDefaultFOV, infov)
                switch = 1
                time.sleep(0.5)
            if keyboard.is_pressed("v") and switch == 1:
                pm.write_int(player + m_iDefaultFOV, deffov)
                switch = 0
                time.sleep(0.5)
            if fov == 0:
                pm.write_int(player + m_iDefaultFOV, deffov)
                switch = 0
                time.sleep(0.5)
            time.sleep(0.1)

if __name__ == "__main__":
    thread1 = Thread(target=thread1, args=("Thread1",))
    thread1.start()
    thread2 = Thread(target=thread2, args=("Thread2",))
    thread2.start()
    thread3 = Thread(target=thread3, args=("Thread3",))
    thread3.start()
    thread4 = Thread(target=thread4, args=("Thread4",))
    thread4.start()
    thread5 = Thread(target=thread5, args=("Thread5",))
    thread5.start()
    thread6 = Thread(target=thread6, args=("Thread6",))
    thread6.start()
    thread7 = Thread(target=thread7, args=("Thread7",))
    thread7.start()
    
    
    #print(lnfov)
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
  
    app.exec_()
    os.abort() 