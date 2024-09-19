import pandas as pd
import numpy as np

vs=pd.DataFrame({"anahtar1":list("aabbab"),
                 "anahtar2":["bir","iki","uc"]*2,
                 "veri1":np.random.randn(6),
                 "veri2":np.random.randn(6)})
print(vs)

print("\n************\n")

# şimdi anahtar1'in kategorileri için veri1'in ortalamalarını alalım
grup=vs["veri1"].groupby(vs["anahtar1"])
print(grup.mean())

print("\n************\n")

# iki anahtar sütuna göre gruplama yapmak:
ort=vs["veri1"].groupby([vs["anahtar1"],vs["anahtar2"]])
print(ort.mean())
print()
# tablo halinde şöyle gösterebilirsin:
print(ort.mean().unstack())

print("\n************\n")

# veri1 ve veri2 için ayrı ayrı ortalama hesaplamak
print(vs.groupby("anahtar1").mean(numeric_only=True))

print("\n************\n")

# iki anahtar sütuna göre de ortalama hesaplanabilir
print(vs.groupby(["anahtar1","anahtar2"]).mean())

print("\n************\n")

# group by nesnesine göre iterasyon yapılabilir
for isim,grup in vs.groupby("anahtar1"):
    print(isim,grup)

print("\n************\n")

# iki anahtara göre de şöyle yapılır
for (x1,x2),grup in vs.groupby(["anahtar1","anahtar2"]):
    print(x1,x2,grup)

print("\n************\n")

# anahtar sütundaki herhangi bir gruba göre veri setini parçalamak
print(list(vs.groupby("anahtar1")))
print()
parca=dict(list(vs.groupby("anahtar1")))
print(parca)
print()
# a grubunu ekrana yazdıralım:
print(parca["a"])

print("\n************\n")
print("\n************\n")


oyun=pd.read_csv("vgsalesGlobale.csv")
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)  # Tüm DataFrame'i tek satırda gösterme
print(oyun.head())
print()
print(oyun.dtypes)

print("\n************\n")

# bu veri setindeki sayısal değişkenler için özet istatistikleri describe ile görelim ve dropna ile eksik veri bulunan satırları kaldıralım
print(oyun.dropna().describe())

print("\n************\n")

# # global satışların ortalamalatını bulalım
print(oyun.Global_Sales.mean())

print("\n************\n")

# oyun türlerine göre grup nesnesini oluştıralım
grup=oyun.groupby("Genre")

# oyun türlerine göre global satışların sayısını görelim
print(grup["Global_Sales"].count())

print()

# oyun tğrlerime göre global satışların göre özet istatistikleri görmek
print(grup["Global_Sales"].describe())

print()

# oyun türlerine göre tüm sayısal tipteki sütunların türlere göre ortalamalarını bulmak:
print(grup.mean(numeric_only=True))

print("\n************\n")

# türlere göre global satış ortalamalarının bar grafiğini görmek:
# ortalamayı bulup grafiğin tipini bar grafiği yap
# sonra grafiği göster
import matplotlib.pyplot as plt
grup["Global_Sales"].mean().plot(kind="bar")
plt.show()

print("\n************\n")

# gruplamalar sözlük ya da Series veri yapısından da olabilir
meyve=pd.DataFrame(np.random.randn(4,4),
                   columns=list("abcd"),
                   index=["elma","kiraz","muz","kivi"])
print(meyve)

print("\n************\n")

# sütunları gruğlamak için sözlğk veri yapısını kullanarak veri seetindeki sütunları haritaayalım
etiket={"a": "yesil","b":"sari","c":"yesil","d":"sari","e":"mor"}

# şimdi bu etiketi kullanarak gruplama yapalım:
# ön tanımlı olarak satırlara göre gruplama yapılır ama biz sğtunlara göre gruplama yapacağımız için axis=1 diyelim
grup=meyve.groupby(etiket,axis=1)

# bu grupların toplamını bulalım
print(grup.sum())

print("\n************\n")

# bunu series veri yapısı için de yapabiliriz
s=pd.Series(etiket)
print(s)

print("\n************\n")

# şimdi s değişkeniyle grupları oluşturalım ve herbir grup için meyve sayılarını bulalım
# yine sütunlaru gruplayalım

print(meyve.groupby(s,axis=1).count())

print("\n************\n")

# meyvelerşn harf sayısına göre gruplayıp her bir gruptaki meyvelerin değerlerinin toplamını bulalım
print(meyve.groupby(len).sum())

print("\n************\n")

print("\n************\n")

# hiyerarşik indexlerle gruplama yapalım:
# çnce hiyerarşik indexlere sahip bir veri seti oluşturalım
veri=pd.DataFrame(np.random.randn(4,5),
                  columns=[list("AAABB"),[1,2,3,1,2]])
veri.columns.names=["harf","sayi"]
print(veri)

print("\n************\n")

# veriyi harf indexlerine göre gruplandıralım ve sütunlara göre gruplama yağalım
# böylece veri sweti her bir harf için gruplandı ve herbirine o harfteki sütunların toplamı yazıldı
print(veri.groupby(level="harf",axis=1).sum())

print("\n************\n")

print("\n************\n")

oyun=pd.read_csv("vgsalesGlobale.csv")
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)  # Tüm DataFrame'i tek satırda gösterme
print(oyun.head())
print(oyun.dtypes)
print(oyun.dropna().describe())

print("\n************\n")

# # global satışların ortalamalarını bulalım:
print(oyun.Global_Sales.mean())

print("\n************\n")

# oyun trüne göre oyun nesnesini oluşturalım
grup=oyun.groupby("Genre")

print("\n************\n")

# oyun türlerine göre globak satışların sayısını görelim
print(grup["Global_Sales"].count())

print("\n************\n")

# oyun tğrleirine gçre gruplanmış oyunların global satışlarının özet istatistikleri
print(grup["Global_Sales"].describe())

print("\n************\n")

# tüm sayısal tipteki sütunların türlere göre ortalamalarını bulmak
print(grup.mean(numeric_only=True))

print("\n************\n")

# türlere göre global satış ortalamalarının bar grafiğini görmek:
# türlere göre global satış ortalamalarının bar grafiğini görmek:
# ortalamayı bulup grafiğin tipini bar grafiği yap
# sonra grafiği göster
import matplotlib.pyplot as plt
grup["Global_Sales"].mean().plot(kind="bar")
plt.show()

print("\n************\n")

# türlere göre amerika ve avrupa ve japonyadaki oyun satışının ortalamalarının bar grafiğini görmek:
grup[["NA_Sales","EU_Sales","JP_Sales"]].mean().plot(kind="bar")
plt.show()

print("\n************\n")

