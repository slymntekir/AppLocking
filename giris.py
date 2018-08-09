# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import subprocess,time,sys
from PyQt4 import QtCore, QtGui

import classes
from classes import Uygulamalar
from classes import Kullanicilar

import threading

kullanicilar = Kullanicilar()

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
        Form.resize(400, 145)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 10, 181, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 50, 181, 27))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 100, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.ac)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def ac(self):
        #self.i=True
        for i in range(kullanicilar.id.__len__()):
            kullanici_adi = kullanicilar.kul[i]
            sifre = kullanicilar.sifre[i]
            if(self.lineEdit.text().__eq__(kullanici_adi) and self.lineEdit_2.text().__eq__(sifre)):
                if self.lineEdit.text().__eq__("root"):
                    subprocess.Popen(ana_uyg,shell=True,stdout=subprocess.PIPE)
                    '''
                    while True:
                        self.kapali_mi()
                    '''
                elif not self.lineEdit.text().__eq__("root"):
                    var_mi = classes.var_mi(kullanici_adi,ana_uyg)
                    if var_mi:
                        subprocess.Popen(ana_uyg,shell=True,stdout=subprocess.PIPE)
                    elif not var_mi:
                        print(kullanici_adi+" malesef yetkiniz yok")
        sys.exit()

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Kullanıcı Adı :", None))
        self.label_2.setText(_translate("Form", "Sifre :", None))
        self.pushButton.setText(_translate("Form", "Giriş Yap", None))

'''
    def kapali_mi(self):
        sonuc = str(subprocess.Popen("ps x |grep -v grep |grep -c "+ana_uyg,shell=True,stdout=subprocess.PIPE).stdout.read())
        if sonuc.__contains__("0") and self.i==True:
            self.i=False
            islem = subprocess.Popen("python3 yonetici.py",shell=True)
            islem.communicate()
        time.sleep(2)
'''

uyg = Uygulamalar()
list1 = uyg.dondur()

class Bekle(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in list1:
            uyga = ''.join(i)
            sonuc = str(subprocess.Popen("ps x |grep -v grep |grep -c "+uyga,shell=True,stdout=subprocess.PIPE).stdout.read())
            if sonuc.__contains__("1"):
                subprocess.Popen("pkill -10 "+uyga,shell=True,stdout=subprocess.PIPE).stdout.read()
                global ana_uyg
                ana_uyg=uyga
                import sys
                app = QtGui.QApplication(sys.argv)
                Form = QtGui.QWidget()
                ui = Ui_Form()
                ui.setupUi(Form)
                Form.show()
                sys.exit(app.exec_())

while True:
    Bekle().start()
    time.sleep(2)