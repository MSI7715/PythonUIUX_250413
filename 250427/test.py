from practice import Ui_Dialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

# 建立UI視窗
app = QApplication(sys.argv)

t = QTranslator()
with open('target2.txt') as f:
    lines = f.readlines()
    if lines[0] == 'jp':
        t.load('jpa.qm')
    elif lines[0] == 'Chi':
        t.load('tra.qm')
    
app.installTranslator(t)

'''
j = QTranslator()
j.load('jpa.qm')
app.installTranslator(j)
'''

widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

def button_reaction():
    print("hello world")

ui.pushButton.clicked.connect(button_reaction)

# 顯示視窗
widget.show()
app.exec_()