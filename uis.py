# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(764, 508)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 60, 711, 73))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(30, 170, 631, 81))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setAutoFillBackground(False)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.charuanniu = QtWidgets.QPushButton(self.centralwidget)
        self.charuanniu.setGeometry(QtCore.QRect(0, 0, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.charuanniu.setFont(font)
        self.charuanniu.setObjectName("charuanniu")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 0, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 0, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.chaxunanniu = QtWidgets.QPushButton(self.centralwidget)
        self.chaxunanniu.setGeometry(QtCore.QRect(80, 0, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.chaxunanniu.setFont(font)
        self.chaxunanniu.setObjectName("chaxunanniu")
        self.pushButton_beifen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_beifen.setGeometry(QtCore.QRect(400, 0, 75, 23))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.pushButton_beifen.setFont(font)
        self.pushButton_beifen.setObjectName("pushButton_beifen")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(30, 260, 631, 192))
        self.tableView.setObjectName("tableView")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(670, 170, 71, 281))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_shuaxin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shuaxin.setGeometry(QtCore.QRect(320, 0, 75, 23))
        self.pushButton_shuaxin.setObjectName("pushButton_shuaxin")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "规范条例查询系统"))
        self.pushButton.setText(_translate("mainWindow", "查询"))
        self.label.setText(_translate("mainWindow", "条例解释："))
        self.label_2.setText(_translate("mainWindow", "输入查询条件："))
        self.charuanniu.setText(_translate("mainWindow", "插入模式"))
        self.pushButton_3.setText(_translate("mainWindow", "删除"))
        self.pushButton_4.setText(_translate("mainWindow", "修改"))
        self.chaxunanniu.setText(_translate("mainWindow", "查询模式"))
        self.pushButton_beifen.setText(_translate("mainWindow", "备份"))
        self.pushButton_shuaxin.setText(_translate("mainWindow", "刷新"))