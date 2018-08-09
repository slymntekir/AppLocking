# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


from classes import Uygulamalar
from PyQt4 import QtCore, QtGui
import time

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
        Form.setEnabled(True)
        Form.resize(261, 521)
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 256, 481))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.clicked.connect(self.islem)
        self.pushButton.setGeometry(QtCore.QRect(0, 490, 251, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Sec", None))

    def islem(self):
        list = []
        for eleman in self.listWidget.selectedItems():
            list.append(eleman.text())
        uyg = Uygulamalar()
        uyg.ekle(list)
        sys.exit()

if __name__ == "__main__":
    import sys,subprocess
    komut = subprocess.Popen("cd /usr/share/applications && ls",shell=True,stdout=subprocess.PIPE)
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    for uyg in komut.stdout.readlines():
        ui.listWidget.addItem(uyg.decode('utf-8').split(".")[0])
    Form.show()
    sys.exit(app.exec_())