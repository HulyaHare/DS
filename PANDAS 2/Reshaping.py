# verilerin formatını çevireceğiz
import pandas as pd
import numpy as np

veri=pd.DataFrame(np.arange(16).reshape(4,4),
                  index=[list("aabb"),[1,2]*2],
                  columns=[["say","say","soz","soz"],
                           ["mat","ing"]*2])
print(veri)

print("\n************\n")

#TABLO ŞEKLİNDEKİ VERİ SETİ
# veri setinin satır ve sütunlarını isimlendirelim
veri.index.names=["sinif","sinav"]
veri.columns.names=["alan","ders"]
print(veri)

print("\n************\n")

# veriyi uzun formata çevirmek
# UZUN FORMATTAKİ VERİ SETİ
uzun=veri.stack()
print(uzun)
print()
# veriyi tablo şekline geri çevirmek:
# TABLO FORMATINDAKİ VERİ SETİ
print(uzun.unstack())

print("\n************\n")

# level numarasını ya da seviye ismini girerek farklı seviyelerde stack ya da unstack yapılabilir
print("mesela veri.stack() yaptığında en içtekine göre yani ders'e göre stacklanmıştı")

print("\n************\n")

# alana göre stack yapmak:
print(veri.stack(0))
print()
# isim girerek stacklama yapmak yine alana göre stacklama yapmak:
print(veri.stack("alan"))

print("\n************\n")

# seviyelerde bütün değerler bulunmazsa unstacktan sonra eksik değerler oluşabilir
s1=pd.Series(np.arange(4),index=list("abcd"))
s2=pd.Series(np.arange(6,9),index=list("cde"))
print(s1)
print(s2)
print()
# iki veri setini concsat ile birleştirelim
veri2=pd.concat([s1,s2],keys=["bir","iki"])
print(veri2)
print()
# şimdi bu veri setini unstacklayalım
print(veri2.unstack())

# VERİ STACKLANIRKEN EKSİK VERİLER KALDIRILIR AMA UNSTACKLANIRKEN EKSŞK VERİLER KALIR

print("\n************\n")

# stacklama yaparken eksik verileri de görmek
print(veri2.unstack().stack(dropna=False))

print("\n************\n")

# uzun formattaki veri:
stok=pd.DataFrame({"meyve":["elma","erik","uzum"]*2,
                   "renk":["mor","sari"]*3,
                    "adet":[3,4,5,6,1,2]})
print(stok)

print("\n************\n")

# veri setini tablo haline çevirelim
print(stok.pivot("meyve","renk","adet"))

print("\n************\n")

# veri setine bir sütun daha ekleyelim
stok["deger"]=np.random.randn(len(stok))
print(stok)

print("\n************\n")

# pivot metodunda ilk iki değeri yazarsak hiyerarşik yani aşamalı sütunlar elde ederiz
p=stok.pivot("meyve","renk")
print(p)

print("\n************\n")

# p veri setinin değer değişkenine göre alt kümesi:
print(p["deger"])

print("\n************\n")

# pivot metodunun ters operatörü melttir yani geniş formatı uzun formata çevirir
# GENİŞ FORMATTA VERİ SETİ OLIŞTIRALIM
veri=pd.DataFrame({"ders":["mat","fiz","edb"],
                   "eda":[50,60,70],
                   "efe":[80,70,90],
                   "ali":[60,70,85]})
print(veri)

print("\n************\n")

# veri setini ders sütununa göre düzenleyelim: (tablo halindeki veri setini uzun veri seti yapmak:
grup=pd.melt(veri,["ders"])
print(grup)

print("\n************\n")

# veri setini eski hale getirelim:
data=grup.pivot("ders","variable","value")
print(data)

print("\n************\n")

# ders sütununu index olmaktan çıkartmak yani sütun haline getirmek
print(data.reset_index())