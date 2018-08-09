# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import subprocess
from classes import *
import classes

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(549, 327)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(0, 110, 241, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QtCore.QRect(250, 10, 291, 261))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 290, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.yetkilendir)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 290, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.yetki_kaldir)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Yetkilendir", None))
        self.pushButton_2.setText(_translate("Form", "Yetki kaldır", None))

    def yetkilendir(self):
        list_uyg = []
        kullanici = str(self.comboBox.currentText())
        for uyg in self.listWidget.selectedItems():
            list_uyg.append(uyg.text())
        yon = Yonetim()
        yon.ekle(kullanici,list_uyg)
        sys.exit()

    def yetki_kaldir(self):
        list_uyg = []
        kullanici = str(self.comboBox.currentText())
        for uyg in self.listWidget.selectedItems():
            list_uyg.append(uyg.text())
        yon = Yonetim()
        yon.sil(kullanici,list_uyg)
        sys.exit()

if __name__ == "__main__":
    import sys
    komut = subprocess.Popen("cd /usr/share/applications && ls",shell=True,stdout=subprocess.PIPE)
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    for i in range(classes.kullanici_id.__len__()):
        if i==0:
            continue
        ui.comboBox.addItem(classes.kullanicilar[i])
    for i in komut.stdout.readlines():
        ui.listWidget.addItem(i.decode('utf-8').split(".")[0])
    Form.show()
    sys.exit(app.exec_())