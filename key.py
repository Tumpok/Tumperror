from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from wmi import WMI
import os


hwid = WMI().Win32_ComputerSystemProduct()[0].UUID
keys = 'https://raw.githubusercontent.com/Tumpok/kshw/main/kshw.json'
response = requests.get(keys).json()
user_key = int(response["signatures"][hwid])

key = open('key.txt', 'r')
keyln = key.readlines()
key.close()
filekey = keyln[0].rstrip()

if int(filekey) == user_key:
    os.startfile("tmc.exe")
    os.abort()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(284, 278)
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 75);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 110, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap("prj.jpg"))

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 160, 261, 41))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 210, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 60, 261, 41))
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.pushButton.clicked.connect(self.keycheck)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter your personal key"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.label_2.setText(_translate("MainWindow", "HWID:"))
        self.lineEdit_2.setText(_translate("MainWindow", hwid))
        
    def keycheck(self, state):
        tpdkey = self.lineEdit.text()
        if int(tpdkey) == user_key:
            key = open('key.txt', 'r')
            keyln = key.readlines()
            key.close()
            keyln[0] = tpdkey
            save_changes = open('key.txt', 'w')
            save_changes.writelines(keyln)
            save_changes.close()
            os.startfile("ts.py")

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Wrong key")
            msg.setIcon(QMessageBox.Warning)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
