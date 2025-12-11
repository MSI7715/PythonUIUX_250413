from cal2 import Ui_Dialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

'''
# 兩個對話框做加法計算函式
def clicked_add():
    # 抓左邊對話框數值(資料型態:字串str)    
    a = ui.lineEdit.text()
    # 抓右邊對話框數值(資料型態:字串str)
    b = ui.lineEdit_2.text()
    # 兩個對話框相加，先把str轉數值(int)做數學加法，再轉回字串回傳
    c = str(int(a) + int(b))
    # 回傳相加後數字結果顯示在label
    ui.label.setText(c)

# 兩個對話框做減法計算函式
def clicked_minus():
    # 抓左邊對話框數值(資料型態:字串str)    
    a = ui.lineEdit.text()
    # 抓右邊對話框數值(資料型態:字串str)
    b = ui.lineEdit_2.text()
    # 兩個對話框相加，先把str轉數值(int)做數學減法，再轉回字串回傳
    c = str(int(a) - int(b))
    # 回傳相減後數字結果顯示在label
    ui.label.setText(c)

ui.pushButton.clicked.connect(clicked_add)
ui.pushButton_2.clicked.connect(clicked_minus)
'''

#===================================================================

def num():
    # 抓左邊對話框數值(資料型態:字串str)    
    a = ui.lineEdit.text()
    # 抓右邊對話框數值(資料型態:字串str)
    b = ui.lineEdit_2.text()
    # 回傳a, b參數給其他function呼叫使用
    return a, b

def add():
    # 從num函式拿取a, b參數
    a, b = num()
    c = str(int(a) + int(b))
    ui.label.setText(c)
    # messageBox - 提示訊息
    msg = QMessageBox()
    # messageBox標題
    msg.setWindowTitle("Answer")
    # messageBox結果顯示
    msg.setInformativeText(str(c))
    msg.exec_()

def minus():
    # 從num函式拿取a, b參數
    a, b = num()
    c = str(int(a) - int(b))
    ui.label.setText(c)

def div():
    # 從num函式拿取a, b參數
    a, b = num()

    if (int(b) == 0):
        # messageBox - 提示訊息
        msg = QMessageBox()
        # messageBox標題
        msg.setWindowTitle("Error")
        # messageBox結果顯示        
        msg.setInformativeText("被除數不可為0")
        msg.exec_()

    else:
        c = str(int(a) / int(b))
        ui.label.setText(c)     

# 執行按鈕時對應計算方法
ui.pushButton.clicked.connect(add)
ui.pushButton_2.clicked.connect(minus)
ui.pushButton_3.clicked.connect(div)

widget.show()
app.exec_()