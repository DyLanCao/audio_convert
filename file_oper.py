from pyqtgraph import PlotWidget
import numpy as np
import pyqtgraph as pq

from PyQt5 import QtCore, QtGui, QtWidgets
 
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionfileopen = QtWidgets.QAction(MainWindow)
        self.actionfileopen.setObjectName("actionfileopen")
        self.menufile.addAction(self.actionfileopen)
        self.menubar.addAction(self.menufile.menuAction())
 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.plotWidget_ted = PlotWidget(self)
        self.plotWidget_ted.setGeometry(QtCore.QRect(5,5,800,600))

        self.data1 = np.random.normal(size=300)
        self.curve2 = self.plotWidget_ted.plot(self.data1,name="mode2")
        self.ptr1 = 0

        self.timer = pq.QtCore.QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(50)


    def update_data(self):
        self.data1[:-1] = self.data1[1:]
        self.data1[-1] = np.random.normal()

        self.curve2.setData(self.data1)

        self.ptr1 += 1
        self.curve2.setPos(self.ptr1,0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "file"))

