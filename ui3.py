# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(366, 616)
        MainWindow.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 20, 201, 51))
        self.checkBox.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 90, 201, 51))
        self.checkBox_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 160, 201, 51))
        self.checkBox_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 230, 201, 51))
        self.checkBox_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 300, 201, 51))
        self.checkBox_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_5.setObjectName("checkBox_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 570, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 30, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 50, 121, 16))
        self.label_3.setObjectName("label_3")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 370, 201, 51))
        self.checkBox_6.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_6.setObjectName("checkBox_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 430, 113, 31))
        self.lineEdit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 470, 111, 31))
        self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 440, 201, 51))
        self.checkBox_7.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_7.setObjectName("checkBox_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 500, 141, 20))
        self.label_4.setObjectName("label_4")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 530, 201, 51))
        self.checkBox_8.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.checkBox_8.setObjectName("checkBox_8")
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
        self.label.setText(_translate("MainWindow", "Created by Tumpok"))
        self.label_2.setText(_translate("MainWindow", "Trigger key is"))
        self.label_3.setText(_translate("MainWindow", " \"mid mouse button\""))
        self.checkBox_6.setText(_translate("MainWindow", "Thirdperson"))
        self.lineEdit.setText(_translate("MainWindow", "120"))
        self.pushButton.setText(_translate("MainWindow", "apply"))
        self.checkBox_7.setText(_translate("MainWindow", "Thirdperson"))
        self.label_4.setText(_translate("MainWindow", "FOV change key is \"v\""))
        self.checkBox_8.setText(_translate("MainWindow", "Aim Bot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())