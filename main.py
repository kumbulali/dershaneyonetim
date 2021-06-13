from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QTableWidgetItem

dbHostAdi = "localhost"
dbKullaniciAdi = "root"
dbSifre = ""
dbAdi = "dershanedb"

class Ui_dershaneKayit(object):

    def setupUi(self, dershaneKayit):
        dershaneKayit.setObjectName("dershaneKayit")
        dershaneKayit.resize(1100, 451)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dershaneKayit.sizePolicy().hasHeightForWidth())
        dershaneKayit.setSizePolicy(sizePolicy)
        self.tablo = QtWidgets.QTableWidget(dershaneKayit)
        self.tablo.setGeometry(QtCore.QRect(420, 10, 670, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablo.sizePolicy().hasHeightForWidth())
        self.tablo.setSizePolicy(sizePolicy)
        self.tablo.setRowCount(5)
        self.tablo.setColumnCount(5)
        self.tablo.setObjectName("tablo")
        columns=["Öğrenci No", "Ad", "Soyad", "Sınıf", "Veli İlt. No"]
        self.tablo.setHorizontalHeaderLabels(columns)
        self.gridLayoutWidget = QtWidgets.QWidget(dershaneKayit)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ogrAd = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ogrAd.setObjectName("ogrAd")
        self.ogrSoyad = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ogrSoyad.setObjectName("ogrSoyad")

        self.ogrSinif = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.ogrSinif.setObjectName("ogrSinif")
        self.ogrSinif.addItem("")
        self.ogrSinif.addItem("")
        self.ogrSinif.addItem("")
        self.ogrSinif.addItem("")
        self.ogrSinif.addItem("")
        self.ogrSinif.addItem("")
        self.ogrSinif.addItem("")
        self.ogrSinif.addItem("")
        self.ogrSinif.addItem("")
        self.ogrSinif.addItem("")
        self.ogrSinif.addItem("")
        self.ogrSinif.addItem("")
        self.gridLayout.addWidget(self.ogrAd, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.ogr_VeliTlf = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ogr_VeliTlf.setObjectName("ogr_VeliTlf")
        self.gridLayout.addWidget(self.ogr_VeliTlf, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.ogrSinif, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.ogrSoyad, 2, 1, 1, 1)
        self.kaydet = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.kaydet.setObjectName("kaydet")
        self.kaydet.clicked.connect(self.kaydetme)
        self.gridLayout.addWidget(self.kaydet, 5, 1, 1, 1)
        self.temizle = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.temizle.setObjectName("temizle")
        self.temizle.clicked.connect(self.temizleme)
        self.gridLayout.addWidget(self.temizle, 5, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(dershaneKayit)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 230, 391, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ogr_No = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ogr_No.setObjectName("ogr_No")
        self.gridLayout_2.addWidget(self.ogr_No, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.kayitSil = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.kayitSil.setObjectName("kayitSil")
        self.kayitSil.clicked.connect(self.silmek)
        self.gridLayout_2.addWidget(self.kayitSil, 1, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(dershaneKayit)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 290, 391, 101))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ogrAraAd = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.ogrAraAd.setObjectName("ogrAraAd")
        self.gridLayout_3.addWidget(self.ogrAraAd, 0, 1, 1, 1)
        self.ogrAraNo = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.ogrAraNo.setObjectName("ogrAraNo")
        self.gridLayout_3.addWidget(self.ogrAraNo, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.arama = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.arama.setObjectName("arama")
        self.arama.clicked.connect(self.aramak)
        self.gridLayout_3.addWidget(self.arama, 2, 1, 1, 1)
        self.yenile = QtWidgets.QPushButton(dershaneKayit)
        self.yenile.setGeometry(QtCore.QRect(310, 400, 91, 41))
        self.yenile.setObjectName("yenile")
        self.yenile.clicked.connect(self.yenilemek)

        self.retranslateUi(dershaneKayit)
        QtCore.QMetaObject.connectSlotsByName(dershaneKayit)
        self.yenilemek()

    def retranslateUi(self, dershaneKayit):
        _translate = QtCore.QCoreApplication.translate
        dershaneKayit.setWindowTitle(_translate("dershaneKayit", "Python Dershanesi Öğrenci Kayıt Sistemi"))
        self.label_3.setText(_translate("dershaneKayit", "Öğrenci Sınıfı"))
        self.label.setText(_translate("dershaneKayit", "Öğrenci Adı"))
        self.label_4.setText(_translate("dershaneKayit", "Öğrenci Veli İletişim Numarası"))
        self.label_2.setText(_translate("dershaneKayit", "Öğrenci Soyadı"))
        self.ogrSinif.setItemText(0, _translate("dershaneKayit", "1. Sınıf"))
        self.ogrSinif.setItemText(1, _translate("dershaneKayit", "2. Sınıf"))
        self.ogrSinif.setItemText(2, _translate("dershaneKayit", "3. Sınıf"))
        self.ogrSinif.setItemText(3, _translate("dershaneKayit", "4. Sınıf"))
        self.ogrSinif.setItemText(4, _translate("dershaneKayit", "5. Sınıf"))
        self.ogrSinif.setItemText(5, _translate("dershaneKayit", "6. Sınıf"))
        self.ogrSinif.setItemText(6, _translate("dershaneKayit", "7. Sınıf"))
        self.ogrSinif.setItemText(7, _translate("dershaneKayit", "8. Sınıf"))
        self.ogrSinif.setItemText(8, _translate("dershaneKayit", "9. Sınıf"))
        self.ogrSinif.setItemText(9, _translate("dershaneKayit", "10. Sınıf"))
        self.ogrSinif.setItemText(10, _translate("dershaneKayit", "11. Sınıf"))
        self.ogrSinif.setItemText(11, _translate("dershaneKayit", "12. Sınıf"))
        self.kaydet.setText(_translate("dershaneKayit", "Öğrenci ekle"))
        self.temizle.setText(_translate("dershaneKayit", "Temizle"))
        self.label_5.setText(_translate("dershaneKayit", "Öğrenci Numarası"))
        self.kayitSil.setText(_translate("dershaneKayit", "Kaydı Sil"))
        self.yenile.setText(_translate("dershaneKayit", "Yenile"))
        self.label_6.setText(_translate("dershaneKayit", "Öğrenci Adı"))
        self.label_7.setText(_translate("dershaneKayit", "Öğrenci Numarası"))
        self.arama.setText(_translate("dershaneKayit", "Ara"))



    def kaydetme(self):
        mydb = mysql.connector.connect(
            host=dbHostAdi,
            user=dbKullaniciAdi,
            password=dbSifre,
            database=dbAdi
        )
        kaydetAd = self.ogrAd.text()
        kaydetSoyad = self.ogrSoyad.text()
        kaydetSinif = self.ogrSinif.currentText()
        kaydetVeliTlf = self.ogr_VeliTlf.text()
        mycursor = mydb.cursor()
        val = (kaydetAd, kaydetSoyad, kaydetSinif, kaydetVeliTlf)
        sql = "INSERT INTO ogrenciler (ogr_ad,ogr_soyad,ogr_sinif,ogr_velitlf) values (%s,%s,%s,%s)"
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()

    def silmek(self):
        mydb = mysql.connector.connect(
            host=dbHostAdi,
            user=dbKullaniciAdi,
            password=dbSifre,
            database=dbAdi
        )
        cursor = mydb.cursor()
        silNumara = int(self.ogr_No.text())
        sql= "DELETE FROM ogrenciler WHERE ogr_no = {}".format(silNumara)
        cursor.execute(sql)
        mydb.commit()

    def temizleme(self):
        self.ogrAd.setText("")
        self.ogrSoyad.setText("")
        self.ogrSinif.setCurrentIndex(0)
        self.ogr_VeliTlf.setText("")

    def yenilemek(self):

        mydb = mysql.connector.connect(
            host=dbHostAdi,
            user=dbKullaniciAdi,
            password=dbSifre,
            database=dbAdi
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM ogrenciler")
        result = mycursor.fetchall()

        self.tablo.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tablo.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tablo.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        mycursor.close()
    def aramak(self):

        mydb = mysql.connector.connect(
            host=dbHostAdi,
            user=dbKullaniciAdi,
            password=dbSifre,
            database=dbAdi
        )
        if self.ogrAraAd.text() != "":
            mycursor = mydb.cursor()
            aramakAd = self.ogrAraAd.text()
            sql = """SELECT * FROM ogrenciler WHERE ogr_ad = '{}'""".format(aramakAd)
            mycursor.execute(sql)
            result = mycursor.fetchall()

            self.tablo.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tablo.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tablo.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            mycursor.close()
        elif self.ogrAraNo.text() != "":
            mycursor = mydb.cursor()
            aramakNo = int(self.ogrAraNo.text())
            sql = """SELECT * FROM ogrenciler WHERE ogr_no = {}""".format(aramakNo)
            mycursor.execute(sql)
            result = mycursor.fetchall()

            self.tablo.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tablo.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tablo.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            mycursor.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dershaneKayit = QtWidgets.QWidget()
    ui = Ui_dershaneKayit()
    ui.setupUi(dershaneKayit)
    dershaneKayit.show()
    sys.exit(app.exec_())

