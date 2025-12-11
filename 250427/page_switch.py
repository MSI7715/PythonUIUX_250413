from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys, p1, p2

# 建立UI視窗
app = QApplication(sys.argv)
# 第一個視窗
widget = QWidget()
ui = p1.Ui_Dialog()
ui.setupUi(widget)
# 第二個視窗
ui2 = p2.Ui_Dialog()
widget2 = QWidget()
ui2.setupUi(widget2)


def button_click():
    print("Hello World")
    widget2.show()
    widget.close()

# 按鈕事件
ui.pushButton.clicked.connect(button_click)

# 顯示視窗
widget.show()
app.exec_()