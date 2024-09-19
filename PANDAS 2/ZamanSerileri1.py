import pandas as pd
import numpy as np
from datetime import datetime

tarih=[datetime(2020,1,5),
       datetime(2020,1,10),
       datetime(2020,1,15),
       datetime(2020,1,20),
       datetime(2020,1,25)]

# indexi bu tarih nesnesi olan bir series yapısı oluşturalim
zs=pd.Series(np.random.rand(5),index=tarih)
print(zs)

print("\n*******\n")

# bu zaman serisinin indexini kontrol edelim
print(zs.index)

print("\n*******\n")

# ZAMAN DAMGASI : TİMESTAMP
"""
zaman serisiyle çalışmak için 3 tür yapı kullanılır:
1-) Timestamps:
    datetime modülüne benzer 
    bu tipin yapısı datetime index şeklindedir
2-) Period:
    perion başlangıç ve bitiş tarihleri olan bir zaman aralığından oluşur
    bu tip sabit aralıklı tarihlere dayanır
3-) Timedelta:
    iki tane zaman arasındaki süreyi gösterir
"""

print("\n*******\n")

# tek bir tarihi zaman damgasına çevirmek için to_datetime() kullanılır
print(pd.to_datetime("01/01/2020"))
print()
# to_datetime() farklı formatlardaki zaman yapılarını zaman damgasına çevirir
dates=pd.to_datetime([datetime(2020,7,5),
                      "6th of July, 2020",
                      "2020-jul-7",
                      "20200708"])
print(dates)

print("\n*******\n")

# herhangi bir datetime index to_pediod() kullanılarak period index yapılabilir
print(dates.to_period("D"))

print("\n*******\n")

# bir tarihten diğer bir tarihi çıkartarak time delta index yapısı oluşturmak
print(dates-dates[0])

print("\n*******\n")

"""
 düzenli tarih serileri oluşturmak için farklı fonksiyonlar vardır:
 timestamps için --> pd.date_range()
 periyot için --> pd.period_range()
 timedelta içim --> pd.timedelta_range()
"""

# baş ve sonu verilen o aralıkta bir zaman serisi oluşturalım
print(pd.date_range("2020-8-15","2020-09-10"))

print()

# 10 periyotluk zaman serisi oluşturalım
print(pd.date_range("2020-07-15",periods=10))

print()

# periypt aralığı oluştururken frakensı da tanımlayabiliriz
# mesela öntanımlı olarak date_range() fonksiyonun frekans aralığı 1 gündür
# bu frekansı bir saat yapalım
print(pd.date_range("2020-07-15",periods=10,freq="H"))

print("\n*******\n")

# period aralığı oluşturalım
print(pd.period_range("2020-10",periods=10,freq="H")) # aylık yapmak istersek M yazaarız

print("\n*******\n")

# bir saatlik artış ile süre serisi oluşturalım
print(pd.timedelta_range(0,periods=8,freq="H"))

print("\n*******\n")

# zaman serisinin birinci indexini bir değişkene atayalım
damga=zs.index[1]
print(damga)
print()
# şimdi bu damganın değerini çağıralım
print(zs[damga])
# zaman damgalı değeri ekrana yazdıralım
print(zs["25.1.2020"])
# şimdi de farklı formatta yazdıralım
print(zs["20200125"])

print("\n*******\n")

# uzun zaman serileriyle de oynayabiliriz
uzun_zs=pd.Series(np.random.randn(1000),
                  index=pd.date_range("1/1/2020",periods=1000))
print(uzun_zs.head())
print()
# veya 2020 yılındaki 10. ayın tarihlerinin ilk beş satırını görelim
print(uzun_zs["2020-10"].head())

print("\n*******\n")

# isterseniz datetime ile tarihkleri dilimleyebilirsiniz
# 20.09.2020 tar,h,nden sonrali tarihleri görelim
print(uzun_zs[datetime(2020,9,20):])

print("\n*******\n")

# mesela 1.15.2020 tarihine kadar olan rarihleri görelim
print(zs.truncate(after="1/15/2020"))

print("\n*******\n")

# şimdi daterange ile bir tarih değişkeni oluşturalım
# frekans olarak haftalık pazar günlerini alalım
tarih=pd.date_range("1/1/2020",periods=100,freq="W-SUN")
# bu tarih değişkenini index alan bir dataframe oluştıralım
uzun_df=pd.DataFrame(np.random.randn(100,4),
                     index=tarih,
                     columns=list("ABCD"))
print(uzun_df)

print("\n*******\n")

# veri setindeki 2020 yılının 10. ayındaki değerleri görelim
print(uzun_df.loc["2020-10"])

print("\n*******\n")

# bazı durumlarda veriler tekrar edebilir
tarih=pd.DatetimeIndex(["1/1/2020",
                        "1/2/2020",
                        "1/2/2020",
                        "1/2/2020",
                        "1/3/2020",])
print(tarih)
print()
# bu tarih nesnesini index kabul eden Series yapısında bir zaman serisi oluşturalım
zs1=pd.Series(np.arange(5),index=tarih)
print(zs1)

print("\n*******\n")

# veride tekrar eden niteliğin olup olmadığı is_unique() ile kontrol edilir
# False çıkarsa demekki tekrar eden veriler var anlamına gelir
print(zs1.index.is_unique)

print("\n*******\n")

# tarihlerin kaçar kez tekrar ettiğini bulmak için gruplayıp yapmamız gerek
grup=zs1.groupby(level=0)
print(grup.count())

print("\n*******\n")

# gruplanmış tarihlerin ortalamanlarını bulalım
print(grup.mean())