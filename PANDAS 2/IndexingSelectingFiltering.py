# [] ile indexleme yapılır
import datetime

import pandas as pd
import numpy as np

obje=pd.Series(np.arange(5),index=["a","b","c","d","e"])
print(obje)

print("\n*******\n")

# indexini girip verivi bulmak:
# burada indexleri harf c,ns,nden yazdığımız için c diyebildik
print(obje["c"])
# print(obje[2]) desek de olurdu çünkğ c'nin indexi 2

print("\n*******\n")

# 0'dan üçe kadar göstermek ama hem solu hem sağı gösyere
print(obje[0:3])

print("\n*******\n")

# belirli satırları yazdırmak:
print(obje[["a","c"]]) # eğer print(obje["a"]) deseydik sadece a'nın olduğunu göstererirdi

print("\n*******\n")

# aynı şeyi index numarası görerek de yapabiliriz:
print(obje[[0,2]])

print("\n*******\n")

# 2'den küçük değerleri eklrana yazdırmak
print(obje[obje<2])


print("\n*******\n")

# a'dan c'ye kadar olan değerleri dilimlemek (hem a hem c dahil)
print(obje["a":"c"])

print("\n*******\n")

# b'den c'ye kadar olan değerlere 5 değerini atamak (yami b ve c dahil)
obje["b":"c"]=5
print(obje)

print("\n*******\n*******\n*******\n")

# DATAFRAME İÇİN İNDEXLEME
# arange(16) diyerek 0'dan 15'e kadr olan sayıları içeren dizi oluşturur
# reshape(4,4) diyerek bu d,z,y, 4x4 boyutunda matrise dönüştürür
veri=pd.DataFrame(np.arange(16).reshape(4,4),index=["Bursa","Ankara","Rize","Istanbul"]
                                            ,columns=["bir","iki","uc","dort"])
print(veri)

print("\n*******\n")

# iki ismindeki sütunu ekrana yazdırmak
print(veri["iki"])
print(veri)

print("\n*******\n")

# birden fazla sütun değerlerini yazdırmak:
print(veri[["bir","iki"]])

print("\n*******\n")

# 3 indexinde kadar olan değerler (sütun olarark 3'e kadar olanlar)
print(veri[:3])

print("\n*******\n")

# 4. sütunda 5'den büyük değeleri göstermek
print(veri[veri["dort"]>5])

print("\n*******\n")

# beşden küçük değerlere 0 değerini ata
veri[veri<5]=0
print(veri)

print("\n*******\n")

# dataframedeki indexler için loc ya da iloc kullanılabilir
# numara için iloc, etiket ismi için loc kullan
# [satır,sütun]

# 1. indexe sahip satırın sütunlarını görmek:
# bu birinci yoldur:
print(veri[1:2])
print()
# bu ikimci yoldur:
print(veri.iloc[1])

print("\n*******\n")

# 1. indexe sahip satırın  1,2 ve 3. sütunlarını seçmek
print(veri.iloc[1,1:4])
print()
# bu ikinci yoldur:
print(veri.iloc[1,[1,2,3]])

print("\n*******\n")

# birden çok satırın belirli sütunlarını seçmek:
print(veri.iloc[[1,3],[1,2,3]])

print("\n*******\n")

# bir satırın birden çok sütununu seçmek
# bir ve iki etiketine sahip sütunların değerlerini ekrana yazdırmak
print(veri.loc["Rize",["bir","iki"]])

print("\n*******\n")

# Rize'ye kadar olan satırların 4. sütununu seçmek
print(veri.loc[:"Rize","dort"])

print("\n*******\n")

# değişken alıp değişkene değerler atayalım
veri=pd.Series(np.arange(5),index=["a","b","c","d","e"])
print(veri)

print("\n*******\n")

print(veri[-1])