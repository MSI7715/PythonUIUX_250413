from cal import Ui_Dialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

def button(value):
    # 取得label內的文字
    a = ui.label.text()
    if a == '0':
        a = ''
    a = a + value    
    # 轉換label內的文字
    ui.label.setText(a)

def button_reaction():
    button("1")

def button_reaction():
    button(1)
    

ui.pushButton.clicked.connect(button_reaction)
# ui.pushButton_2.clicked.connect(button_reaction2)

widget.show()
app.exec_()