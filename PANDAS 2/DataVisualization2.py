import random

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

# grafiklerin alan grafiklerini çizelim
df=pd.DataFrame(np.random.rand(10,4),columns=list("ABCD"))
print(df.head())

print("\n************\n")

# df veri setindeki A sütununun alan grafiğini çizdirelim
df["A"].plot.area()
plt.show()

print("\n************\n")

# bütün sütunların alan grafiklerini çizdirelim
df.plot.area()
plt.show()

print("\n************\n")

# alan grafikleri öntanımlı olarak üst üste binmiş yani staklanmış halde gelşr
# stacklanmamış grafik şöyle çizdirilir
df.plot.area(stacked=False)
plt.show()

print("\n************\n")

# alan grafiği çizdirilirken eğer eksik veri varsa otomatik olarak bu değer 0 olur
# eksik verileri kaldırmak içim fillna kullanılır

print("\n************\n")

# iki sayısal değişkenin arasındaki ilişkiyi görmek için saçılım grafiği çizilir
# saçılım grafiği için plot.scatter() kulanılır
# df veri setindeki A ve B değişkenlerinin saçılım grafiğini çizelim
df.plot.scatter(x="A",y="B")
plt.show()

print("\n************\n")

# şimdi iris veri setini alalım önce okutalım
iris=pd.read_csv("iris.txt")
print(iris.head())

print("\n************\n")

# sepal_boy ve sepal_en arasındaki ilişkiyi görmek için saçılım grafiğini çizdirelim
iris.plot.scatter(x="sepal_boy",y="sepal_en")
plt.show()

print("\n************\n")

# iki çift değişkenin saçılım grafiğini bir grafikte görelim
ax_degiskeni=iris.plot.scatter(x="sepal_boy",y="sepal_en",color="Blue",label="Sepal")
iris.plot.scatter(x="petal_boy",y="petal_en",color="Red",ax=ax_degiskeni)
plt.show()

print("\n************\n")

# iki değişkeni karşılaştırırken herbir noktanın rengini ayarlamak
iris.plot.scatter(x="sepal_boy",y="sepal_en",c="petal_boy",s=100)
plt.show()

print("\n************\n")

# grafikteki noktaların her birinin boyutunu ayarlamak
iris.plot.scatter(x="sepal_boy",y="sepal_en",s=iris["petal_boy"]*50)
plt.show()

print("\n************\n")

# verideki gözlem sayısı fazla ise hektegonal grafik kullan
df=pd.DataFrame({"a":np.random.randn(1000),
                 "b":np.arange(1000)})
# gridsize, x ekseni üzerindeki altıgenlerin sayısını belirler yani 25 yerine 10 yazarsan altıgenler büyür çünkü sayısı azaldı
df.plot.hexbin(x="a",y="b",gridsize=25)
plt.show()
print()
df.plot.hexbin(x="a",y="b",gridsize=10)
plt.show()

print("\n************\n")

print("\n************\n")

# pasta grafiği için plot.pie() metodu kullanılır
s=pd.Series(3*np.random.rand(5),index=list("ABCDE"),name="series")
s.plot.pie()
plt.show()

print("\n************\n")

# şimdi de dataframe veri yapısında veri setleri için pasta grafiğine bakalım
df=pd.DataFrame(3*np.random.rand(4,2),index=list("abcd"),columns=list("xy"))

# veri setinin herbir sütunu için ayrı ayrı pasta ggrafiği oluşturalım
df.plot.pie(subplots=True)
plt.show()

print("\n************\n")

# pasta grafiklerinde etiket gibi başka özellikleri de ayalanabilir
s.plot.pie()
plt.show()
# şimdi bunun özelliklerimni değiştirelim
s.plot.pie(labels=["efe","ali","can","nur","ata"],
           colors=list("brgmk"),
           fontsize=25,
           figsize=(10,10))
plt.show()

print("\n************\n")

# plot.kde() ile yoğunluk grafiği çizilebilir
iris.plot.kde()
plt.show()

print("\n************\n")

# verilerin saçılım matrix grafiğini çizebiliriz
from pandas.plotting import scatter_matrix
# iris veri setindeki saıysal sütunların ikişerli saçılım grafiklerini gösterelim
# alpha: görünürlüğü belirler
# diagonal="kde" : köşelere yoğunluk grafiği çizilmesini istediğimizi belli eder
# BÖYLECE KÖŞELERİNDE YOĞUNLUK GRAFİĞİ BULUNAN SAÇILIM MATRİX GRAFİĞİ ÇİZİLDİ
scatter_matrix(iris,alpha=0.5,diagonal="kde")
plt.show()

print()

# ama yazıların boyutu büyük oldu p yüzden stilini değiştirelim
plt.style.use(("ggplot"))
scatter_matrix(iris,alpha=0.5,diagonal="kde")
plt.show()
# BÖYLECE KÖŞELERİNDE YOĞUNLUK GRAFİĞİ BULUNAN GGPLOT STİLİNDE SAÇILIM MATRİX GRAFİĞİ ÇİZİLDİ

