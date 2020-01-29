import sys
import uis
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import  QApplication,QMainWindow
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from operators import db_operator
import os
import shutil
from PyQt5.QtWidgets import QHeaderView

class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=uis.Ui_mainWindow()
        self.ui.setupUi(self)
        #self.ui.Qpush
        self.file_path = os.getcwd()
        self.db_path = self.file_path + '\mogo.db'

        self.operator = db_operator(self.db_path, 'regulations')
        # 初始化应用
        self.setWindowIcon(QIcon('1.ico'))
        self.init_client()
        # 设置菜单栏按钮
        self.ui.charuanniu.clicked.connect(self.setText_insert)
        self.ui.chaxunanniu.clicked.connect(self.find_mode)
        self.ui.pushButton_3.clicked.connect(self.delete)
        self.ui.pushButton_4.clicked.connect(self.update)
        self.ui.pushButton_beifen.clicked.connect(self.beifen)
        # 显示小图片
        self.ui.graphicsView.setStyleSheet("border-image: url(1.png);")
        # 查看数据表

        self.view_data()
        self.ui.pushButton_shuaxin.clicked.connect(self.view_data)




    def init_client(self):
        self.ui.chaxunanniu.setDown(True)
        self.ui.charuanniu.setDown(False)
        self.ui.pushButton.setText('查询')
        #self.ui.pushButton.clicked.disconnect(self.insert)
        self.ui.pushButton.clicked.connect(self.find)
        self.ui.plainTextEdit_2.setReadOnly(True)

    def find_mode(self):
        self.ui.chaxunanniu.setDown(True)
        self.ui.charuanniu.setDown(False)
        self.ui.pushButton.setText('查询')
        self.ui.pushButton.clicked.disconnect(self.insert)
        self.ui.pushButton.clicked.connect(self.find)
        self.ui.plainTextEdit_2.setReadOnly(True)


    def setText_insert(self):
        self.ui.chaxunanniu.setDown(False)
        self.ui.charuanniu.setDown(True)
        if self.ui.charuanniu.isDown():
            self.ui.pushButton.setText('写入')
            self.ui.pushButton.clicked.disconnect(self.find)
            self.ui.pushButton.clicked.connect(self.insert)
            if self.ui.plainTextEdit_2.isReadOnly():
                self.ui.plainTextEdit_2.setReadOnly(False)



    def insert(self):
        try:
            matters = self.ui.plainTextEdit.toPlainText()
            regulations = self.ui.plainTextEdit_2.toPlainText()
            if matters=='' or regulations =='':
                self.ui.statusbar.showMessage('插入内容不能为空，请重新输入！')
            else:
                self.operator.insert_db(regulations,matters)
                self.statusBar().showMessage('插入成功！')
        except:
            self.statusBar().showMessage('插入失败！')


    def find(self):
        matters = self.ui.plainTextEdit.toPlainText()
        # if self.operator.find_column(matters):
        regula = self.operator.find_db(matters)

        res = regula

        print(res)
        if len(regula)==0:
            self.statusBar().showMessage('没有查询到相似案例，可以添加到数据库！')
        else:
            res = str(list(regula)[0])
            res = res.strip("'()',")
            self.statusBar().showMessage('查询成功！')
            self.ui.plainTextEdit_2.setPlainText(res)



    def delete(self):
        try:
            matters = self.ui.plainTextEdit.toPlainText()
            regula = self.operator.find_db1(matters)
            print(regula)
            res = str(list(regula)[0])
            res = res.strip("'()',")

            # print(regulations[0])
            # print('---------')
            if len(res) == 0:
                self.statusBar().showMessage('删除失败！输入一字不差的的查询条件才可以删除哦！')

            else:
                self.operator.delete_db(matters)
                self.statusBar().showMessage('删除成功！')
        except:
            self.statusBar().showMessage('删除失败！输入一字不差的的查询条件才可以删除哦！')


    def update(self):
        if self.ui.plainTextEdit_2.isReadOnly():
            self.ui.plainTextEdit_2.setReadOnly(False)
        matters = self.ui.plainTextEdit.toPlainText()
        regulations = self.ui.plainTextEdit_2.toPlainText()
        if matters == '' or regulations == '':
            self.ui.statusbar.showMessage('修改内容不能为空，请重新输入！')
        else:
            self.operator.update_db(matters,regulations)
            self.statusBar().showMessage('修改成功！')

        # res = str(list(regula)[0])
        # res = res.strip("'()',")


    # 浏览数据
    def view_data(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('mogo.db')
        # 实例化一个可编辑数据模型
        db.open()
        self.model = QSqlTableModel()
        self.ui.tableView.setModel(self.model)

        self.model.setTable('regulations')  # 设置数据模型的数据表
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)  # 允许字段更改
        self.model.select()  # 查询所有数据
        # 设置表格头
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)#ResizeToContents

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, '条款解释')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, '行为规范')


    def beifen(self):
        import datetime
        try:
            curr_time = datetime.datetime.now()
            shutil.copyfile(self.db_path,os.getcwd()+'\{}.db'.format(curr_time.date()))
            self.ui.statusbar.showMessage('备份成功！')
        except:
            self.ui.statusbar.showMessage('备份失败！')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=mainWindow()
    window.show()
    sys.exit(app.exec_())
