# sayısal hesaplamalar için numpy kullanılır
# çok boyutlu dizi işkemleri döngü kullanılmadan da yapışlabilir

import numpy as np

# NUMPY İLE DİZİ İŞKEMLERİ

data=np.random.randn(3,2)
print(data)

print("\n*******\n")

# datadaki her bir elemanı 10 ile çarpalım
print(data*10)

print("\n*******\n")

# datadaki herbir elemanı kendiyle toplayalım
print(data+data)

print("\n*******\n")

# data ismşndekş dizinin yapısına bakalım
print(data.shape)

print("\n*******\n")

# dizinin elemanlarının veri tiplerini görelim
print(data.dtype)

print("\n*******\n")

# array komutuyla dizi oluşturalım
liste=[3,6.5,0,1,9]
# listeyi diziye çevirelim
dizi=np.array(liste)
print(dizi)

print("\n*******\n")

# eşit uzunluktaki iç içe listeleri çok boyutta diziye çevirebiliriz
liste=[[1,2,3],[4,5,6]]
dizi=np.array(liste)
print(dizi)

print("\n*******\n")

# yeni diziler oluşturalım elemanlşarının hepsi 0 olsun ve 7 birim uzunluğunda olsun
dizi=np.zeros(7)
print(dizi)
print()
# elemanları birlerden oluşan bir dizi elde edelim
dizi=np.ones(7)
print(dizi)

print("\n*******\n")

# farklı boyutlarda dizi üretelim
# beş sütun 4 satırı olsun
# elemanları yine birlerden oluşsun
dizi=np.ones((5,4))
print(dizi)

print("\n*******\n")

# arange fonskyionu range gibidir
print(np.arange(10))

print("\n*******\n")

# pythonda tip belirtilmezse veri tipi oromatik olarak float olur
# oluşturacaüımız diziye veri tipini belli etmek için dtype kullanılır
dizi=np.array([1,2,3],dtype=int)
print(dizi)
print(dizi.dtype)

print("\n*******\n")

# dizinin veri tipini değiştrimek için astype() kulanılır
dizi2=dizi.astype(np.float64)
print(dizi2)
print(dizi2.dtype)

print("\n*******\n")

# dizilerle for döngüsü kullanmadan matematiksel işlem yapmak:
dizi=np.array([[1,2,3],[4,5,6]])
# aynı indexler aynı indexlerle çarpışır ya da toplanır
print(dizi*dizi)
print()
print(dizi+dizi)
print()
print(dizi-dizi)
print()
print(1/dizi)

print("\n*******\n")

# İNDEX İŞLEMLERİ
dizi=np.arange(10)
print(dizi)

print("\n*******\n")

# dizinin 7. indexine bakalım
print(dizi[7])

print("\n*******\n")

# 3. indexten başlayıp 8. indexe kadar olan elemanlarını görmek
print(dizi[3:7])
# bu elemanları 13 yapmak
dizi[3:7]=13
print(dizi)

print("\n*******\n")

# şimdi çok bpyutlu dizilerin indexlerine bakalım
dizi2b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2b)

print("\n*******\n")

# ilk bileşenine bakalım
print(dizi2b[0])

print("\n*******\n")

# 2. bileşeninin 3. elemnanını alalım
print(dizi2b[1][2])

print("\n*******\n")

# diziyi dilimleyelim
print(dizi2b[0:2])
print()
print(dizi2b[:2])

print("\n*******\n")

# 1. bileşeninin elemanlarını dilimleyelim
# birinci bileşeninin 2. indexe kadarki elemanlarını dilimleyelim
print(dizi2b[0,:2])

print("\n*******\n")

# 2. satıra kadar olan elemanlardan 1. sütun ve sonrakileri görelim
print(dizi2b[:2,1:])

print("\n*******\n")

# boolean tipinde dizi alalım
isimler=np.array(["ALi","Veli","Ayşe","Ali"])
veri=np.random.randn(4,3)
print(isimler)
print()
print(veri)

print("\n*******\n")

# isimler verideki satırlara denk gelsin
# ali ismine karşılık gelen satırın birinci indexten sonraki elemanlarını yazduralım
print(veri[isimler=="Ali",1:])

print("\n*******\n")

# ali ismi haricindeki sütunları seçelim
# ~ operatörü ters işlemler için kullanılır
print(veri[~(isimler=="ALi")])

print("\n*******\n")

# Ali veya Veli ismine karşılık gelen satırları seçelim
sec=(isimler=="Ali")|(isimler=="Veli")
print(veri[sec])

print("\n*******\n")

# verideki negatif değerlerin yerine 0 atayalım
veri[veri<0]=0
print(veri)

print("\n*******\n")

# çok boyutlu dizi oluşturalım
dizi=np.arange(12).reshape(3,4)
print(dizi)

print("\n*******\n")

# transposesini almak (satırları sütun olarak yazmak)
print(dizi.T)

print("\n*******\n")

# matrix çarpımını bulmak
print(np.dot(dizi.T,dizi))

print("\n*******\n")

print(dizi)
print()
# DİZİLER ÜSTÜNDE İSTATİSTİKSEL METOTKAR KULLANMAK:
print(dizi.mean())
print()
print(dizi.sum())
print()
# satırların ortalamasını alalım:
print(dizi.mean(1))
print()
# sütunların ortalamasını bulalım:
print(dizi.mean(0))

print("\n*******\n")

# sort() metodu ile elemanları sıralamak
print(dizi.sort())

print("\n*******\n")

# birden fazla elemandan sadece b,r tane almak için un,que kullanalım
say=np.array([1,1,1,2,3])
print(np.unique(say))

print("\n*******\n")

print("\n*******\n")

"""
NUMPY İLE BİLGİSAYARA VERİ KAYDEDEBİLİR YA DA ÇALIŞMA DİZİNİNDEN VERİ YÜKLEYEBİLİRİZ
"""

dizi=np.arange(10)
# diziyi kaydedelim
np.save("bir_dizi",dizi)
# kaydedilen diziyi yükleyelim
np.load("bir_dizi.npy")

print("\n*******\n")


print("\n*******\n")


print("\n*******\n")


print("\n*******\n")


print("\n*******\n")

