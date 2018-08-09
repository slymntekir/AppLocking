import sqlite3 as sql
import time

kullanici_id = [("0"),   ("1"),       ("2"),    ("3"),    ("4"),    ("5"),     ("6")]
kullanicilar = [("root"),("suleyman"),("ender"),("hasan"),("ali"),  ("mehmet"),("ahmet")]
sifreler     = [("0000"),("1111"),    ("2222"), ("3333"), ("4444"), ("5555"),  ("6666")]
yetkiler     = [("Evet"),("Hayir"),   ("Hayir"),("Hayir"),("Hayir"),("Hayir"), ("Hayir")]

class Kullanicilar:
    def __init__(self,id=kullanici_id,kul=kullanicilar,sifre=sifreler,yetki=yetkiler):
        self.id=id
        self.kul = kul
        self.sifre = sifre
        self.yetki = yetki
    def yaz(self):
        for i in range(kullanici_id.__len__()):
            print(self.id[i],self.kul[i],self.sifre[i],self.yetki[i],sep=" ",end="\n")


class Uygulamalar:
    def __init__(self):
        pass
    def ekle(self,list):
        for i in list:
            print(''.join(i))
        with sql.connect("data1.db") as vt:
            im=vt.cursor()
            im.execute("""DROP TABLE IF EXISTS uygulama""")
            im.execute("""CREATE TABLE uygulama(uygulamaadi)""")
            for i in list:
                im.execute("""INSERT INTO uygulama(uygulamaadi) values(?)""",[(i)])
            vt.commit()
    def dondur(self):
        with sql.connect("data1.db") as vt:
            im=vt.cursor()
            im.execute("""SELECT * FROM uygulama""")
            return im.fetchall()

def var_mi(k,u):
    degisken = False
    vt1 = sql.connect("veri.db")
    im1 = vt1.cursor()
    im1.execute("""SELECT * FROM yetki""")
    bilgiler = im1.fetchall()
    for bilgi in bilgiler:
        k1,u1 = bilgi
        if str(k).__eq__(k1) and str(u).__eq__(u1):
            degisken=True
            break
    return degisken


class Yonetim:
    def __init__(self):
        pass
    def ekle(self,kul,uyg):
        vt = sql.connect("veri.db")
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS yetki("kullaniciadi","uygulamaadi")""")
        for uy in uyg:
            cikti=var_mi(kul,uy)
            if not cikti:
                im.execute("""INSERT INTO yetki VALUES(?,?)""",[(kul),(uy)])
                vt.commit()
                print("'"+kul+"' kullanicisina '"+uy+"' programının yetkisi verildi.")
            elif cikti:
                print("'"+kul+" kullanicisinin "+uy+" programına yetkisi zaten verilmis.")
    def sil(self,kul,uyg):
        vt = sql.connect("veri.db")
        im = vt.cursor()
        for uy in uyg:
            cikti=var_mi(kul,uy)
            if cikti:
                im.execute("""DELETE FROM yetki WHERE kullaniciadi=? and uygulamaadi=?""",[(kul),(uy)])
                vt.commit()
                print("'"+kul+"' kullanicisinin '"+uy+"' programina yetkisi kaldirildi.")
            elif not cikti:
                print("'"+kul+"' kullanicisinin '"+uy+"' programina yetkisi zaten yok.")
    def yaz(self):
        vt = sql.connect("veri.db")
        im = vt.cursor()
        im.execute("""SELECT * FROM yetki""")
        for uu,kk in im.fetchall():
            print(uu+"-"+kk)

'''
    calistir = subprocess.Popen("python3 giris.py",shell=True)
    calistir.communicate()"

id = []
prog = []
yetki = []

class Yetkiler:
    i=0
    def __init__(self,yetki_id=id,prog_adi=prog,yetki=yetki):
        self.yetki_id = yetki_id
        self.prog_adi = prog_adi
        self.yetki = yetki
    def ekle(self,program,yetkii):
        id.append(str(self.i))
        prog.append(program)
        yetki.append(yetkii)
        self.i +=1
    def yaz(self):
        for index in range(id.__len__()):
            print(self.yetki_id[index],self.prog_adi[index],self.yetki[index],sep=" ",end="\n")
'''