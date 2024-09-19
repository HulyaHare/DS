import pandas as pd
import numpy as np

# inplace=True diyerek df tamamen değiştirilebilir

s=pd.Series(["ege",np.nan,"ali","eda"])
print(s)

print("\n*******\n")

# eksik veriyi temsil etmek:
print(s.isnull()) # true eksikleri gösterir

print("\n*******\n")

# notnull() metodu isnull metodunun tersini yapar
print(s.notnull())

print("\n*******\n")

# 3. indekse sahip değeri eksik veri yapmak:
s[3]=None
print(s.isnull())

print("\n*******\n")

# EKSİK VERİLERİ ORTADAN KALDIRMAK:
# 1. yol --> eksik verileri ortadan kaldırmak için dropna() kullan:
print(s.dropna())
print()
# 2. yol --> s içinden notnull() olanları yani eksik veri olmayanları seç
print(s[s.notnull()])

print("\n*******\n")

# DATAFRAME YAPISINDA EKSİK VERİLERİ KALDIRMAK:
from numpy import nan as NA
df=pd.DataFrame([[1,2,3],[4,NA,5],[NA,NA,NA]])
print(df)

print("\n*******\n")

# dropna()  ile eksik verileri silmek:
print(df.dropna())

print("\n*******\n")

# tüm değerleri eksik veri olan satırı how="all" yaparak silebilirdsin
print(df.dropna(how="all"))

print("\n*******\n")

# sütunun tüm değerlerini eksik veriye dönüştürmek:
# 2. sütunun tüm değerelerini eksik veri yapalım
df[1]=NA
print(df)
# axis=1 yapıp bütün değerleri eksik veri olan sütunu kaldırmak:
# yani 2. sütunun tüm değerleri eksik veri olduğuna göre 2. sütunu ortadan kaldırıcaz
print(df.dropna(axis=1,how="all"))

print("\n*******\n")

# belirli satıda gözlem değeri olan sütunları almak:
# yani mesela tresh=2 dediğin zaman en az 2 değeri eksik veri olmayan satırları gösterir
print(df.dropna(thresh=2)) # tresh=3 deseydik hiçbir satır görünmezdi ççünkü en az 3 değeri eksik veri olmayan satır yok

print("\n*******\n")

# eksik verilerin yerine sıfır atayalım:
print(df.fillna(0))

print("\n*******\n")

# sözlük ile her sütundaki eksik verilere istediğimiz değerleri atamak
# 1. sütundaki eksik veriler 15 oldu, 2. sütundaki eksik veriler 25 oldu, 3. sütundaki eksik veriler 35 oldu,
print(df.fillna({0:15,1:25,2:35}))

print("\n*******\n")

# objeyi modifiy etmek:
# yani df'yi değiştirmek:
df.fillna(0,inplace=True) # df tamamen değişti

print("\n*******\n")

df=pd.DataFrame([[1,2,3],[4,NA,5],[NA,NA,NA]])
print(df)

print("\n*******\n")

# eksik verilerin yerine bir üst sütunundaki verinin değerini atamak
print(df.fillna(method="ffill"))

print("\n*******\n")

# her bir sütundak, sadece bir eksik verinin değerini değiştircez
# yani her bir sütundaki sadece bir eksik değerin yerine o eksik değerin bir üst sütunundaki değeri yazmak
print(df.fillna(method="ffill",limit=1))

print("\n*******\n")

# eksik verilerin yerine farklı değer atamak
# eksib verilerin yerine ortalama değeri atamak
veri=pd.Series([1,0,NA,5])
print(veri)
print()
print(veri.fillna(veri.mean()))

print("\n*******\n")

print(df)
# df içinde her bir sütunun ortalamasını alıp eksilk verileri bununla doldurmak:
print()
print(df.fillna(df.mean()))