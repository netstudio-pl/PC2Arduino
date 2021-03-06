# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(521, 414)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainForm.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ArduinoUNO.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainForm.setWindowIcon(icon)
        MainForm.setAutoFillBackground(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(MainForm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 171, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cboPort = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cboPort.setObjectName("cboPort")
        self.cboPort.addItem("")
        self.cboPort.addItem("")
        self.cboPort.addItem("")
        self.cboPort.addItem("")
        self.cboPort.addItem("")
        self.cboPort.addItem("")
        self.cboPort.addItem("")
        self.cboPort.addItem("")
        self.cboPort.addItem("")
        self.cboPort.addItem("")
        self.verticalLayout.addWidget(self.cboPort)
        self.btnConnect = QtWidgets.QPushButton(self.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.btnConnect.setPalette(palette)
        self.btnConnect.setObjectName("btnConnect")
        self.verticalLayout.addWidget(self.btnConnect)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnDisconnect = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnDisconnect.setObjectName("btnDisconnect")
        self.verticalLayout.addWidget(self.btnDisconnect)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btnExit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnExit.setObjectName("btnExit")
        self.verticalLayout.addWidget(self.btnExit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(MainForm)
        self.label.setGeometry(QtCore.QRect(220, 20, 261, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ArduinoUNO.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(MainForm)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 210, 331, 191))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtLog = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.txtLog.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.txtLog.setPalette(palette)
        self.txtLog.setObjectName("txtLog")
        self.verticalLayout_2.addWidget(self.txtLog)
        self.lcdNumber = QtWidgets.QLCDNumber(MainForm)
        self.lcdNumber.setGeometry(QtCore.QRect(350, 220, 161, 81))
        self.lcdNumber.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(MainForm)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(350, 309, 161, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnLed = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnLed.setObjectName("btnLed")
        self.verticalLayout_3.addWidget(self.btnLed)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)

        self.retranslateUi(MainForm)
        self.btnExit.clicked.connect(MainForm.close)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Arduino connect"))
        self.cboPort.setToolTip(_translate("MainForm", "<html><head/><body><p><span style=\" font-size:10pt;\">Wybierz port COM do połączenia z Arduino</span></p></body></html>"))
        self.cboPort.setCurrentText(_translate("MainForm", "COM1"))
        self.cboPort.setItemText(0, _translate("MainForm", "COM1"))
        self.cboPort.setItemText(1, _translate("MainForm", "COM2"))
        self.cboPort.setItemText(2, _translate("MainForm", "COM3"))
        self.cboPort.setItemText(3, _translate("MainForm", "COM4"))
        self.cboPort.setItemText(4, _translate("MainForm", "COM5"))
        self.cboPort.setItemText(5, _translate("MainForm", "COM6"))
        self.cboPort.setItemText(6, _translate("MainForm", "COM7"))
        self.cboPort.setItemText(7, _translate("MainForm", "COM8"))
        self.cboPort.setItemText(8, _translate("MainForm", "COM9"))
        self.cboPort.setItemText(9, _translate("MainForm", "COM10"))
        self.btnConnect.setToolTip(_translate("MainForm", "<html><head/><body><p><span style=\" font-size:10pt;\">Ten przycisk nawiązuje komunikację z płytką Arduino</span></p></body></html>"))
        self.btnConnect.setText(_translate("MainForm", "Połącz z Arduino"))
        self.btnDisconnect.setToolTip(_translate("MainForm", "<html><head/><body><p><span style=\" font-size:10pt;\">Ten przycisk zamyka komunikację z płytką Arduino</span></p></body></html>"))
        self.btnDisconnect.setText(_translate("MainForm", "Rozłącz z Arduino"))
        self.btnExit.setToolTip(_translate("MainForm", "<html><head/><body><p><span style=\" font-size:10pt;\">Ten przycisk zamyka aplikację</span></p></body></html>"))
        self.btnExit.setText(_translate("MainForm", "Zamknij program"))
        self.txtLog.setToolTip(_translate("MainForm", "<html><head/><body><p><span style=\" font-size:10pt;\">Tu wyświetlane są Informacje z aplikacji</span></p></body></html>"))
        self.lcdNumber.setToolTip(_translate("MainForm", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:400; font-style:normal;\">Tu wyświetlane są wartości z Arduino</span></p></body></html>"))
        self.btnLed.setToolTip(_translate("MainForm", "<html><head/><body><p><span style=\" font-size:10pt;\">Ten przycisk zapala lub gasi diodę LED w Arduino</span></p></body></html>"))
        self.btnLed.setText(_translate("MainForm", "Włącz LED"))

