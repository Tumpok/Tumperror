import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from threading import Thread
import keyboard
import pymem
import os
import pymem.process
import requests
import time
import psutil
import json
from wmi import WMI

#hwid = WMI().Win32_ComputerSystemProduct()[0].UUID
#keys = #'https://raw.githubusercontent.com/Tumpok/kshw/main/kshw.json'
#response = requests.get(keys).json()
#user_key = int(response["signatures"][hwid])

#keyf = open('key.txt', 'r')
#keyss = keyf.readlines()
#keyf.close()
#key = int(keyss[0].rstrip())

#if key != user_key:
#    os.abort()

conf = open('cfg.txt', 'r')
lines = conf.readlines()
conf.close()

changer = 0
chams = 0
trigger = 0
radar = 0
bhop = 0
glow = 0
third = 0   
lnfov = int(lines[22])
infov = int(lines[22])
fov = int(lines[22])
deffov = 0
trgdd = int(lines[19])
trgdelay = int(lines[19])
trgkey = lines[20].rstrip()
fovkey = lines[23].rstrip()
print(fovkey)
thirdkey = lines[25].rstrip()
tGlow = [0, 0]
tChams = [0, 0]

rgbGlowT = [int(lines[1]), int(lines[2]), int(lines[3]), int(lines[4])]
rgbGlowE = [int(lines[6]), int(lines[7]), int(lines[8]), int(lines[9])]
rgbT = [int(lines[11]), int(lines[12]), int(lines[13])]
rgbCT = [int(lines[15]), int(lines[16]), int(lines[17])]
glowteamr = 0
glowteamg = 0
glowteamb = 1
glowteama = 1
glowenemyr = 0
glowenemyg = 0
glowenemyb = 1
glowenemya = 1


save_changes = open('cfg.txt', 'w')
save_changes.writelines(lines)
save_changes.close()


offsets = 'https://raw.githubusercontent.com/Tumpok/offsets/main/csgo.json'
#offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
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
#m_hMyWeapons = int(response['netvars']['m_hMyWeapons'])
#m_iItemIDHigh = int(response['netvars']['m_iItemIDHigh'])
#dwClientState = int(response['signatures']['dwClientState'])
#m_nFallbackPaintKit = int(response['netvars']['m_nFallbackPaintKit'])
#m_iItemDefinitionIndex = int(response['netvars']['m_iItemDefinitionIndex'])
#m_flFallbackWear = int(response['netvars']['m_flFallbackWear'])
#m_nFallbackStatTrak = int(response['netvars']['m_nFallbackStatTrak'])
#m_szCustomName = int(response['netvars']['m_szCustomName'])

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll


#from untitled import Ui_MainWindow
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(582, 760)
        MainWindow.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.WindB1 = QtWidgets.QPushButton(self.centralwidget)
        self.WindB1.setGeometry(QtCore.QRect(560, 7, 16, 16))
        self.WindB1.setStyleSheet("border-radius: 7px;\n"
"background-color: rgb(255, 0, 4);")
        self.WindB1.setText("")
        self.WindB1.setObjectName("pushButton")
        self.WindLBL = QtWidgets.QLabel(self.centralwidget)
        self.WindLBL.setGeometry(QtCore.QRect(0, 0, 676, 31))
        self.WindLBL.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.WindLBL.setText("")
        self.WindLBL.setObjectName("label")
        self.WindB2 = QtWidgets.QPushButton(self.centralwidget)
        self.WindB2.setGeometry(QtCore.QRect(535, 7, 16, 16))
        self.WindB2.setStyleSheet("background-color: rgb(255, 183, 0);\n"
"border-radius: 7px;")
        self.WindB2.setText("")
        self.WindB2.setObjectName("WindB2")
        self.WindLBL.raise_()
        self.WindB1.raise_()
        self.WindB2.raise_()
        
        #MENU
        self.ChamsBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ChamsBox.setGeometry(QtCore.QRect(21, 50, 121, 21))
        self.ChamsBox.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.ChamsBox.setObjectName("ChamsBox")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(11, 40, 563, 3))
        self.line.setMinimumSize(QtCore.QSize(0, 1))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(11, 41, 3, 691))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.ChamsTeamBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ChamsTeamBox.setGeometry(QtCore.QRect(21, 90, 121, 31))
        self.ChamsTeamBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ChamsTeamBox.setObjectName("ChamsTeamBox")
        self.ChamsEnemyBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ChamsEnemyBox.setGeometry(QtCore.QRect(161, 90, 121, 31))
        self.ChamsEnemyBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ChamsEnemyBox.setObjectName("ChamsEnemyBox")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(151, 80, 1, 201))
        self.line_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.ChamsTeamColorLB = QtWidgets.QLabel(self.centralwidget)
        self.ChamsTeamColorLB.setGeometry(QtCore.QRect(21, 130, 121, 21))
        self.ChamsTeamColorLB.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ChamsTeamColorLB.setObjectName("ChamsTeamColorLB")
        self.ChamsEnemyColorLB = QtWidgets.QLabel(self.centralwidget)
        self.ChamsEnemyColorLB.setGeometry(QtCore.QRect(161, 130, 121, 21))
        self.ChamsEnemyColorLB.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ChamsEnemyColorLB.setObjectName("ChamsEnemyColorLB")
        self.ChamsTeamRC = QtWidgets.QLabel(self.centralwidget)
        self.ChamsTeamRC.setGeometry(QtCore.QRect(21, 160, 21, 21))
        self.ChamsTeamRC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ChamsTeamRC.setObjectName("ChamsTeamRC")
        self.ChamsEnemyRC = QtWidgets.QLabel(self.centralwidget)
        self.ChamsEnemyRC.setGeometry(QtCore.QRect(161, 160, 21, 21))
        self.ChamsEnemyRC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ChamsEnemyRC.setObjectName("ChamsEnemyRC")
        self.ChamsTeamGC = QtWidgets.QLabel(self.centralwidget)
        self.ChamsTeamGC.setGeometry(QtCore.QRect(21, 190, 21, 21))
        self.ChamsTeamGC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ChamsTeamGC.setObjectName("ChamsTeamGC")
        self.ChamsEnemyGC = QtWidgets.QLabel(self.centralwidget)
        self.ChamsEnemyGC.setGeometry(QtCore.QRect(161, 190, 21, 21))
        self.ChamsEnemyGC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ChamsEnemyGC.setObjectName("ChamsEnemyGC")
        self.ChamsTeamBC = QtWidgets.QLabel(self.centralwidget)
        self.ChamsTeamBC.setGeometry(QtCore.QRect(21, 220, 21, 21))
        self.ChamsTeamBC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ChamsTeamBC.setObjectName("ChamsTeamBC")
        self.ChamsEnemyBC = QtWidgets.QLabel(self.centralwidget)
        self.ChamsEnemyBC.setGeometry(QtCore.QRect(161, 220, 21, 21))
        self.ChamsEnemyBC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ChamsEnemyBC.setObjectName("ChamsEnemyBC")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setEnabled(True)
        self.line_4.setGeometry(QtCore.QRect(12, 280, 561, 3))
        self.line_4.setMinimumSize(QtCore.QSize(0, 1))
        self.line_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(291, 41, 3, 240))
        self.line_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.ChamsTeamEditR = QtWidgets.QLineEdit(self.centralwidget)
        self.ChamsTeamEditR.setGeometry(QtCore.QRect(51, 160, 41, 21))
        self.ChamsTeamEditR.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.ChamsTeamEditR.setObjectName("ChamsTeamEditR")
        self.ChamsTeamEditG = QtWidgets.QLineEdit(self.centralwidget)
        self.ChamsTeamEditG.setGeometry(QtCore.QRect(51, 190, 41, 21))
        self.ChamsTeamEditG.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.ChamsTeamEditG.setObjectName("ChamsTeamEditG")
        self.ChamsTeamEditB = QtWidgets.QLineEdit(self.centralwidget)
        self.ChamsTeamEditB.setGeometry(QtCore.QRect(51, 220, 41, 21))
        self.ChamsTeamEditB.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.ChamsTeamEditB.setObjectName("ChamsTeamEditB")
        self.ChamsEnemyEditR = QtWidgets.QLineEdit(self.centralwidget)
        self.ChamsEnemyEditR.setGeometry(QtCore.QRect(191, 160, 41, 21))
        self.ChamsEnemyEditR.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.ChamsEnemyEditR.setObjectName("ChamsEnemyEditR")
        self.ChamsEnemyEditG = QtWidgets.QLineEdit(self.centralwidget)
        self.ChamsEnemyEditG.setGeometry(QtCore.QRect(191, 190, 41, 21))
        self.ChamsEnemyEditG.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.ChamsEnemyEditG.setObjectName("ChamsEnemyEditG")
        self.ChamsEnemyEditB = QtWidgets.QLineEdit(self.centralwidget)
        self.ChamsEnemyEditB.setGeometry(QtCore.QRect(191, 220, 41, 21))
        self.ChamsEnemyEditB.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.ChamsEnemyEditB.setObjectName("ChamsEnemyEditB")
        self.GlowBox = QtWidgets.QCheckBox(self.centralwidget)
        self.GlowBox.setGeometry(QtCore.QRect(301, 50, 121, 21))
        self.GlowBox.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.GlowBox.setObjectName("GlowBox")
        self.GlowEnemyEditB = QtWidgets.QLineEdit(self.centralwidget)
        self.GlowEnemyEditB.setGeometry(QtCore.QRect(471, 220, 41, 21))
        self.GlowEnemyEditB.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.GlowEnemyEditB.setObjectName("GlowEnemyEditB")
        self.GlowTeamGC = QtWidgets.QLabel(self.centralwidget)
        self.GlowTeamGC.setGeometry(QtCore.QRect(301, 190, 21, 21))
        self.GlowTeamGC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.GlowTeamGC.setObjectName("GlowTeamGC")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(431, 80, 1, 201))
        self.line_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.GlowEnemyGC = QtWidgets.QLabel(self.centralwidget)
        self.GlowEnemyGC.setGeometry(QtCore.QRect(441, 190, 21, 21))
        self.GlowEnemyGC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.GlowEnemyGC.setObjectName("GlowEnemyGC")
        self.GlowTeamAC = QtWidgets.QLabel(self.centralwidget)
        self.GlowTeamAC.setGeometry(QtCore.QRect(301, 250, 21, 21))
        self.GlowTeamAC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.GlowTeamAC.setObjectName("GlowTeamAC")
        self.GlowEnemyEditR = QtWidgets.QLineEdit(self.centralwidget)
        self.GlowEnemyEditR.setGeometry(QtCore.QRect(471, 160, 41, 21))
        self.GlowEnemyEditR.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.GlowEnemyEditR.setObjectName("GlowEnemyEditR")
        self.GlowEnemyColorLB = QtWidgets.QLabel(self.centralwidget)
        self.GlowEnemyColorLB.setGeometry(QtCore.QRect(441, 130, 121, 21))
        self.GlowEnemyColorLB.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.GlowEnemyColorLB.setObjectName("GlowEnemyColorLB")
        self.GlowTeamBox = QtWidgets.QCheckBox(self.centralwidget)
        self.GlowTeamBox.setGeometry(QtCore.QRect(301, 90, 121, 31))
        self.GlowTeamBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.GlowTeamBox.setObjectName("GlowTeamBox")
        self.GlowTeamRC = QtWidgets.QLabel(self.centralwidget)
        self.GlowTeamRC.setGeometry(QtCore.QRect(301, 160, 21, 21))
        self.GlowTeamRC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.GlowTeamRC.setObjectName("GlowTeamRC")
        self.GlowTEamEditB = QtWidgets.QLineEdit(self.centralwidget)
        self.GlowTEamEditB.setGeometry(QtCore.QRect(331, 220, 41, 21))
        self.GlowTEamEditB.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.GlowTEamEditB.setObjectName("GlowTEamEditB")
        self.GlowEnemyRC = QtWidgets.QLabel(self.centralwidget)
        self.GlowEnemyRC.setGeometry(QtCore.QRect(441, 160, 21, 21))
        self.GlowEnemyRC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.GlowEnemyRC.setObjectName("GlowEnemyRC")
        self.GlowTEamEditA = QtWidgets.QLineEdit(self.centralwidget)
        self.GlowTEamEditA.setGeometry(QtCore.QRect(331, 250, 41, 21))
        self.GlowTEamEditA.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.GlowTEamEditA.setObjectName("GlowTEamEditA")
        self.GlowEnemyEditA = QtWidgets.QLineEdit(self.centralwidget)
        self.GlowEnemyEditA.setGeometry(QtCore.QRect(471, 250, 41, 21))
        self.GlowEnemyEditA.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.GlowEnemyEditA.setObjectName("GlowEnemyEditA")
        self.GlowTeamColorLB = QtWidgets.QLabel(self.centralwidget)
        self.GlowTeamColorLB.setGeometry(QtCore.QRect(301, 130, 121, 21))
        self.GlowTeamColorLB.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.GlowTeamColorLB.setObjectName("GlowTeamColorLB")
        self.GlowEnemyBC = QtWidgets.QLabel(self.centralwidget)
        self.GlowEnemyBC.setGeometry(QtCore.QRect(441, 220, 21, 21))
        self.GlowEnemyBC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.GlowEnemyBC.setObjectName("GlowEnemyBC")
        self.GlowEnemyBox = QtWidgets.QCheckBox(self.centralwidget)
        self.GlowEnemyBox.setGeometry(QtCore.QRect(441, 90, 121, 31))
        self.GlowEnemyBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.GlowEnemyBox.setObjectName("GlowEnemyBox")
        self.GlowTEamEditG = QtWidgets.QLineEdit(self.centralwidget)
        self.GlowTEamEditG.setGeometry(QtCore.QRect(331, 190, 41, 21))
        self.GlowTEamEditG.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.GlowTEamEditG.setObjectName("GlowTEamEditG")
        self.GlowTeamBC = QtWidgets.QLabel(self.centralwidget)
        self.GlowTeamBC.setGeometry(QtCore.QRect(301, 220, 21, 21))
        self.GlowTeamBC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.GlowTeamBC.setObjectName("GlowTeamBC")
        self.GlowEnemyAC = QtWidgets.QLabel(self.centralwidget)
        self.GlowEnemyAC.setGeometry(QtCore.QRect(441, 250, 21, 21))
        self.GlowEnemyAC.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.GlowEnemyAC.setObjectName("GlowEnemyAC")
        self.GlowEnemyEditG = QtWidgets.QLineEdit(self.centralwidget)
        self.GlowEnemyEditG.setGeometry(QtCore.QRect(471, 190, 41, 21))
        self.GlowEnemyEditG.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.GlowEnemyEditG.setObjectName("GlowEnemyEditG")
        self.GlowTEamEditR = QtWidgets.QLineEdit(self.centralwidget)
        self.GlowTEamEditR.setGeometry(QtCore.QRect(331, 160, 41, 21))
        self.GlowTEamEditR.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.GlowTEamEditR.setObjectName("GlowTEamEditR")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(571, 41, 3, 691))
        self.line_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.TriggerBox = QtWidgets.QCheckBox(self.centralwidget)
        self.TriggerBox.setGeometry(QtCore.QRect(21, 290, 121, 31))
        self.TriggerBox.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.TriggerBox.setObjectName("TriggerBox")
        self.TriggerDelayLB = QtWidgets.QLabel(self.centralwidget)
        self.TriggerDelayLB.setGeometry(QtCore.QRect(20, 330, 61, 31))
        self.TriggerDelayLB.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.TriggerDelayLB.setObjectName("TriggerDelayLB")
        self.TriggerEditDeley = QtWidgets.QLineEdit(self.centralwidget)
        self.TriggerEditDeley.setGeometry(QtCore.QRect(90, 330, 51, 31))
        self.TriggerEditDeley.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.TriggerEditDeley.setObjectName("TriggerEditDeley")
        self.TriggerKeyLB = QtWidgets.QLabel(self.centralwidget)
        self.TriggerKeyLB.setGeometry(QtCore.QRect(20, 370, 51, 31))
        self.TriggerKeyLB.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.TriggerKeyLB.setObjectName("TriggerKeyLB")
        self.TriggerEditKey = QtWidgets.QLineEdit(self.centralwidget)
        self.TriggerEditKey.setGeometry(QtCore.QRect(80, 370, 111, 31))
        self.TriggerEditKey.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.TriggerEditKey.setObjectName("TriggerEditKey")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setEnabled(True)
        self.line_6.setGeometry(QtCore.QRect(12, 410, 241, 3))
        self.line_6.setMinimumSize(QtCore.QSize(0, 1))
        self.line_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setEnabled(True)
        self.line_9.setGeometry(QtCore.QRect(12, 540, 241, 3))
        self.line_9.setMinimumSize(QtCore.QSize(0, 1))
        self.line_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.FOVKeyLB = QtWidgets.QLabel(self.centralwidget)
        self.FOVKeyLB.setGeometry(QtCore.QRect(20, 500, 51, 31))
        self.FOVKeyLB.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.FOVKeyLB.setObjectName("FOVKeyLB")
        self.FOVBox = QtWidgets.QCheckBox(self.centralwidget)
        self.FOVBox.setGeometry(QtCore.QRect(21, 420, 121, 31))
        self.FOVBox.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.FOVBox.setObjectName("FOVBox")
        self.FOVEditKey = QtWidgets.QLineEdit(self.centralwidget)
        self.FOVEditKey.setGeometry(QtCore.QRect(80, 500, 111, 31))
        self.FOVEditKey.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.FOVEditKey.setObjectName("FOVEditKey")
        self.FOVAngleLB = QtWidgets.QLabel(self.centralwidget)
        self.FOVAngleLB.setGeometry(QtCore.QRect(20, 460, 71, 31))
        self.FOVAngleLB.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.FOVAngleLB.setObjectName("FOVAngleLB")
        self.FOVEditAngle = QtWidgets.QLineEdit(self.centralwidget)
        self.FOVEditAngle.setGeometry(QtCore.QRect(100, 460, 41, 31))
        self.FOVEditAngle.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.FOVEditAngle.setObjectName("FOVEditAngle")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setEnabled(True)
        self.line_10.setGeometry(QtCore.QRect(12, 730, 561, 3))
        self.line_10.setMinimumSize(QtCore.QSize(0, 1))
        self.line_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.ThirdpesonKeyLB = QtWidgets.QLabel(self.centralwidget)
        self.ThirdpesonKeyLB.setGeometry(QtCore.QRect(20, 590, 51, 31))
        self.ThirdpesonKeyLB.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.ThirdpesonKeyLB.setObjectName("ThirdpesonKeyLB")
        self.ThirdpersonBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ThirdpersonBox.setGeometry(QtCore.QRect(21, 550, 161, 31))
        self.ThirdpersonBox.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.ThirdpersonBox.setObjectName("ThirdpersonBox")
        self.ThirdpersonEditKey = QtWidgets.QLineEdit(self.centralwidget)
        self.ThirdpersonEditKey.setGeometry(QtCore.QRect(80, 590, 111, 31))
        self.ThirdpersonEditKey.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.ThirdpersonEditKey.setObjectName("ThirdpersonEditKey")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setEnabled(True)
        self.line_11.setGeometry(QtCore.QRect(12, 680, 241, 3))
        self.line_11.setMinimumSize(QtCore.QSize(0, 1))
        self.line_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.RadarBox = QtWidgets.QCheckBox(self.centralwidget)
        self.RadarBox.setGeometry(QtCore.QRect(21, 690, 221, 31))
        self.RadarBox.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.RadarBox.setObjectName("RadarBox")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setEnabled(True)
        self.line_12.setGeometry(QtCore.QRect(12, 630, 241, 3))
        self.line_12.setMinimumSize(QtCore.QSize(0, 1))
        self.line_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.BhopBox = QtWidgets.QCheckBox(self.centralwidget)
        self.BhopBox.setGeometry(QtCore.QRect(21, 640, 221, 31))
        self.BhopBox.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.BhopBox.setObjectName("BhopBox")
        self.ChamsTeapAppClr = QtWidgets.QPushButton(self.centralwidget)
        self.ChamsTeapAppClr.setGeometry(QtCore.QRect(30, 250, 41, 21))
        self.ChamsTeapAppClr.setObjectName("ChamsTeapAppClr")
        self.ChamsEnemyAppClr = QtWidgets.QPushButton(self.centralwidget)
        self.ChamsEnemyAppClr.setGeometry(QtCore.QRect(170, 250, 41, 21))
        self.ChamsEnemyAppClr.setObjectName("ChamsEnemyAppClr")
        self.GlowTeamAppClr = QtWidgets.QPushButton(self.centralwidget)
        self.GlowTeamAppClr.setGeometry(QtCore.QRect(380, 250, 41, 21))
        self.GlowTeamAppClr.setObjectName("GlowTeamAppClr")
        self.ChamsEnemyAppClr_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ChamsEnemyAppClr_2.setGeometry(QtCore.QRect(520, 250, 41, 21))
        self.ChamsEnemyAppClr_2.setObjectName("ChamsEnemyAppClr_2")
        self.TriggerKeyApp = QtWidgets.QPushButton(self.centralwidget)
        self.TriggerKeyApp.setGeometry(QtCore.QRect(200, 370, 41, 31))
        self.TriggerKeyApp.setObjectName("TriggerKeyApp")
        self.TriggerDelayApp = QtWidgets.QPushButton(self.centralwidget)
        self.TriggerDelayApp.setGeometry(QtCore.QRect(150, 330, 41, 31))
        self.TriggerDelayApp.setObjectName("TriggerDelayApp")
        self.FOVAnglrApp = QtWidgets.QPushButton(self.centralwidget)
        self.FOVAnglrApp.setGeometry(QtCore.QRect(150, 460, 41, 31))
        self.FOVAnglrApp.setObjectName("FOVAnglrApp")
        self.FOVKeyApp = QtWidgets.QPushButton(self.centralwidget)
        self.FOVKeyApp.setGeometry(QtCore.QRect(200, 500, 41, 31))
        self.FOVKeyApp.setObjectName("FOVKeyApp")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(250, 281, 3, 451))
        self.line_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.ThirdpersonKeyApp = QtWidgets.QPushButton(self.centralwidget)
        self.ThirdpersonKeyApp.setGeometry(QtCore.QRect(200, 590, 41, 31))
        self.ThirdpersonKeyApp.setObjectName("ThirdpersonKeyApp")
        self.SkinChangerrBox = QtWidgets.QCheckBox(self.centralwidget)
        self.SkinChangerrBox.setGeometry(QtCore.QRect(270, 290, 211, 31))
        self.SkinChangerrBox.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.SkinChangerrBox.setObjectName("SkinChangerrBox")
        self.ChangerEditApp = QtWidgets.QPushButton(self.centralwidget)
        self.ChangerEditApp.setGeometry(QtCore.QRect(490, 290, 71, 31))
        self.ChangerEditApp.setObjectName("ChangerEditApp")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setEnabled(True)
        self.line_14.setGeometry(QtCore.QRect(250, 330, 321, 3))
        self.line_14.setMinimumSize(QtCore.QSize(0, 1))
        self.line_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.SaveCfgApp = QtWidgets.QPushButton(self.centralwidget)
        self.SaveCfgApp.setGeometry(QtCore.QRect(260, 690, 101, 31))
        self.SaveCfgApp.setObjectName("SaveCfgApp")
        self.LoadCfgApp = QtWidgets.QPushButton(self.centralwidget)
        self.LoadCfgApp.setGeometry(QtCore.QRect(370, 690, 101, 31))
        self.LoadCfgApp.setObjectName("LoadCfgApp")
        self.EditCfgApp = QtWidgets.QPushButton(self.centralwidget)
        self.EditCfgApp.setGeometry(QtCore.QRect(480, 690, 91, 31))
        self.EditCfgApp.setObjectName("EditCfgApp")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setEnabled(True)
        self.line_15.setGeometry(QtCore.QRect(250, 680, 321, 3))
        self.line_15.setMinimumSize(QtCore.QSize(0, 1))
        self.line_15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 160, 28))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("name.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 370, 231, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("cmsn.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        
        
        self.TriggerBox.stateChanged.connect(self.TriggerBoxT)
        self.RadarBox.stateChanged.connect(self.RadarBoxT)
        self.ChamsBox.stateChanged.connect(self.ChamsBoxT)
        self.GlowTeamBox.stateChanged.connect(self.GlowTeamBoxT)
        self.GlowEnemyBox.stateChanged.connect(self.GlowEnemyBoxT)
        self.ChamsTeamBox.stateChanged.connect(self.ChamsTeamBoxT)
        self.ChamsEnemyBox.stateChanged.connect(self.ChamsEnemyBoxT)
        self.BhopBox.stateChanged.connect(self.BhopBoxT)
        self.GlowBox.stateChanged.connect(self.GlowBoxT)
        self.ThirdpersonBox.stateChanged.connect(self.ThirdpersonBoxT)
        self.FOVBox.stateChanged.connect(self.FOVBoxT)
        self.SkinChangerrBox.stateChanged.connect(self.SkinChanger)
        
        self.FOVAnglrApp.clicked.connect(self.fovapp)
        self.FOVKeyApp.clicked.connect(self.fovkeyapp)
        self.ThirdpersonKeyApp.clicked.connect(self.thirdkeyapp)
        self.TriggerDelayApp.clicked.connect(self.triggerdalay)
        self.GlowTeamAppClr.clicked.connect(self.glowteamcl)
        self.ChamsEnemyAppClr_2.clicked.connect(self.glowenemycl)
        self.ChamsTeapAppClr.clicked.connect(self.chamsteamcl)
        self.ChamsEnemyAppClr.clicked.connect(self.chamsenemycl)
        self.ChangerEditApp.clicked.connect(self.changcfgapp)
        self.EditCfgApp.clicked.connect(self.cfgapp)
        self.SaveCfgApp.clicked.connect(self.svcfgapp)
        self.TriggerKeyApp.clicked.connect(self.trgkeyapp)
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        #MENU
        self.ChamsBox.setText(_translate("MainWindow", "Chams"))
        self.ChamsTeamBox.setText(_translate("MainWindow", "Team"))
        self.ChamsEnemyBox.setText(_translate("MainWindow", "Enemy"))
        self.ChamsTeamColorLB.setText(_translate("MainWindow", "Color:"))
        self.ChamsEnemyColorLB.setText(_translate("MainWindow", "Color:"))
        self.ChamsTeamRC.setText(_translate("MainWindow", "R:"))
        self.ChamsEnemyRC.setText(_translate("MainWindow", "R:"))
        self.ChamsTeamGC.setText(_translate("MainWindow", "G:"))
        self.ChamsEnemyGC.setText(_translate("MainWindow", "G:"))
        self.ChamsTeamBC.setText(_translate("MainWindow", "B:"))
        self.ChamsEnemyBC.setText(_translate("MainWindow", "B:"))
        self.ChamsTeamEditR.setText(_translate("MainWindow", "14"))
        self.ChamsTeamEditG.setText(_translate("MainWindow", "14"))
        self.ChamsTeamEditB.setText(_translate("MainWindow", "14"))
        self.ChamsEnemyEditR.setText(_translate("MainWindow", "15"))
        self.ChamsEnemyEditG.setText(_translate("MainWindow", "15"))
        self.ChamsEnemyEditB.setText(_translate("MainWindow", "15"))
        self.GlowBox.setText(_translate("MainWindow", "Glow"))
        self.GlowEnemyEditB.setText(_translate("MainWindow", "17"))
        self.GlowTeamGC.setText(_translate("MainWindow", "G:"))
        self.GlowEnemyGC.setText(_translate("MainWindow", "G:"))
        self.GlowTeamAC.setText(_translate("MainWindow", "A:"))
        self.GlowEnemyEditR.setText(_translate("MainWindow", "17"))
        self.GlowEnemyColorLB.setText(_translate("MainWindow", "Color:"))
        self.GlowTeamBox.setText(_translate("MainWindow", "Team"))
        self.GlowTeamRC.setText(_translate("MainWindow", "R:"))
        self.GlowTEamEditB.setText(_translate("MainWindow", "16"))
        self.GlowEnemyRC.setText(_translate("MainWindow", "R:"))
        self.GlowTEamEditA.setText(_translate("MainWindow", "16"))
        self.GlowEnemyEditA.setText(_translate("MainWindow", "17"))
        self.GlowTeamColorLB.setText(_translate("MainWindow", "Color:"))
        self.GlowEnemyBC.setText(_translate("MainWindow", "B:"))
        self.GlowEnemyBox.setText(_translate("MainWindow", "Enemy"))
        self.GlowTEamEditG.setText(_translate("MainWindow", "16"))
        self.GlowTeamBC.setText(_translate("MainWindow", "B:"))
        self.GlowEnemyAC.setText(_translate("MainWindow", "A:"))
        self.GlowEnemyEditG.setText(_translate("MainWindow", "17"))
        self.GlowTEamEditR.setText(_translate("MainWindow", "16"))
        self.TriggerBox.setText(_translate("MainWindow", "Trigger"))
        self.TriggerDelayLB.setText(_translate("MainWindow", "Delay:"))
        self.TriggerEditDeley.setText(_translate("MainWindow", "0"))
        self.TriggerKeyLB.setText(_translate("MainWindow", "Key:"))
        self.TriggerEditKey.setText(_translate("MainWindow", "Mbutton"))
        self.FOVKeyLB.setText(_translate("MainWindow", "Key:"))
        self.FOVBox.setText(_translate("MainWindow", "FOV"))
        self.FOVEditKey.setText(_translate("MainWindow", "v"))
        self.FOVAngleLB.setText(_translate("MainWindow", "Angle:"))
        self.FOVEditAngle.setText(_translate("MainWindow", "120"))
        self.ThirdpesonKeyLB.setText(_translate("MainWindow", "Key:"))
        self.ThirdpersonBox.setText(_translate("MainWindow", "Thirdperson"))
        self.ThirdpersonEditKey.setText(_translate("MainWindow", "Caps_Lock"))
        self.RadarBox.setText(_translate("MainWindow", "Radar Hack"))
        self.BhopBox.setText(_translate("MainWindow", "Bhop"))
        self.ChamsTeapAppClr.setText(_translate("MainWindow", "apply"))
        self.ChamsEnemyAppClr.setText(_translate("MainWindow", "apply"))
        self.GlowTeamAppClr.setText(_translate("MainWindow", "apply"))
        self.ChamsEnemyAppClr_2.setText(_translate("MainWindow", "apply"))
        self.TriggerKeyApp.setText(_translate("MainWindow", "apply"))
        self.TriggerDelayApp.setText(_translate("MainWindow", "apply"))
        self.FOVAnglrApp.setText(_translate("MainWindow", "apply"))
        self.FOVKeyApp.setText(_translate("MainWindow", "apply"))
        self.ThirdpersonKeyApp.setText(_translate("MainWindow", "apply"))
        self.SkinChangerrBox.setText(_translate("MainWindow", "SkinChanger"))
        self.ChangerEditApp.setText(_translate("MainWindow", "Edit Cfg"))
        self.SaveCfgApp.setText(_translate("MainWindow", "Save Config"))
        self.LoadCfgApp.setText(_translate("MainWindow", "Load Config"))
        self.EditCfgApp.setText(_translate("MainWindow", "Edit Config"))
        
        self.GlowTEamEditR.setText(_translate("MainWindow", str(rgbGlowT[0])))
        self.GlowTEamEditG.setText(_translate("MainWindow", str(rgbGlowT[1])))
        self.GlowTEamEditB.setText(_translate("MainWindow", str(rgbGlowT[2])))
        self.GlowTEamEditA.setText(_translate("MainWindow", str(rgbGlowT[3])))
        self.GlowEnemyEditR.setText(_translate("MainWindow", str(rgbGlowE[0])))
        self.GlowEnemyEditG.setText(_translate("MainWindow", str(rgbGlowE[1])))
        self.GlowEnemyEditB.setText(_translate("MainWindow", str(rgbGlowE[2])))
        self.GlowEnemyEditA.setText(_translate("MainWindow", str(rgbGlowE[3])))
        self.ChamsTeamEditR.setText(_translate("MainWindow", str(rgbT[0])))
        self.ChamsTeamEditG.setText(_translate("MainWindow", str(rgbT[1])))
        self.ChamsTeamEditB.setText(_translate("MainWindow", str(rgbT[2])))
        self.ChamsEnemyEditR.setText(_translate("MainWindow", str(rgbCT[0])))
        self.ChamsEnemyEditG.setText(_translate("MainWindow", str(rgbCT[1])))
        self.ChamsEnemyEditB.setText(_translate("MainWindow", str(rgbCT[2])))
        self.TriggerEditDeley.setText(_translate("MainWindow", str(trgdelay)))
        self.TriggerEditKey.setText(_translate("MainWindow", trgkey))
        self.FOVEditKey.setText(_translate("MainWindow", fovkey))
        self.FOVEditAngle.setText(_translate("MainWindow", str(fov)))
        self.ThirdpersonEditKey.setText(_translate("MainWindow", thirdkey))
        
        
        
    def TriggerBoxT(self, state):
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
            
    def RadarBoxT(self, state):
        global radar
        if state == QtCore.Qt.Checked:
            radar = 1 
            #print("radar on")
        else:
            radar = 0
            #print("radar off")
            
    def ChamsBoxT(self, state):
        global chams
        if state == QtCore.Qt.Checked:
            chams = 1 
            #print("chams on")
        else:
            chams = 0
            #print("chams off")
            
    def GlowTeamBoxT(self, state):
        #global tGlow
        if state == QtCore.Qt.Checked:
            tGlow[0] = 1 
        else:
            tGlow[0] = 0
            
    def GlowEnemyBoxT(self, state):
        #global tGlow
        if state == QtCore.Qt.Checked:
            tGlow[1] = 1 
        else:
            tGlow[1] = 0
            
    def ChamsTeamBoxT(self, state):
        #global tChams
        if state == QtCore.Qt.Checked:
            tChams[0] = 1 
        else:
            tChams[0] = 0
            
    def ChamsEnemyBoxT(self, state):
        #global tChams
        if state == QtCore.Qt.Checked:
            tChams[1] = 1 
        else:
            tChams[1] = 0
            
    def BhopBoxT(self, state):
        global bhop
        if state == QtCore.Qt.Checked:
            bhop = 1 
            #print("bhop on")
        else:
            bhop = 0
            #print("bhop off")
            
    def GlowBoxT(self, state):
        global glow
        if state == QtCore.Qt.Checked:
            glow = 1 
            #print("glow on")
        else:
            glow = 0
            #print("glow off")
            
    def ThirdpersonBoxT(self, state):
        global third
        if state == QtCore.Qt.Checked:
            third = 1 
            #print("third on")
        else:
            third = 0
            #print("third off")
            
    def FOVBoxT(self, state):
        global fov
        if state == QtCore.Qt.Checked:
            fov = 1 
            #print("third on")
        else:
            fov = 0
            #print("third off")
    
    def fovapp(self, state):
        global infov
        lnfov = self.FOVEditAngle.text()
        infov = int(lnfov)
        #print(lnfov)
        
    def fovkeyapp(self, state):
        global fovkey
        fovkey = self.FOVEditKey.text()
        
    def trgkeyapp(self, state):
        global trgkey
        trgkey = self.TriggerEditKey.text()
        
    def changcfgapp(self, state):
        os.startfile("changer.txt")
        
    def cfgapp(self, state):
        os.startfile("cfg.txt")
        
    def svcfgapp(self, state):
        lnfov = self.FOVEditAngle.text()
        infov = int(lnfov)
        fovkey = self.FOVEditKey.text()
        trgkey = self.TriggerEditKey.text()
        thirdkey = self.ThirdpersonEditKey.text()
        trgdd = self.TriggerEditDeley.text()
        trgdelay = float(trgdd)
        if self.GlowTEamEditR.text() == "0":
            rgbGlowT[0] = 0
        else:
            rgbGlowT[0] = int(self.GlowTEamEditR.text()) / 255
        if self.GlowTEamEditG.text() == "0":
            rgbGlowT[1] = 0
        else:
            rgbGlowT[1] = int(self.GlowTEamEditG.text()) / 255
        if self.GlowTEamEditB.text() == "0":
            rgbGlowT[2] = 0
        else:
            rgbGlowT[2] = int(self.GlowTEamEditB.text()) / 255
        if self.GlowTEamEditA.text() == "0":
            rgbGlowT[3] = 0
        else:
            rgbGlowT[3] = int(self.GlowTEamEditA.text()) / 255
        if self.GlowEnemyEditR.text() == "0":
            rgbGlowE[0] = 0
        else:
            rgbGlowE[0] = int(self.GlowEnemyEditR.text()) / 255
        if self.GlowEnemyEditG.text() == "0":
            rgbGlowE[1] = 0
        else:
            rgbGlowE[1] = int(self.GlowEnemyEditG.text()) / 255
        if self.GlowEnemyEditB.text() == "0":
            rgbGlowE[2] = 0
        else:
            rgbGlowE[2] = int(self.GlowEnemyEditB.text()) / 255
        if self.GlowEnemyEditA.text() == "0":
            rgbGlowE[3] = 0
        else:
            rgbGlowE[3] = int(self.GlowEnemyEditA.text()) / 255
        if self.ChamsTeamEditR.text() == "0":
            rgbT[0] = 0
        else:
            rgbT[0] = int(self.ChamsTeamEditR.text()) / 1
        if self.ChamsTeamEditG.text() == "0":
            rgbT[1] = 0
        else:
            rgbT[1] = int(self.ChamsTeamEditG.text()) / 1
        if self.ChamsTeamEditB.text() == "0":
            rgbT[2] = 0
        else:
            rgbT[2] = int(self.ChamsTeamEditB.text()) / 1
        if self.ChamsEnemyEditR.text() == "0":
            rgbCT[0] = 0
        else:
            rgbCT[0] = int(self.ChamsEnemyEditR.text()) / 1
        if self.ChamsEnemyEditG.text() == "0":
            rgbCT[1] = 0
        else:
            rgbCT[1] = int(self.ChamsEnemyEditG.text()) / 1
        if self.ChamsEnemyEditB.text() == "0":
            rgbCT[2] = 0
        else:
            rgbCT[2] = int(self.ChamsEnemyEditB.text()) / 1
        sv = open('cfg.txt', 'r')
        lines = sv.readlines()
        lines[0] = 'Glow Team (r g b a)' + '\n'
        lines[1] = str(int(rgbGlowT[0] * 255)) + '\n'
        lines[2] = str(int(rgbGlowT[1] * 255)) + '\n'
        lines[3] = str(int(rgbGlowT[2] * 255)) + '\n'
        lines[4] = str(int(rgbGlowT[3] * 255)) + '\n'
        lines[5] = 'Glow Enemy (r g b a)' + '\n'
        lines[6] = str(int(rgbGlowE[0] * 255)) + '\n'
        lines[7] = str(int(rgbGlowE[1] * 255)) + '\n'
        lines[8] = str(int(rgbGlowE[2] * 255)) + '\n'
        lines[9] = str(int(rgbGlowE[3] * 255)) + '\n'
        lines[10] = 'Chams Team (r g b)' + '\n'
        lines[11] = str(rgbT[0]) + '\n'
        lines[12] = str(rgbT[1]) + '\n'
        lines[13] = str(rgbT[2]) + '\n'
        lines[14] = 'Chams Enemy (r g b)' + '\n'
        lines[15] = str(rgbCT[0]) + '\n'
        lines[16] = str(rgbCT[1]) + '\n'
        lines[17] = str(rgbCT[2]) + '\n'
        lines[18] = 'Trigger (Delay Key)' + '\n'
        lines[19] = trgdd# + '\n'
        lines[20] = trgkey# + '\n'
        lines[21] = 'FOV (Angle Key)' + '\n'
        lines[22] = lnfov# + '\n'
        lines[23] = fovkey# + '\n'
        lines[24] = 'Thirdperson (Key)' + '\n'
        lines[25] = thirdkey# + '\n'
        sv.close()
 
        save = open('cfg.txt', 'w')
        save.writelines(lines)
        save.close()
        
    def thirdkeyapp(self, state):
        global thirdkey
        thirdkey = self.ThirdpersonEditKey.text()
        
    def triggerdalay(self, state):
        global trgdelay
        trgdd = self.TriggerEditDeley.text()
        trgdelay = float(trgdd)
        
    def glowteamcl(self, state):
        global rgbGlowT
        if self.GlowTEamEditR.text() == "0":
            rgbGlowT[0] = 0
        else:
            rgbGlowT[0] = int(self.GlowTEamEditR.text()) / 255
        if self.GlowTEamEditG.text() == "0":
            rgbGlowT[1] = 0
        else:
            rgbGlowT[1] = int(self.GlowTEamEditG.text()) / 255
        if self.GlowTEamEditB.text() == "0":
            rgbGlowT[2] = 0
        else:
            rgbGlowT[2] = int(self.GlowTEamEditB.text()) / 255
        if self.GlowTEamEditA.text() == "0":
            rgbGlowT[3] = 0
        else:
            rgbGlowT[3] = int(self.GlowTEamEditA.text()) / 255
            
    def glowenemycl(self, state):
        global rgbGlowE
        if self.GlowEnemyEditR.text() == "0":
            rgbGlowE[0] = 0
        else:
            rgbGlowE[0] = int(self.GlowEnemyEditR.text()) / 255
        if self.GlowEnemyEditG.text() == "0":
            rgbGlowE[1] = 0
        else:
            rgbGlowE[1] = int(self.GlowEnemyEditG.text()) / 255
        if self.GlowEnemyEditB.text() == "0":
            rgbGlowE[2] = 0
        else:
            rgbGlowE[2] = int(self.GlowEnemyEditB.text()) / 255
        if self.GlowEnemyEditA.text() == "0":
            rgbGlowE[3] = 0
        else:
            rgbGlowE[3] = int(self.GlowEnemyEditA.text()) / 255
            
    def chamsteamcl(self, state):
        print('team')
        if self.ChamsTeamEditR.text() == "0":
            rgbT[0] = 0
        else:
            rgbT[0] = int(self.ChamsTeamEditR.text()) / 1
        if self.ChamsTeamEditG.text() == "0":
            rgbT[1] = 0
        else:
            rgbT[1] = int(self.ChamsTeamEditG.text()) / 1
        if self.ChamsTeamEditB.text() == "0":
            rgbT[2] = 0
        else:
            rgbT[2] = int(self.ChamsTeamEditB.text()) / 1
            
    def chamsenemycl(self, state):
        global rgbCT
        if self.ChamsEnemyEditR.text() == "0":
            rgbCT[0] = 0
        else:
            rgbCT[0] = int(self.ChamsEnemyEditR.text()) / 1
        if self.ChamsEnemyEditG.text() == "0":
            rgbCT[1] = 0
        else:
            rgbCT[1] = int(self.ChamsEnemyEditG.text()) / 1
        if self.ChamsEnemyEditB.text() == "0":
            rgbCT[2] = 0
        else:
            rgbCT[2] = int(self.ChamsEnemyEditB.text()) / 1
            
    def SkinChanger(self, state):
        global changer
        if state == QtCore.Qt.Checked:
            changer = 1 
        else:
            changer = 0


        


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.WindB1.clicked.connect(self.myClose)

        self.WindB2.clicked.connect(self.myMinimize)

        self.start = QPoint(0, 0)    # +                  
        self.pressing = False        # +


    def myClose(self):
#        self.WindB1.clicked.connect(self.close)
        self.close()
        app.exec_()
        os.abort() 

    def myMinimize(self):
#        self.WindB2.clicked.connect(self.showMinimized)
        self.showMinimized()     

# + vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.width(),
                                self.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False
# + ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  

#ChestThreads
def trigger_t(threadname):

    while True:
        time.sleep(0.5)
        while trigger == 1:
            try:
                if not  keyboard.is_pressed('j'):
                    time.sleep(0.1)
                if  keyboard.is_pressed('j'):
                    time.sleep(trgdelay)
                    player = pm.read_int(client + dwLocalPlayer)
                    entity_id = pm.read_int(player + m_iCrosshairId)
                    entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

                    entity_team = pm.read_int(entity + m_iTeamNum)
                    player_team = pm.read_int(player + m_iTeamNum)

                    if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                        pm.write_int(client + dwForceAttack, 6)

                    time.sleep(0.006)
            except:
                print("Trigger Error")
    
def radar_t(threadname):

    while True:
        time.sleep(0.5)
        while radar == 1:
            try:
                for i in range(1, 32):
                    entity = pm.read_int(client + dwEntityList + i * 0x10)
                    if entity:
                        pm.write_uchar(entity + m_bSpotted, 1)
            except:
                print("Radar Error")

                
def chams_t(threadname): 
  

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
                    
                        if entity_team_id != team and tChams[1] == 1:
                            pm.write_int(entity + m_clrRender, (rgbCT[0]))
                            pm.write_int(entity + m_clrRender + 0x1, (rgbCT[1]))
                            pm.write_int(entity + m_clrRender + 0x2, (rgbCT[2]))
                        
                        elif entity_team_id == team and tChams[0] == 1: #elif entity_team_id == 3:
                            pm.write_int(entity + m_clrRender, (rgbT[0]))
                            pm.write_int(entity + m_clrRender + 0x1, (rgbT[1]))
                            pm.write_int(entity + m_clrRender + 0x2, (rgbT[2]))
                    else:
                        pass
            except Exception as e:
                print(e)
                
def bhop_t(threadname):

    while True:
        time.sleep(0.5)
        while bhop == 1:
            try:
                if pm.read_int(client + dwLocalPlayer):
                    player = pm.read_int(client + dwLocalPlayer)
                    force_jump = client + dwForceJump
                    on_ground = pm.read_int(player + m_fFlags)

                    if keyboard.is_pressed("space"):
                        if on_ground == 257:
                            pm.write_int(force_jump, 5)
                            time.sleep(0.17)
                            pm.write_int(force_jump, 4)
            except:
                print("Bhop Error")
                        
def glow_t(threadname):

    while True:
        time.sleep(0.5)
        while glow == 1:
            try:
                player = pm.read_int(client + dwLocalPlayer)
                glow_manager = pm.read_int(client + dwGlowObjectManager)

                if (player):
                    team  = pm.read_int(player + m_iTeamNum)
            
                    for i in range(1, 32):
                        entity = pm.read_int(client + dwEntityList + i * 0x10)
                
                        if (entity):
                            entity_team_id = pm.read_int(entity + m_iTeamNum)
                            entity_glow = pm.read_int(entity + m_iGlowIndex)
                    
                            if (entity_team_id != team) and tGlow[1] == 1:
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(rgbGlowE[0]))
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(rgbGlowE[1]))
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(rgbGlowE[2]))
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(rgbGlowE[3]))
                        
                                pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)
                        
                            if (entity_team_id == team) and tGlow[0] == 1:
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(rgbGlowT[0]))
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(rgbGlowT[1]))
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(rgbGlowT[2]))
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(rgbGlowT[3]))
                        
                                pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)
                        
            except:
                print("Glow Error")
            
def thirdperson_t(threadname):
    
    switch = 0
    while True:
        time.sleep(0.5)
        while third == 1:
            try:
                localplayer = pm.read_int(client + dwLocalPlayer)
                if keyboard.is_pressed(thirdkey) and switch == 0:
                    pm.write_int(localplayer + m_iObserverMode, 1)
                    switch = 1
                    time.sleep(0.5)
                elif keyboard.is_pressed(thirdkey) and switch == 1:
                    pm.write_int(localplayer + m_iObserverMode, 0)
                    switch = 0
                    time.sleep(0.5)
            except:
                print("Third Error")
                
def fov_t(threadname):
    
    switch = 0
    player = pm.read_int(client + dwEntityList)
    deffov = pm.read_int(player + m_iDefaultFOV)
    while True:
        time.sleep(0.5)
        while fov == 1:
            try:
                if keyboard.is_pressed(fovkey) and switch == 0:
                    pm.write_int(player + m_iDefaultFOV, infov)
                    switch = 1
                    time.sleep(0.5)
                if keyboard.is_pressed(fovkey) and switch == 1:
                    pm.write_int(player + m_iDefaultFOV, deffov)
                    switch = 0
                    time.sleep(0.5)
                if fov == 0:
                    pm.write_int(player + m_iDefaultFOV, deffov)
                    switch = 0
                    time.sleep(0.5)
                time.sleep(0.1)
            except:
                print("Fov Error")
            
def changer_t(threadname):
    t = requests.get("https://raw.githubusercontent.com/Tumpok/offsets/main/csgo.json")
    dwLocalPlayer = int(t.json()['signatures']['dwLocalPlayer'])
    m_hMyWeapons = int(t.json()['netvars']['m_hMyWeapons'])
    dwEntityList = int(t.json()['signatures']['dwEntityList'])
    m_iItemIDHigh = int(t.json()['netvars']['m_iItemIDHigh'])
    dwClientState = int(t.json()['signatures']['dwClientState'])
    m_nFallbackPaintKit = int(t.json()['netvars']['m_nFallbackPaintKit'])
    m_iItemDefinitionIndex = int(t.json()['netvars']['m_iItemDefinitionIndex'])
    m_flFallbackWear = int(t.json()['netvars']['m_flFallbackWear'])
    m_nFallbackStatTrak = int(t.json()['netvars']['m_nFallbackStatTrak'])
    m_szCustomName = int(t.json()['netvars']['m_szCustomName'])

    print("Skin swapper has launched.")
    handle = pymem.Pymem("csgo.exe")
    client_dll = pymem.process.module_from_name(handle.process_handle, "client.dll").lpBaseOfDll
    engine_dll = pymem.process.module_from_name(handle.process_handle, "engine.dll").lpBaseOfDll

    def force_full_update():
        engine_state = handle.read_int(engine_dll + dwClientState)
        handle.write_int(engine_state + 0x174, -1)

    def statTrak(value):
        handle.write_int(currentWeapon + m_nFallbackStatTrak, value)

    while True:
        time.sleep(0.5)
        while changer == 1:
            try:
                f = open('changer.json', "r")
                config = json.load(f)

                localPlayer = handle.read_int(client_dll + dwLocalPlayer)
                for i in range(8):
                    currentWeapon = handle.read_int(localPlayer + m_hMyWeapons + i * 0x4) & 0xfff
                    currentWeapon = handle.read_int(client_dll + dwEntityList + (currentWeapon - 1) * 0x10)
                    if currentWeapon == 0:
                        continue

                    weaponID = handle.read_short(currentWeapon + m_iItemDefinitionIndex)
                    fallbackPaint = 0
                    fallbackWear = 0.01
                    itemIDHigh = -1

                    for (k, v) in config.items():
                        if weaponID == config[k]["id"]:
                            fallbackPaint = config[k]["skinID"]
                            fallbackWear = config[k]["float"]
                            if "statTrak" in config[k]:
                                statTrak(config[k]["statTrak"])
                            if "name" in config[k]:
                                handle.write_string(currentWeapon + m_szCustomName, config[k]["name"])
                    handle.write_int(currentWeapon + m_iItemIDHigh, itemIDHigh)
                    handle.write_int(currentWeapon + m_nFallbackPaintKit, fallbackPaint)
                    handle.write_float(currentWeapon + m_flFallbackWear, fallbackWear)
        
        
                    if keyboard.is_pressed('f1'):
                        force_full_update()
            except:
                print("Changer Error")
            

if __name__ == "__main__":
    
    trigger_t = Thread(target=trigger_t, args=("Trigger_t",))
    trigger_t.start()
    radar_t = Thread(target=radar_t, args=("Radar_t",))
    radar_t.start()
    chams_t = Thread(target=chams_t, args=("Chams_t",))
    chams_t.start()
    bhop_t = Thread(target=bhop_t, args=("Bhop_t",))
    bhop_t.start()
    glow_t = Thread(target=glow_t, args=("Glow_t",))
    glow_t.start()
    thirdperson_t = Thread(target=thirdperson_t, args=("Thirdperson_t",))
    thirdperson_t.start()
    fov_t = Thread(target=fov_t, args=("Fov_t",))
    fov_t.start()
    changer_t = Thread(target=changer_t, args=("Changer_t",))
    changer_t.start()
    
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())