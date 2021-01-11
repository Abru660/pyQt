# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 17:31:46 2021

@author: paul
"""

import PyQt5.QtWidgets as qtw

class ToDo():
    def __init__(self,name,state,checkbox):
        self.value = name
        self.state = state
        self.checkbox = checkbox

    def getName(self):
        return self.value
    
    def getState(self):
        return self.state
    
    def getCheckbox(self):
        return self.checkbox
    
    def setName(self, name):
        self.value = name
    
    def setState(self, state):
        self.state = state
    
    def setCheckbox(self, checkbox):
        self.checkbox = checkbox
    def __str__(self):
        result = "" + str(self.value) +"," + str(self.getState()) + "," + str(self.getCheckbox())
        return result
    


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.todos = []
        self.initialize()

        self.setWindowTitle("My To Do list")
        self.setLayout(qtw.QVBoxLayout())
        self.setUI()
        self.setTodos()

        self.show()

    def setTodos(self):
        # for todo in self.todos:
        for i in range(len(self.todos)):
            todo = self.todos[i]
            # container
            todoContainer = qtw.QWidget()
            todoContainer.setLayout(qtw.QHBoxLayout())

            #checkbox
            checkbox = qtw.QCheckBox()
            checkbox.setChecked(todo.getState())
            todoContainer.layout().addWidget(checkbox)
            self.todos[i].setCheckbox(checkbox)
            checkbox.stateChanged.connect(self.checkboxStateChanged)

            # label
            label = qtw.QLabel(todo.getName())
            todoContainer.layout().addWidget(label)

            self.layout().addWidget(todoContainer)
            
    def setUI(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        
        self.add = qtw.QPushButton("Add to do",  clicked = self.addToDo)
        self.remove = qtw.QPushButton("remove to do",  clicked = self.removeToDo)
        self.save = qtw.QPushButton("save",  clicked = self.saveToDo)
        container.layout().addWidget(self.add,0,0)
        container.layout().addWidget(self.remove,1,0)
        container.layout().addWidget(self.save,2,0)
        self.layout().addWidget(container)
        
    def addToDo(self):
        todoQuestion = qtw.QInputDialog.getText(self, 'input dialog', 'What should you do ?')
        todo = ToDo(todoQuestion[0],False,False)
        self.todos.append(todo)
        
        todoContainer = qtw.QWidget()
        todoContainer.setLayout(qtw.QHBoxLayout())

        #checkbox
        checkbox = qtw.QCheckBox()
        checkbox.setChecked(todo.getState())
        todoContainer.layout().addWidget(checkbox)
        todo.setCheckbox(checkbox)
        checkbox.stateChanged.connect(self.checkboxStateChanged)

        # label
        label = qtw.QLabel(todo.getName())
        todoContainer.layout().addWidget(label)

        self.layout().addWidget(todoContainer)
        
        
    def removeToDo(self):
        for i in range(self.layout().count()):
            self.layout().itemAt(i).widget().deleteLater()
        self.setUI()
        elemRemoved = True
        while elemRemoved:
            for i in range(len(self.todos)):
                if i == len(self.todos)-1:
                    elemRemoved = False
                if self.todos[i].getCheckbox().isChecked():
                    self.todos.pop(i)
                    break
                
    
        self.setTodos()
        
    def saveToDo(self):
        toSave = ""
        file  = open("todolistsave.txt","w")
        for e in self.todos:
            toSave += "" + str(e.getName()) +":" + str(e.getState()) + ":" + str(e.getCheckbox().isChecked()) + "\n"
        file.write(toSave)
        file.close()
        msg = qtw.QMessageBox()
        msg.setText("To dos have been saved")
        msg.setWindowTitle("Information")
        msg.setStandardButtons(qtw.QMessageBox.Ok)
        msg.exec_()
        
    def initialize(self):
        try:
            file  = open("todolistsave.txt","r")
            lines = file.readlines()
            for string in lines:
                r = string.rstrip("\n").split(":")
                state = "True" == r[1]
                checkbox = "True" == r[2]
                tmp = ToDo(r[0],state,checkbox)
                self.todos.append(tmp)
            file.close()
        except IOError:
            print("File not accessible")

        
    def checkboxStateChanged(self):
        for i in range(len(self.todos)):
            if (self.todos[i].getCheckbox()):
                self.todos[i].setState(self.todos[i].getCheckbox().isChecked())
        
        

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()