import pandas as pd
import numpy as np

# ZAMAN DAMGALARI AMERİKANIN ZAMAN FORMATINA GÖREDİR

# bir tarihi zaman damgasına çevirmek
print(pd.to_datetime("15/08/2019"))

print("\n*******\n")

# tarihleri index olarak alırsak analizlerei çoko kolay yapabiliriz
# yani farklı formattaki tarihleri datetime formatına to_datetime ile çevirelim
# errors=coerce ile geçersiz tarihleri naT yani not a Time yaptuk
# errors=ignore yazarsak görmezden gel anlamına gelirdi
trh=["2019-01-05","jan 6, 2019","7/05/2019","2019/01/9","20190110"]
# şimdi bu trh nesnesini datetime'ye çevirelim
print(pd.to_datetime(trh,errors="coerce"))

print("\n*******\n")

# 3. ayın 5. gününü zaman damgalı hale getirelim
print(pd.to_datetime("03/05/2019"))
print()
# tarihimizi avrupa formatında yazalım
print(pd.to_datetime("03/05/2019",dayfirst=True))

print("\n*******\n")

# tarihimizi avrupa formatında yazalım
# farklı formatlardaki tarihi çevirirken format kullanılır
# meseşa / yerine * kullanalım
print(pd.to_datetime("05*03*2019",format="%d*%m*%Y"))

print("\n*******\n")

#ipok değerini zaman damgasına çevirelim
# ipok bilgisayarların başladığı tarihten itibaren geçen zasaniye sayısına denir bu tarih 01/01/1970
# öntanıımlı olarak milisaniye okınur. bunu saniye çeviremek için unit=s yazılır
# önce bir milyar saniye geçtiyse bilgisayarlar başladığından beri o değerin karşılığını bulalom
t=1000000000
print(pd.to_datetime(t,unit="s"))

print("\n*******\n")

# frekanslar temel bir frekans ya da çarpımlardan oluşur
# temel frekanslar aylık M ya d günlük D gibi datetime offset denilen string argumanlardan oluşur
# bu date ofsetler frekans argumanı için kullanılır
# mesela 4'er saatlik aralarla oluşmuş tarih listesi yapalım:
print(pd.date_range("2010-01-01","2010-01-03",freq="4h"))

print("\n*******\n")

# her ayın son haftasının pazar günlerini alalım
print(pd.date_range("2010-01-01","2010-09-03",freq="WOM-4SUN"))

print("\n*******\n")

# periyodlar gün ay ve yıl gibi zaman damgalarını temsil eder
p=pd.Period(2020)
print(p)
print()
# p için kullanılabilicek metotlara bakalım
print(dir(p))

print("\n*******\n")

# bu periyodun başlangıç zamanını görelim
print(p.start_time)
# bu periyodun bitiş tarihini görelim
print(p.end_time)

print("\n*******\n")

# aylık periyıd alalım
a=pd.Period("2020-01",freq="M")
print(a)
# bu periyodun başlangıç zamanını görelim
print(p.start_time)
# bu periyodun bitiş tarihini görelim
print(p.end_time)

print("\n*******\n")

# eğer bu a tarihine beş eklersek ay olarak 5 gideriz çünkü ay tipinde oluşmuştu
print(a+5)
print(a-5)

print("\n*******\n")

# eğer iki periyodun frekansı aynıysa iki tarih arasındaki farkı bulabşkşrşz
print(p-pd.Period("2015"))

print("\n*******\n")

# period_range fonksiyonu ile düzenli tarih aralıkları üretebiliriz
rng=pd.period_range("2019-01-01","2019-08-30",freq="M")
print(rng)
print()
# bu periyod_index() nesnesi pandas için periyod alınabilir
print(pd.Series(range(8),index=rng))

print("\n*******\n")

# perion ve period index nesneleri s_frekans ile diğer bir frekansa çevrilebilir
# mesela yıllık periyodu aylık periyoda çevirelim
p=pd.Period("2019",freq="A-DEC")
# bu yıllık periyodun başlangıçtaki ayını aylık periyoda çevirelim
print(p.asfreq("M",how="start"))
print()
# son ayı alalım
print(p.asfreq("M",how="end"))

print("\n*******\n")

# 3 aylık veriler finans gibi alanlarda standarttır
# 3 aylık raporlar mali yılın sonunda rapor edilir
# ŞU KOMUT YILIN 4. ÇEYREĞİNİN DECEMBERDE BİTTİĞİNİ İFADE EDER
p=pd.Period("2019Q4",freq="Q-DEC")
print(p)
print(p.end_time)

print("\n*******\n")

# periyod ile 3 aylık tarihler üretelim
# freq olarak hangi 3 aylıktan başlayacağımız yazılır
rng=pd.period_range("2019Q3","2020Q4",freq="Q-JAN")
print(rng)

print("\n*******\n")

# bu period index nesnesi ile bir zaman serisi oluşturalım
zs=pd.Series(range(len(rng)),index=rng)
print(zs)

print("\n*******\n")

# Series ve Dataaframe nesneleri to_period() ile Periyoda çevrilebilir
rng=pd.date_range("2020-01-01",periods=5,freq="M")
# bu tarih aralığını index kabul eden zaman serisi oluşturalım
zs=pd.Series(range(len(rng)),index=rng)
print(zs)

print("\n*******\n")

# şimdi bu zaman serisini periyot tipine dönüştürelim
pzs=zs.to_period()
print(pzs)
print()
# bu verinin index yapısına bakalım (PeriyodIndex olcak)
print(pzs.index)