import sys
from PyQt5 import QtWidgets
import pymysql


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
        var = ''
        dbname = ''
        d = ''

    def UI(self):
        self.chkbx1 = QtWidgets.QCheckBox("Create Database from scratch")
        self.chkbx2 = QtWidgets.QCheckBox("Perform QL")
        self.label1 = QtWidgets.QLabel("Enter the name of the database")
        self.field1 = QtWidgets.QLineEdit()
        self.outputLabel = QtWidgets.QLabel()
        self.btn1 = QtWidgets.QPushButton("Add database")
        self.btn2 = QtWidgets.QPushButton("Add tables database")
        self.noteedit = QtWidgets.QPlainTextEdit()
        self.label2 = QtWidgets.QLabel("ON SCREEN SQL COMMAND LINE")
        self.outputLabel2 = QtWidgets.QLabel()
        self.label3 = QtWidgets.QLabel("ON SCREEN SQL COMMAND LINE")
        self.btn3 = QtWidgets.QPushButton("Perform action")
        self.sqledit = QtWidgets.QPlainTextEdit()
        self.label4 = QtWidgets.QLabel()
        self.btn4 = QtWidgets.QPushButton("Select Database")
        self.l5 = QtWidgets.QLabel()
        self.field2 = QtWidgets.QLineEdit()
        self.l1 = QtWidgets.QLabel("Enter the name of the database")
        self.rdiobtn = QtWidgets.QRadioButton("Use the database")

        self.label1.setVisible(False)
        self.field1.setVisible(False)
        self.btn1.setVisible(False)
        self.btn2.setVisible(False)
        self.noteedit.setVisible(False)
        self.label2.setVisible(False)
        self.outputLabel2.setVisible(False)
        self.label3.setVisible(False)
        self.btn3.setVisible(False)
        self.sqledit.setVisible(False)
        self.label4.setVisible(False)
        self.l5.setVisible(False)
        self.btn4.setVisible(False)
        self.field2.setVisible(False)
        self.l1.setVisible(False)
        self.rdiobtn.setVisible(False)

        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(self.label1)
        hlayout.addWidget(self.l1)
        hlayout.addWidget(self.field1)
        hlayout.addWidget(self.field2)
        hlayout.addWidget(self.btn4)

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(self.chkbx1)
        vlayout.addWidget(self.chkbx2)
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.btn1)
        vlayout.addWidget(self.rdiobtn)
        vlayout.addWidget(self.outputLabel)
        vlayout.addWidget(self.label2)
        vlayout.addWidget(self.noteedit)
        vlayout.addWidget(self.btn2)
        vlayout.addWidget(self.outputLabel2)
        vlayout.addWidget(self.label3)
        vlayout.addWidget(self.sqledit)
        vlayout.addWidget(self.btn3)
        vlayout.addWidget(self.l5)
        vlayout.addWidget(self.label4)

        self.chkbx1.toggled.connect(lambda: self.chkbx())
        self.btn1.clicked.connect(lambda: self.btn1press())
        self.btn2.clicked.connect(lambda: self.btn2press())
        self.btn3.clicked.connect(lambda: self.btn3press())
        self.btn4.clicked.connect(lambda: self.btn4press())
        self.chkbx2.toggled.connect(lambda: self.chkbx())
        self.rdiobtn.toggled.connect(lambda: self.usedb())

        self.setLayout(vlayout)
        self.setGeometry(500,500,500,500)
        self.setWindowTitle("ZMS")
        self.show()

    def chkbx(self):
        if self.chkbx1.isChecked() or self.chkbx2.isChecked():
            self.conection = pymysql.connect('localhost','root','root')
            self.cursor = self.conection.cursor()

        if self.chkbx1.isChecked():
            self.label1.setVisible(True)
            self.field1.setVisible(True)
            self.btn1.setVisible(True)
            self.l1.setVisible(True)
        else:
            self.label1.setVisible(False)
            self.field1.setVisible(False)
            self.btn1.setVisible(False)
            self.btn2.setVisible(False)
            self.noteedit.setVisible(False)
            self.label2.setVisible(False)
            self.l1.setVisible(False)

        if self.chkbx2.isChecked():
            self.label3.setVisible(True)
            self.btn3.setVisible(True)
            self.btn4.setVisible(True)
            self.sqledit.setVisible(True)
            self.label1.setVisible(True)
            self.l5.setVisible(True)
            self.label4.setVisible(True)
            self.field2.setVisible(True)
        else:
            self.label3.setVisible(False)
            self.btn3.setVisible(False)
            self.btn4.setVisible(False)
            self.sqledit.setVisible(False)
            self.label1.setVisible(False)
            self.l5.setVisible(False)
            self.label4.setVisible(False)
            self.field2.setVisible(False)


    def btn1press(self):
        self.dbname = self.field1.text()
        try:
            self.btn3.setVisible(True)
            self.sqledit.setVisible(True)
            self.label2.setVisible(True)
            self.l5.setVisible(True)
            self.label4.setVisible(True)
            self.rdiobtn.setVisible(True)
            self.list = self.cursor.execute('show databases;')
            self.d = 'create database if not exists '+self.dbname+';'
            self.cursor.execute(self.d)
            self.outputLabel.setText("The Database name is \n" + self.dbname)
        except Exception as e:
            print(type(e))

    # def btn2press(self):
    #     if self.sender():
    #         self.var = self.noteedit.toPlainText()
    #         self.outputLabel2.setText("The Tables are\n"+self.var)
    #         self.label3.setVisible(True)
    #         self.btn3.setVisible(True)
    #         self.sqledit.setVisible(True)
    def usedb(self):
        self.cursor.execute('use '+self.dbname)

    def btn4press(self):
        try:
            self.dbname = self.field2.text()
            self.name = "use "+self.dbname
            self.cursor.execute(self.name)
            self.l5.setText("Database "+self.dbname+" created")
        except Exception as e:
            print(e)
    def btn3press(self):
        try:
            if self.sender():
                self.d = self.sqledit.toPlainText()
                self.cursor.execute(self.d)
                self.l5.setText("Performing action")
                self.data = self.cursor.fetchall()
                self.label4.setText(str(list(self.data)))
                print(type(str(list(self.data))))
                self.sqledit.clear()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    i = QtWidgets.QApplication(sys.argv)
    app = Window()
    sys.exit(i.exec_())
