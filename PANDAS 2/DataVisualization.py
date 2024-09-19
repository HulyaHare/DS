import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# grafileri satır aralarında görmek için şunu yaparız
plt.style.use("fivethirtyeight")

# series yapısında bir veri oluşturalım ve değerler toplanarak gitsin
# verilerin toplanarak gitmesi için cumsum() kullanılır yani cumulativeden gelir
veri=pd.Series(np.random.randn(1000).cumsum())
veri.plot()
plt.show()

print("\n************\n")

# şimdi dataframe yapısında bir veri seti oluşturalım
df=pd.DataFrame(np.random.randn(100,4),columns=list("ABCD"))
df=df.cumsum() # veri setindeki değerlerin toplanarak gitmesini sağladık
df.plot()
plt.show()

print("\n************\n")

# farklı stilde grafik çizdirmek için kind kullan
# mesela df veri setinin 10 satırındaki bar grafiklerini çizdirelim
df.iloc[10].plot(kind="bar")
plt.show()

print("\n************\n")

# kind yerine plot metodunun nitelikleri kullanılarak da farklı grafikler çizdirilebilir
df.iloc[10].plot.bar()
plt.show()

print("\n************\n")

# çoklu bar grafikleri de çizdirilebilir
vs = pd.DataFrame(np.random.rand(7,3), columns=list("ABC"))
vs.plot.bar()
plt.show()

print("\n************\n")

# stacklanmış bar grafiği çizmek
# grafiği üst üste dizer bu stacked=True
vs.plot.bar(stacked=True)
plt.show()

print("\n************\n")

# barları yatarda görmek için barh metofu kullanılır
vs.plot.barh(stacked=True)
plt.show()

print("\n************\n")

# verinin dağılımını görmek içij histogramlar kullanılır
iris=pd.read_csv("iris.txt")
print(iris.head())

print("\n************\n")

# veri setindeki değişkenlerin aynı grafikte histogramlarını görelim
# grafiğin saydamlığını alpha belirler
iris.plot.hist(alpha=0.7)
plt.show()

print("\n************\n")

# stacklanmış halde histogramlarını görmek için stacked=True diyelim
# böylece sayıları üst üste toplanmış sayılar olarak göreliim
iris.plot.hist(alpha=0.7,stacked=True)
plt.show()

print("\n************\n")

# dikdörtgenlerin boyutlarını arttırabiliriz mesela 25 yapalım
# yani histogram 20 aralığa bölünecektir
iris.plot.hist(alpha=1,stacked=True,bins=25)
plt.show()

print("\n************\n")

# yatayda histogram çizdirmek bunun için orientation="horizontal" deriz
iris["sepal_en"].plot.hist(orientation="horizontal")
plt.show()

print("\n************\n")

# bir sütun için uygulanan fonksiyondann sonra da histogramlar çizilebilir
# her bir elemanı bir önceki elemandan çıkartan diff() metodunu uygulayalım mesela
iris["sepal_boy"].diff().hist()
plt.show()

print("\n************\n")

# herbir değişkenin ayrı ayrı hisytogramlarını çizelim
iris.hist(color="red",alpha=1,bins=20)
plt.show()

print("\n************\n")

# bu kod ile mevcut deaborm stillerini görebiliriz
print(plt.style.available)

print("\n************\n")

# histogram stilini değiştirebiliriz
plt.style.use("seaborn-v0_8-bright")
iris.hist(color="red",alpha=1,bins=20)
plt.show()

print("\n************\n")

# iris veri setini by ile gruplayarak histogramları görebilirz
# mesela petal_boy'unun herbir tür için histogramlarını görelim
iris.hist("petal_boy",by="tur")
plt.show()

print("\n************\n")

"""
kutu grafikleri süreklş bir değişkenin dağılımını gösterir
bu grafik dağışımın aralık değerini yani range, medianı, basıklığı, çarpıklığı ve aykırı yani outlier değerleri gösterir
kutu grafikleri için box kullanılır
"""

print("\n************\n")

# iris veri setinin her bir sütununun kutu grafiğinş çizdirelim
iris.plot.box()
plt.show()

print("\n************\n")

# istersek özelliklerin renkleri ayarlayabiliriz
# bunları grafiğe geçirmek için sözlük kullanılır
renk={"boxes":"red","whiskers":"blue","medians":"black","caps":"green"}
iris.plot.box(color=renk)
plt.show()

print("\n************\n")

# kutu grafipini yatayda çizdirmek için vert=False demeliyiz
iris.plot.box(vert=False)
plt.show()

print("\n************\n")

# aslında direl boxplot() dersek herbir sütunun kutu grafiğini çizdirebiliriz
iris.boxplot()
plt.show()

print("\n************\n")

# gruplanmış verilerin kutu grafiklerini çizdirmek
# mesela iris veri setindeki herbir değişken için türleri ayrı ayrı görmek isteyelim
iris.boxplot(by="tur")
plt.show()

print("\n************\n")

# grafiğin daha güzel görünöesi için stilini değiştirelim
# mesela ggplot stilinde görelim
plt.style.use("ggplot")
iris.boxplot(by="tur")
plt.show()