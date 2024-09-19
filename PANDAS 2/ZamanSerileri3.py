import pandas as pd
import numpy as np

# resampling gruplandırma yapar ve zaman serisini bir frekanstan diğer bir frekansa çevirir
fb=pd.read_csv("FB.csv",parse_dates=["Date"],index_col="Date")
print(fb.head())

print("\n*******\n")

# aylık gruplandırmaları resample ile görelim
# onların ortalamalrını alalım
print(fb.resample("M"))
print()
print(fb.resample("M").mean())

print("\n*******\n")

# veri setinin aylık kapanış fiyatlarının ortalaman değerlerşni görelim ve grafiğini çizdirelim
import matplotlib.pyplot as plt
fb.Close.resample("M").mean().plot()
plt.show()

print("\n*******\n")

# ççeyrek aralıkların ortalamalarını çizdirelim ama bar grafiği olsun
fb.Close.resample("Q").mean().plot(kind="bar")
plt.show()

print("\n*******\n")

# shifting değerleri zaman boyunca ileri ya da geri gitmeyi gösterir
fb1=pd.DataFrame(fb.Close["2024-02"])
print(fb1.head())

print("\n*******\n")

# şimdi değerşeri iki tarih ileri öteleyelim
# geriye ötelemek isteseydik -2 derdik
print(fb1.shift(+2))

print("\n*******\n")

# bu değişikliğpi ortjinal verilerle aynı tabloda görelim
# herbir tarihteki değeri bir sonraki tarihe ötelenmiş olarak bulacağız
fb1["Bir Önceki Fiyat"]=fb1.shift(1)
print(fb1)

print("\n*******\n")

# bir günlük değişimin yüzdesini bulalım
fb1["Bir Günlük Fark"]=fb1["Close"]-fb1["Bir Önceki Fiyat"]
print(fb1)

print("\n*******\n")

# zamöan serisine bir günlük değişimin yüzdesini hesaplayalım
fb1["Yüzde Degisim"]=(fb1["Close"]-fb1["Bir Önceki Fiyat"])*100/fb1["Bir Önceki Fiyat"]

print("\n*******\n")

# tshift metodu indexi ileri veya geri oynatır
fb2=fb1[["Close"]]
print(fb2.head())

print("\n*******\n")

print(fb2.index)
print()
# förüldüğü gibi frekans bulunmamaktadır
# date_range ile frekans atayalım
# date_range içine başlangıç tarihi yazılır
# B iş günşerini temsil eder
fb2.index=pd.date_range('2024-02-21',periods=3,freq="B")
print(fb2.index) # artık frekansı var

print("\n*******\n")

# bir günlük indexi ileri öteleyelim
print(fb2.shift(1))

print("\n*******\n")

# window fonksiyonları verileri düzleştirmek içim kulllanılır
# mesela rollimg 10 ifadesi 10 günün ortalamasını bulır
fb.Close.rolling(10).mean().plot()
plt.show()

print("\n*******\n")

# ZAMAN BÖLGESİ
# pythonda zaman bölgesi pytz kütüphanesi ile sağlanır
import pytz
# türkiyenin zaman bölgeisne bakalım:
print(pytz.timezone("Turkey"))

print("\n*******\n")

# amerika newyorukun zaman bölgeisni görelim:
print(pytz.timezone("America/New_York"))

print("\n*******\n")

# bölgenin zaman bölgesinden 7 saat geride olan yerleri bulalım:
print(pytz.common_timezones[-7:])

print("\n*******\n")

# tarih değerleri üretelim
x=pd.date_range("12/9/2009 9:30",periods=6,freq="D")
zs=pd.Series(np.random.randn(len(x)),index=x)
print(zs)

print("\n*******\n")

# indexlerin zaman bölgelerini kontrol ederim:
print(zs.index.tz)

print("\n*******\n")

# şimdi tarihleri zaman bölgesine göre düzenleyelim
# herbir tarihi uluslararsı zaman bölgesine göre düzenşeyelim:
zs_utc=zs.tz_localize("UTC")
print(zs_utc)

print("\n*******\n")

# özel bir bölgeye göre zaman serisini düzenşeyeilim
# mesela hawaiiye göre düzenlşeyelim
# yani herbir tarihini havai zaman bölgesi tipinde yazalım
print(zs_utc.tz_convert("US/Hawaii"))

print("\n*******\n")

# bir zaman damgalı tarihi uluslararsı zaman bölgesi tipine dönüştürelim
zdamga=pd.Timestamp("2019-06-26 05:00")
zdamga_utc=zdamga.tz_localize("utc")
print(zdamga_utc)

print("\n*******\n")

# istabnul reels saatine dönüştürelim
print(zdamga_utc.tz_convert("Europe/Istanbul"))

print("\n*******\n")

# farklı bölgelerdeki iki zaman serisi birleştirilirse sonuçlar uluslararsı zaman serisine göre gösterilir
zs1=zs[:5].tz_localize("Europe/Berlin")
zs2=zs[2:].tz_localize("Europe/Istanbul")
sonuc=zs1+zs2
print(sonuc.index) # sonuçlar uluslararsı merkezi zamana göre gölrüldü

print("\n*******\n")


print("\n*******\n")


print("\n*******\n")


print("\n*******\n")


print("\n*******\n")


print("\n*******\n")


print("\n*******\n")

