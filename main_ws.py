from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from file_oper import Ui_MainWindow
import sys
import os
 
class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.actionfileopen.triggered.connect(self.open_file)
 
    def open_file(self):
        fileName,fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), 
        "All Files(*);;Text Files(*.txt)")
        print(fileName)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

