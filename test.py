#sadece test sınıfı hangi kullanıcılar yetkili onu yazıyor

import sqlite3 as sql

def yaz():
    with sql.connect("veri.db") as vt:
        im=vt.cursor()
        #im.execute("""DELETE FROM yetki""")
        #vt.commit()
        im.execute("""SELECT * FROM yetki""")
        veriler = im.fetchall()
        for veri in veriler:
            print(veri,sep="\n")

def goster():
    with sql.connect("data1.db") as vt:
        im=vt.cursor()
        im.execute("""SELECT * FROM uygulama""")
        uydulamalar = im.fetchall()
        for uyg in uydulamalar:
            print(uyg,sep="\n")

goster()
yaz()