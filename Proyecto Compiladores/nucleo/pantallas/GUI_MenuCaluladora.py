# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(683, 479)
        MainWindow.setStyleSheet("background-image: url(:/menu/WhatsApp Image 2022-08-10 at 1.30.55 PM.jpeg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnCalculadora = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalculadora.setGeometry(QtCore.QRect(160, 380, 141, 51))
        self.btnCalculadora.setStyleSheet("font: 75 bold 14pt \"Cantarell\";\n"
"color: \"Black\";")
        self.btnCalculadora.setObjectName("btnCalculadora")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(360, 380, 141, 51))
        self.btnSalir.setStyleSheet("font: 81  bold 14pt \"Cantarell\";\n"
"color: \"black\";")
        self.btnSalir.setObjectName("btnSalir")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 391, 121))
        self.label.setStyleSheet("font: 81 bold 14pt \"Cantarell\";\n"
"\n"
"color: \"black\";\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 130, 141, 141))
        self.label_2.setStyleSheet("border-image: url(:/logo/logo-is.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu"))
        self.btnCalculadora.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\"><br/></span></p></body></html>"))
        self.btnCalculadora.setText(_translate("MainWindow", "Calculadora"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#040404;\">GRUPO # 1</span></p><p align=\"center\"><span style=\" font-size:24pt; color:#040404;\">II PAC 2022</span></p></body></html>"))
#import recursosMenu_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())