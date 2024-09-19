# dosyadaki veriler virgül ile ayrılmışsa read_csv kullan
# dosyadaki veriler bir tab boşlık ile ayrılmışsa read_table kullan
import pandas as pd
df=pd.read_table("veri.txt")
print(df)
print()
df2=pd.read_table("veri2.txt")
print(df2)

print("\n************\n")

# veri setini tablo halinde görmek (yani virgülleri kaldırıcaz)
df2=pd.read_table("veri2.txt",sep=",")
print(df2)

print("\n************\n")

# veri setinde sütun isimleri yoksa  bunu pythone bildirmemiz gerek çümkü
# mesela veri2 veri setinde sütun isimleri olmadığı için Ali.80 ve E otomatik olarak sütun isimleri oldu, ama olmamalıydı
# bunu header=none diyere sütun ismi olmadıüını belirtebiliriz
df2=pd.read_table("veri2.txt",sep=",",header=None)
print(df2)

print("\n************\n")

# sütun isimlerini kendimiz verebiliriz:
df2=pd.read_table("veri2.txt",
                  sep=",",
                  header=None,
                  names=["isim","puan","cinsiyet"])
print(df2)

print("\n************\n")

# isim sütununu index olarak kullanmak istersek şöyle yapıcaz:
df2=pd.read_table("veri2.txt",
                  sep=",",
                  header=None,
                  names=["isim","puan","cinsiyet"],
                  index_col="isim")
print(df2)

print("\n************\n")

df3=pd.read_table("veri3.txt",
                  sep=",")
print(df3)
print()
# eğer veri seti çoklu sütunlardan oluşuyorsa ve
# biz bu veri setini aşamalı hale getirmek istersek:
df3=pd.read_table("veri3.txt",
                  sep=",",
                  index_col=["ders","isim"])
print(df3)

print("\n************\n")

df4=pd.read_table("veri4.txt",sep=",")
print(df4)
print()
# veri4 ismindeki yorun satırı olan 1. ve 3. satırları okutmak istemiyoruz bunun için skip row kullanıcaz
# skiprows=[0,2] demeliyiz çünkü o. ve 2. satırlaru okutmak istemiyoruz
df4=pd.read_table("veri4.txt",sep=",",skiprows=[0,2])
print(df4)

print("\n************\n")

# veri4'deki ilk iki sütunu okutmak istiyoeuz: usecols=[0,1]
# toplam ekrande görünecek satır sayısı da 3 olsun: nrows=3
df4=pd.read_table("veri4.txt",
                 sep=",",
                 skiprows=[0,2],
                 usecols=[0,1])
print(df4)

print("\n************\n")

# EKSİK VERİ OLAN VERİ SETLERİYLE ÇALIŞMAK:
df5=pd.read_table("veri5.txt",sep=",")
print(df5)

print("\n************\n")

# tablodaki null değerleri True gösterie ama null olmayanları False gösterir
print(pd.isnull(df5)) # df5.isnull()   eğer bu şekilde yazsak da aynı şey olurdu

print("\n************\n")

# ama yanlış oldu çünkü mesela puan -5 olamaz o yüzden o kısım da true olmaluydu ama false oldu
# ya da cinsiyet n.a olamaz yani bunun gibi olmaması gereken şeyleri de eksik veri alacak şekilde kodumuzu düzenleyelim

df5=pd.read_table("veri5.txt",sep=",",na_values=["n.a",-5])
print(df5)

print("\n************\n")

# ama cinsiyet içinde bir efe değeri var ki bu da olmaması gerekliydi
# efe değeri cinsiyet içindeyken NaN olmalı ama eğer isimdeyse NaN olmamalı. Buna göre ayarlayalım
# bu sorunu gidermek için şunu yapmalısım:
# HER BİR SÜTUNDAKİ EKSİK VERİLERİ SÖZLÜK İÇİNDE YAZ
eksik_veri={"puan":[-5],"cinsiyet":["n.a","Efe"]}
df5=pd.read_table("veri5.txt",sep=",",na_values=eksik_veri)
print(df5) # görüldüğü gibi cinsiyet sütunundaki Efe eksik veri oldı ama isim sütunundak, Efe eksik veri olmadı
print()
print(pd.isnull(df5))




print("\n************\n")

# veri setini csv formatında yazdırmak:
df=pd.read_table("veri.txt")
# şimdi bu df veri setini virgülle ayrılmış formatta dış kaynağa yazdıralım:
df.to_csv("yeni_veri.csv") # böylece df veri seti yeni_veri şeklinde kaydedilmiş oldu
# verideki değerleri ayırmak için bu sefer virgül yerine | yazalım
import sys
# eksik veriler için na_rep="NULL" yaz:
print(df.to_csv(sys.stdout,sep="|",na_rep="NULL"))
#satır ve sütun isimlerini kaldırmak için şunu yap:
print(df.to_csv(sys.stdout,sep="|",na_rep="NULL",index=False,header=False))
# sadece belirli sütınşarı yazdırmak:
print(df.to_csv(sys.stdout,sep="|",index=False,columns=["isim","puan"]))