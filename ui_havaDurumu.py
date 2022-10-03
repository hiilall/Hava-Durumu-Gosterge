# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'havaDurumu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 502)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(550, 502))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(560, 500))
        self.centralwidget.setMaximumSize(QtCore.QSize(560, 500))
        self.centralwidget.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(245, 213, 172, 255));")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frameSicaklik = QtWidgets.QFrame(self.centralwidget)
        self.frameSicaklik.setMinimumSize(QtCore.QSize(300, 300))
        self.frameSicaklik.setMaximumSize(QtCore.QSize(300, 300))
        self.frameSicaklik.setStyleSheet("QFrame{\n"
"    border-radius:150px;\n"
"    background-color: qconicalgradient(cx:0.51, cy:0.511364, angle:270.2, stop:0 rgba(255, 255, 255, 255), stop:0.04 rgba(255, 255, 0, 255), stop:0.08 rgba(255, 151, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"}\n"
"")
        self.frameSicaklik.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSicaklik.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSicaklik.setObjectName("frameSicaklik")
        self.frameNem = QtWidgets.QFrame(self.frameSicaklik)
        self.frameNem.setGeometry(QtCore.QRect(20, 20, 260, 260))
        self.frameNem.setMaximumSize(QtCore.QSize(260, 260))
        self.frameNem.setSizeIncrement(QtCore.QSize(260, 260))
        self.frameNem.setStyleSheet("QFrame{\n"
"    border-radius:130px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:0.999818, stop:0.15 rgba(255, 255, 255, 255), stop:0.4 rgba(113, 144, 255, 255), stop:1 rgba(69, 110, 255, 255));\n"
"    \n"
"}\n"
"")
        self.frameNem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameNem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameNem.setObjectName("frameNem")
        self.gridLayout_10.addWidget(self.frameSicaklik, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setStyleSheet("")
        self.frame_5.setObjectName("frame_5")
        self.labelDeger = QtWidgets.QLabel(self.frame_5)
        self.labelDeger.setGeometry(QtCore.QRect(20, 120, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDeger.setFont(font)
        self.labelDeger.setObjectName("labelDeger")
        self.gridLayout_10.addWidget(self.frame_5, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_10, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonManuel = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonManuel.setMinimumSize(QtCore.QSize(100, 30))
        self.radioButtonManuel.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonManuel.setFont(font)
        self.radioButtonManuel.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"border-radius: 15px;")
        self.radioButtonManuel.setObjectName("radioButtonManuel")
        self.verticalLayout.addWidget(self.radioButtonManuel)
        self.radioButtonOtomatik = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonOtomatik.setMinimumSize(QtCore.QSize(100, 30))
        self.radioButtonOtomatik.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonOtomatik.setFont(font)
        self.radioButtonOtomatik.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"border-radius: 15px;")
        self.radioButtonOtomatik.setObjectName("radioButtonOtomatik")
        self.verticalLayout.addWidget(self.radioButtonOtomatik)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label.setSizeIncrement(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalSliderNem = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderNem.setMinimumSize(QtCore.QSize(300, 0))
        self.horizontalSliderNem.setMaximumSize(QtCore.QSize(300, 16777215))
        self.horizontalSliderNem.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderNem.setObjectName("horizontalSliderNem")
        self.gridLayout_4.addWidget(self.horizontalSliderNem, 1, 1, 1, 1)
        self.horizontalSliderSicaklik = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderSicaklik.setMinimumSize(QtCore.QSize(300, 0))
        self.horizontalSliderSicaklik.setMaximumSize(QtCore.QSize(300, 16777215))
        self.horizontalSliderSicaklik.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSicaklik.setObjectName("horizontalSliderSicaklik")
        self.gridLayout_4.addWidget(self.horizontalSliderSicaklik, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelDeger.setText(_translate("MainWindow", "SICAKLIK:\n"
"NEM:"))
        self.radioButtonManuel.setText(_translate("MainWindow", "Manuel "))
        self.radioButtonOtomatik.setText(_translate("MainWindow", "Otomatik"))
        self.label_2.setText(_translate("MainWindow", "Nem"))
        self.label.setText(_translate("MainWindow", "Sıcaklık"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
