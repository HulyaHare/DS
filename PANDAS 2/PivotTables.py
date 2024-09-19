# veri setini araçlar kullanarak dikdörtgen şeklindeki tabloda birleştirir
# pivot tablolar groupby ile yaomanın çok yönlüsüdür
# pivot tablo ve groupby ile oluşmuş tablo b,rbirinden farklıdır
import pandas as pd
import numpy as np

nt=pd.DataFrame({"sinif":list("ABC")*4,
                 "ders":["mat","fiz"]*6,
                 "cinsiyet":list("EKEE")*3,
                 "kardes":[1,2,3]*4,
                 "puan":np.arange(40,100,5)})
print(nt)

print("\n*******\n")

# ders kategorisine göre gruplama yapalım
# derslere göre puan ortalamalarını bulalım
print(nt.groupby("ders")["puan"].mean())

print("\n*******\n")

# şimdi iki kategorilik sütuna göre ortalamaları bulalım (hiyerarşikal indexleme ile bulalım)
print(nt.groupby(["ders","sinif"])["puan"].aggregate("mean"))

print("\n*******\n")

# tablo haline çevirip yazalım
print(nt.groupby(["ders","sinif"])["puan"].aggregate("mean").unstack())

print("\n*******\n")

"""
PİVOT TABLE İLE ÇOK BOYUTLU GRUPLAMA İŞLEMLERİ YAPILIR VE İLERİ DÜZEY İŞLEMLER YAPILIR
ŞİMDİ AYNI ŞEYLERİ PİVOT TABLE İLE YAPALIM
"""

print("\n*******\n")

# az önce groupby şle oluşmuş tabloyu pivot_table ile oluşturalım
print(nt.pivot_table("puan",
                     index="ders",
                     columns="sinif"))

print("\n*******\n")

# şimdi hiyerarşik indexlerle pivot table oluşturalım
print(nt.pivot_table(["kardes","puan"],
                     index=["sinif","ders"],
                     columns="cinsiyet"))

print("\n*******\n")

# tabloya satır ve sütunların ortalamalarını veren satır ve sütun eklemek
# bu satıra ve sütuna All denir
print(nt.pivot_table(["kardes","puan"],
                     index=["sinif","ders"],
                     columns="cinsiyet",
                     margins=True))

print("\n*******\n")

# eksik değerlerin yerine değer atamak
print(nt.pivot_table(["kardes","puan"],
                     index=["sinif","ders"],
                     columns="cinsiyet",
                     margins=True,
                     fill_value=True))

print("\n*******\n")

# pivot tablolaro çok seviyeli hale getirebilirz:
# ömce cut metodu ile kardeş değişkenini aralıklara bölelim yani her bir dğeğerinin hangi aralıkta olduğunu belirttiğimiz aralıklara göre söyleyelim
kardes=pd.cut(nt["kardes"],[0,2,3])
print(kardes)
# şimdi bu kardes değişkenini kullanarak veri setini çok seviyeli hale getirelim
print(nt.pivot_table("puan",["ders",kardes],"sinif",fill_value=0))

print("\n*******\n")

# seviye sayısını arttırabiliriz.
# normalde otomatik olarak ortalama bulunur ama bunu elimizle değiştirebiliriz
# mesela ortalama yerine toplam fonksiyonunu kullanalım
print(nt.pivot_table("puan",index="ders",columns="sinif",aggfunc="sum"))

print("\n*******\n")

# puan değişkenini kardırırsak hem kardeş hem puan verilier:
print(nt.pivot_table(index="ders",columns="sinif",aggfunc="sum"))

print("\n*******\n")

# istersek sözlük yapısını kullanarak herbir sütun için farklı fonksiyon kullanabiliriz
print(nt.pivot_table(index="ders",columns="sinif",
                     aggfunc={"kardes":"max","puan":"sum"}))

print("\n*******\n")

"""
ŞİMDİ CROSSTAB TABLOSUNA BAKALIM 
BU TABLO GRUP FREKANSLARINI HESAPLAYAN BİR TABLODUR
İKİ ARGUMAN ALIRLAR, İLKİ SIKLIĞĞI BULUNACAK ŞEYİ VERİR İKİNCİSİ DE GRUPLANACAK ÖGEYİ VERİR
"""

# herbir sınıftaki kardeş sayılarının sıklığını bulalım
print(pd.crosstab(nt.kardes,nt.sinif))

print("\n*******\n")

# derslere göre kardeş sayılarını ve herbir sınıftaki kardeş sayılarının sıklığını bulalık
print(pd.crosstab([nt.kardes,nt.ders],nt.sinif))

print("\n*******\n")

print("\n*******\n")

dogum=pd.read_csv("births1.txt")
print(dogum.head())

print("\n*******\n")

# her on yılda bir doğan çocukların sayısını bulalım
dogum["onyıl"]=10*(dogum["year"]//10)
print(dogum)
print()
# her on yılda doğan çocukların kız erkek sayısını bulalım
print(dogum.pivot_table("births",
                        index="onyıl",
                        columns="gender",
                        aggfunc="sum"))

print("\n*******\n")

# şimdi kız ve erkek doğumlarının trendini görmek için grafiğini çizzelim
import matplotlib.pyplot as plt
import seaborn as sns
# seaborn kullanmak için şunu yap:
sns.set()
# şimdi doğumların yıllık değişimi görmek için pivot table kullanalım
# plot() ile grafiği çizdirmek istediğiöizi belirtelim
dogum.pivot_table("births",
                        index="year",
                        columns="gender",
                        aggfunc="sum").plot()
# y eksenini isimlendirelim:
plt.ylabel("Yıllık toplam doğum")
# grafiği gösterelim:
plt.show()
