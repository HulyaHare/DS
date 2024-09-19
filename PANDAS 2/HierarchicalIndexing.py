# bunlar bir eksen üzerinde birden fazla indexe sahip olabilirler
# çoklu indexlerdir
import pandas as pd
import numpy as np

veri=pd.Series(np.random.randn(8),
               index=[["a","a","a","b","b","b","c","c"],
                      [1,2,3,1,2,3,1,2]])
print(veri)

print("\n*******\n")

# verinin indexlerinin çoklu seviyelerini görmek
print(veri.index)

print("\n*******\n")

# istediğimiz indexi yazarak verinin alt kümelerini elde edebiliriz
# a indexe sahip verileri ekrana yazdıralım
print(veri["a"])

print("\n*******\n")

# veriyi dilimleyelim
# b indexinden c indexine kadar dilimleyelim:
print(veri["b":"c"])

print("\n*******\n")

# birden fazla indexi alalım
# a ve c indexine sahip verileri ekrana yazdıralım:
print(veri.loc[["a","c"]])

print("\n*******\n")

# içteki indexten değer seçelim:
# içteki indexin birinci değerini ekrana yazdıralım
print(veri.loc[:,1]) # tüm indexleri seçtik sonra da onların içinden 1.leri seçtik

print("\n*******\n")

# veriyi tablo şeklinde göstermek:
print(veri.unstack())

print("\n*******\n")

# tablo haline gelmiş veri setini tekrar eski haline getirmek:
print(veri.unstack().stack())

print("\n*******\n")
print("\n*******\n")

# DataFrame yapısındaki vweriler de hiyerrterşik olabilir:
vs=pd.DataFrame(np.arange(12).reshape(4,3),
                index=[["a","a","b","b"],[1,2,1,2]],
                columns=[["say","say","soz"],["mat","fiz","edb"]])
print(vs)

print("\n*******\n")

# hiyerarşik sevileri isimlendirmek:
vs.index.names=["sinif","sinav"]
vs.columns.names=["alan","ders"]
print(vs)

print("\n*******\n")

# verinin alt gruplarını seçelim:
# say indexine sahip verileri ekrana yazdıralom
print(vs["say"])

print("\n*******\n")

# indexlerin seviyelerini değiştirelim
# iki seviye ya da iki isim argumanı alır ve obje döndürür
# mesela sınıf ve sınav indexlerinin yerini değiştirelim
print(vs.swaplevel("sinif","sinav"))

print("\n*******\n")

# seviyelere göre indexleri sıralayalım:
# seviye 1'e göre sıralauyalım
print(vs.sort_index(level=1)) # içini boş bıraksaydık 0. indexe göre sıralama yapardo

print("\n*******\n")

# isediğimiz seviyeye göre özet istatistikleri elde edebiliriz
# verideki sayı seviyesine göre toplam değerleri bulmak
print(vs.groupby(level=0).sum())

print()

# verideki alan seviyesine göre toplam değerleri bulmak
print(vs.groupby(level=1).sum())

print("\n*******\n")

veri=pd.DataFrame({"x":range(8),
                   "y":range(8,0,-1),
                   "a":["bir","bir","bir","bir","iki","iki","iki","iki"],
                   "b":[0,1,2,3,0,1,2,3]})
print(veri)

print("\n*******\n")

# veri setinin a ve b sütunlarını bir değişken şeklinde yazalım
veri2=veri.set_index(["a","b"]) # a ve b sütunlaru satur indexi oldu
print(veri2)

print("\n*******\n")

# setindex metodunda satıra taşınan indexler sütundan kaldırılır
# eğer istersek drop=False opsiyonu ile index olarak aldığımız sütunlar aynı yerinde kalır
veri3=veri.set_index(["a","b"],drop=False)
print(veri3)

print("\n*******\n")

# reset_index komutu veri stini eski haline getirir
print(veri2.reset_index())

print("\n*******\n")

