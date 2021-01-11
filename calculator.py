# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 09:42:20 2021

@author: paul
"""

import PyQt5.QtWidgets as qtw

history = []



class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        
        self.setLayout(qtw.QVBoxLayout())
        self.setUI()

        self.show()

    def setUI(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        self.btns = []
        for i in range(0,10):
            self.btns.append(qtw.QPushButton(str(i), clicked = self.onClick))
            
        self.input1 = qtw.QLineEdit()
        

        self.enter = qtw.QPushButton("Enter", clicked = self.onClick)
        self.clear = qtw.QPushButton("clear", clicked = self.onClick)
        
        self.plus = qtw.QPushButton("+", clicked = self.onClick)
        self.minus = qtw.QPushButton("-", clicked = self.onClick)
        self.div = qtw.QPushButton("/", clicked = self.onClick)
        self.time = qtw.QPushButton("*", clicked = self.onClick)
        

        # set layout
        container.layout().addWidget(self.input1,0, 0, 1 , 5)
        
        container.layout().addWidget(self.enter,1, 0, 1 , 2)
        container.layout().addWidget(self.clear,1, 2, 1 , 3)
        
        container.layout().addWidget(self.plus,2, 4)
        container.layout().addWidget(self.minus,3, 4)
        container.layout().addWidget(self.div,4, 4)
        container.layout().addWidget(self.time,5, 4)
        
        container.layout().addWidget(self.btns[7],2, 0 )
        container.layout().addWidget(self.btns[8],2,1)
        container.layout().addWidget(self.btns[9],2, 2 )
        
        container.layout().addWidget(self.btns[4],3, 0 )
        container.layout().addWidget(self.btns[5],3, 1 )
        container.layout().addWidget(self.btns[6],3, 2 )

        container.layout().addWidget(self.btns[1],4, 0 )
        container.layout().addWidget(self.btns[2],4, 1 )
        container.layout().addWidget(self.btns[3],4, 2 )

        container.layout().addWidget(self.btns[0],5,0, 1, 3 )


        self.layout().addWidget(container)
    
    def onClick(self):
        button = self.sender()
        if (button == self.btns[0]):
            self.input1.setText(self.input1.text() + "0")
        elif (button ==self.btns[1]):
            self.input1.setText(self.input1.text() + "1")
        elif (button == self.btns[2]):
            self.input1.setText(self.input1.text() + "2")
        elif (button == self.btns[3]):
            self.input1.setText(self.input1.text() + "3")
        elif (button == self.btns[4]):
            self.input1.setText(self.input1.text() + "4")
        elif (button == self.btns[5]):
            self.input1.setText(self.input1.text() + "5")
        elif (button == self.btns[6]):
            self.input1.setText(self.input1.text() + "6")
        elif (button == self.btns[7]):
            self.input1.setText(self.input1.text() + "7")
        elif (button == self.btns[8]):
            self.input1.setText(self.input1.text() + "8")
        elif (button == self.btns[9]):
            self.input1.setText(self.input1.text() + "9")
        elif (button == self.plus):
            if (self.isOnProgress(self.input1.text())):
                history.append(self.input1.text())
                self.input1.setText(self.calculate(self.input1.text()) + " + ")
            else:
                self.input1.setText(self.input1.text() + " + ")
            
        elif (button == self.minus):
            if (self.isOnProgress(self.input1.text())):
                history.append(self.input1.text())
                self.input1.setText(self.calculate(self.input1.text()) + " - ")
            else:
                self.input1.setText(self.input1.text() + " - ")
        elif (button == self.div):
            if (self.isOnProgress(self.input1.text())):
                history.append(self.input1.text())
                self.input1.setText(self.calculate(self.input1.text()) + " / ")
            else:
                self.input1.setText(self.input1.text() + " / ")

        elif (button == self.time):
            if (self.isOnProgress(self.input1.text())):
                history.append(self.input1.text())
                self.input1.setText(self.calculate(self.input1.text()) + " * ")
            else:
                self.input1.setText(self.input1.text() + " * ")
                
        elif (button == self.enter):
            history.append(self.input1.text())
            self.input1.setText(self.calculate(self.input1.text()))
        elif (button == self.clear):
            self.input1.setText("")
        
        

    def isOnProgress(self,string):
        if "+" in string or "*" in string or "-" in string or "/" in string:
            return True
        else:
            return False
    
    def calculate(self,string):
        if "+" in string:
            numbers = string.replace(" ", "").split("+")
            return str(float(numbers[0]) + float(numbers[1]))
        elif "-" in string:
            numbers = string.replace(" ", "").split("-")
            return str(float(numbers[0]) - float(numbers[1]))
        elif "*" in string:
            numbers = string.replace(" ", "").split("*")
            return str(float(numbers[0]) * float(numbers[1]))
        elif "/" in string:
            numbers = string.replace(" ", "").split("/")
            if (int(numbers[1]) == 0):
                   return ""
            return str(float(float(numbers[0]) / float(numbers[1])))
            

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()