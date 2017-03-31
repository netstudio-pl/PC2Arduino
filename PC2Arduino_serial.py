#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import serial
from ui import Ui_MainForm
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QTimer

class ArduinoSerial(Ui_MainForm):
        def __init__(self, dialog):
                Ui_MainForm.__init__(self)
                self.setupUi(dialog)
                self.timer = QTimer()
                self.txtLog.appendPlainText(u"Aplikacja gotowa do połączenia")
                                
                #definicje własnych połączeń sygnałów do slotów (połączenie przycisku i funkcji)
                self.btnConnect.clicked.connect(self.arduinoConnect)
                self.btnDisconnect.clicked.connect(self.arduinoDisconnect)
                self.btnExit.clicked.connect(self.appClose)
                self.timer.timeout.connect(self.timerEvent)          
                self.polaczono = False             
          
        def arduinoConnect(self):
                self.serialPort = serial.Serial(str(self.cboPort.currentText()), 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, 0.100)
                
                if self.polaczono == False:
                        if (self.serialPort.isOpen()):
                                self.serialPort.close()
                        try:
                                self.serialPort.open()
                                self.polaczono = True
                                self.btnConnect.setText(u"Połączono")
                                self.btnConnect.setStyleSheet("background-color: green")
                                self.txtLog.appendPlainText(u"Połączono z Arduino na porcie " + self.serialPort.portstr)
                        except:
                                self.polaczono = False
                                self.btnConnect.setStyleSheet("background-color: red")
                                self.txtLog.appendPlainText(u"Błąd połączenia")
                        self.timer.start(10)

        def timerEvent(self):                    
                if (self.serialPort.inWaiting()):                               
                        self.lcdNumber.display(int(self.serialPort.readline()))

        def arduinoDisconnect(self):
                if self.polaczono == True:
                        self.txtLog.appendPlainText(u"Zakończono połączenie z Arduino...")
                        self.btnConnect.setText(u"Połącz")
                        self.btnConnect.setStyleSheet("background-color: None")                              
                        self.polaczono = False
                        self.serialPort.close()
                self.timer.stop()
                self.lcdNumber.display(0)

        def appClose(self):
                if self.polaczono == True:
                        self.txtLog.appendPlainText(u"Najpierw zakończ połączenie z Arduino!")
                else:
                        sys.exit(app.exec_())
                
if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = ArduinoSerial(dialog)
    dialog.show()
    sys.exit(app.exec_())




