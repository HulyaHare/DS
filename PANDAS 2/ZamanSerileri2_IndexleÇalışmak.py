import pandas as pd
import numpy as np

# frekans son 3 gün olsun
rng=pd.date_range(start="2010",end="2019",freq="BM")
print(rng)
print()
# bu tarihleri index alan veri oluşturalım
# notmal dağılımla üretilecel sayıların uzunluğu rng'nin uzunluğu kadar olsun
ts=pd.Series(np.random.randn(len(rng)),index=rng)
print(ts)

print("\n*************\n")

print(ts.index)
print()
# indexleri dilimleyelim
print(ts[:5].index)

print("\n*************\n")
fb=pd.read_csv("FB.csv")
print(fb.head())

print("\n*************\n")

# verisetindeki sütunların tipine bakalım
print(fb.dtypes)

print("\n*************\n")

# tarih(Date) sütununu datetime tipine getirelim
fb=pd.read_csv("FB.csv",parse_dates=["Date"])
print(fb.dtypes)

print("\n*************\n")

# Date sütununu index yapalım
fb=pd.read_csv("FB.csv",parse_dates=["Date"],index_col="Date")
print(fb.head())

print("\n*************\n")

# 2019'un 6. ayının değerlerine bakalım
# eper Date sütununun tipini datetime yapmasaydık bu işlemi yapamazdık
print(fb.loc["2024-01"])

print("\n*************\n")

# bu aydaki kapanış fiyatlarının ortalamasını görelim
print(fb.loc["2024-01"].Close.mean())

print("\n*************\n")

fb=fb.sort_index()
# tarihler index olduğu için tarihleri dilimleyebiliriz
print(fb.loc["2024-01-05":"2024-02-13"].head())

print("\n*************\n")

# bir tarihi timestamp formatına çevirebiliriz
t=pd.to_datetime("1/26/2024")
print(t)
print()
# bu tarih ile veri setindeki tarihleri karşılaştırabiliriz
# veri setnde bu tarihten sonrKİ verileri ekrana yazdıralım
print(fb.loc[fb.index>=t,:])

print("\n*************\n")

#şimdi tarihsiz bir veri setine tarihi kendimiz ekleyip kullanmayı görelim
fb1=pd.read_csv("FB1.csv")
print(fb1.head())
print()
# şimdi veri setine tarih sütunu eklicez:
# önce tarihler üreteceğiz
dates=pd.date_range(start="03/01/2019",end="03/29/2019",freq="B") # B iş günlerini yani haftaiçini temsil eder
# şimdi indeximizi veri setine atayalım
fb1.set_index(dates,inplace=True)
print(fb1.head())

print("\n*************\n")

#index olarak atanan tarihlere bakalım yani ibdexleri kontrol edelim
print(fb1.index)

print("\n*************\n")

# satış işlemleri grafiği çizdirelim
import matplotlib.pyplot as plt
fb1.Close.plot()
plt.show()

print("\n*************\n")

# veri setinde tatil günlerinin değerleri yoktu
# eğer tatil günlerini de veri setine son iş günündeki dğerleri atamak üzrer ekleyelim
# asfreq özellikle eksik tarihler varsa veya belirli bir frekansta veriye ihtiyacınız varsa kullanışlıdır.
# D hedef frekanstır günlük veriyi belirtir
# pad: eksik değerler için çnceki değeri taşımayı sağlayan metttur
print(fb1.asfreq("D",method="pad").head())
# eğer değerşeri haftalık olarak görmek istersek D yerine W yazarız

print("\n*************\n")

# periyod girerek de tar,h değerleri üretebiliriz
z=pd.date_range(start="3/1/2019",periods=60,freq="B") # frekans olarak haftaiçi aldık
print(z)

print("\n*************\n")

# kendimiz zaman serisi veri seti üretebilriiz
zs=pd.Series(np.random.randint(1,10,len(z)),index=z)
print(zs.head())