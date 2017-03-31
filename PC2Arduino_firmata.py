#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from ui import Ui_MainForm
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from pyfirmata import Arduino, util #biblioteka do obsługi komunikacji z Arduino

class ArduinoFirmata(Ui_MainForm):    
        def __init__(self, dialog):
                Ui_MainForm.__init__(self)
                self.setupUi(dialog)
                self.timer = QTimer()
                self.txtLog.appendPlainText(u"Aplikacja gotowa do połączenia")
                                
                #definicje własnych połączeń sygnałów do slotów
                self.btnConnect.clicked.connect(self.arduinoConnect)
                self.btnDisconnect.clicked.connect(self.arduinoDisconnect)
                self.btnExit.clicked.connect(self.appClose)
                self.timer.timeout.connect(self.readAnalog)
                self.btnLed.clicked.connect(self.arduinoLed)
                
                self.analogPin = 0             # Arduino port A0
                self.ledPin = 2                # Arduino port D2
                self.polaczono = False            
 
        def arduinoConnect(self):               #połączenie z Arduino
                if self.polaczono == False:
                        try:
                                #obsługa komunikacji z Arduino
                                self.board = Arduino(str(self.cboPort.currentText()))
                                iterator = util.Iterator(self.board)
                                iterator.start()
                                self.board.analog[self.analogPin].enable_reporting()

                                #zmiana ui (button)
                                self.polaczono = True
                                self.btnConnect.setText(u"Połączono")
                                self.btnConnect.setStyleSheet("background-color: green")
                                self.txtLog.appendPlainText(u"Połączono z Arduino")
                        except:
                                #zmiana ui (button)
                                self.polaczono = False
                                self.btnConnect.setStyleSheet("background-color: red")
                                self.txtLog.appendPlainText(u"Błąd połączenia")
                                self.lcdNumber.display(0)
                        #except BaseException as err:
                        #        print("Błąd: " + str(err))
                        self.timer.start(100)

        def readAnalog(self):                   #odczyt wartości analogowej z Arduino
                value = self.board.analog[self.analogPin].read()
                  
                if value is not None:
                    analogValue = value * 1000
                    self.lcdNumber.display(int(analogValue))

        def arduinoLed(self):                   #zapala lub gasi diodę LED w Arduino
                if self.btnLed.text() == u"Włącz LED":
                        self.btnLed.setText(u"Wyłącz LED")
                        self.board.digital[self.ledPin].write(1)
                else:
                        self.btnLed.setText(u"Włącz LED")
                        self.board.digital[self.ledPin].write(0)   
                                
        def arduinoDisconnect(self):            #rozłączenie z Arduino
                if self.polaczono == True: 
                        self.txtLog.appendPlainText(u"Zakończono połączenie z Arduino...")
                        self.btnConnect.setText(u"Połącz")
                        self.btnConnect.setStyleSheet("background-color: None")                              
                        self.polaczono = False
                        self.board.exit()
                self.timer.stop()
                self.lcdNumber.display(0)

        def appClose(self): 
                if self.polaczono == True:      #jeżeli było połaczenie to najpierw należy się rozłączyć
                        self.txtLog.appendPlainText(u"Najpierw zakończ połączenie z Arduino!")
                else:                           #zamknięcie aplikacji
                        sys.exit(app.exec_())
                
if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = ArduinoFirmata(dialog)
    dialog.show()
    sys.exit(app.exec_())







