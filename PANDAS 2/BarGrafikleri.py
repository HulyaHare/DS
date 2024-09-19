import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# grafik stiki olarak fivethiryeight seçelim
plt.style.use("fivethirtyeight")

mat=np.random.randint(50,100,7)
fen=np.random.randint(50,100,7)
ing=np.random.randint(50,100,7)
sinif=list("ABCDEFG")

# grafik nesnesi oluşturalım
fig=plt.figure()
# grafik alanlarını oluşturalım
ax=plt.axes()

# önce çizgi grafiği çizelim
plt.plot(sinif,mat,label="mat ort")
plt.plot(sinif,fen,label="fen ort")
plt.plot(sinif,ing,label="ing ort")
# etiketlediğimiz isimleri grafikte kullanmak için legend() yazalım
plt.legend()
# grafiğe başlık verelim
plt.title("Sınıfların Ders Ortalamaları")
# eksenleri isimlendirelim:
plt.xlabel("Sınıflar")
plt.ylabel("Ortalamalar")
plt.show()

print("\n************\n")

# x ekseninde kategorik değişken varsa bar grafiği çizmek daha amnlaşılırdir
# bar grafiği çizmek için plot() yerine bar yazılır
plt.bar(sinif,mat,label="mat ort")
plt.bar(sinif,fen,label="fen ort")
plt.bar(sinif,ing,label="ing ort")
# etiketlediğimiz isimleri grafikte kullanmak için legend() yazalım
plt.legend()
# grafiğe başlık verelim
plt.title("Sınıfların Ders Ortalamaları")
# eksenleri isimlendirelim:
plt.xlabel("Sınıflar")
plt.ylabel("Ortalamalar")
plt.show()

print("\n************\n")

# ancak üst üste gelmiş yani stacklanmış barlar çizildi
# verilerin ayrı ayrı barlarını görmek için öncelikle verileri indexleyelim
x_index=np.arange(len(sinif))
# ayrıca barların üsst üste binmesini engellemek için en isminde bir dğeişken tanımlayalım
# herbir grafiğin indexinin farklı olması için bu değişkeni metotlarda kullanalım
en=0.25
# yani en değerini ekleyip çıkarark herbir grafiğin x eksenindeki yerini farklı yapıcaz
# barların genişliği öntanımlı olarak 0.8 gelir aöa bunu width argumanııyla en kadar genişlikte yapalım
plt.bar(x_index-en,mat,width=en,label="mat ort")
plt.bar(x_index,fen,width=en,label="fen ort")
plt.bar(x_index+en,ing,width=en,label="ing ort")
# etiketlediğimiz isimleri grafikte kullanmak için legend() yazalım
plt.legend()
# grafiğe başlık verelim
plt.title("Sınıfların Ders Ortalamaları")
# eksenleri isimlendirelim:
plt.xlabel("Sınıflar")
plt.ylabel("Ortalamalar")
plt.show()

print("\n************\n")

x_index=np.arange(len(sinif))
en=0.25
plt.bar(x_index-en,mat,width=en,label="mat ort")
plt.bar(x_index,fen,width=en,label="fen ort")
plt.bar(x_index+en,ing,width=en,label="ing ort")
plt.legend()
# x eksenine dikkat edersen sayılar var
# bu x eksenindeki sayıları sınıf değerleriyle değiştirelim
# bunun için xticks() kullanılır
# yani x_indexe sınıftaki şeyleri yazalım
# böylece x eksenine sayılar yerine sınıf etiketleri yazıldı
plt.xticks(ticks=x_index,labels=sinif)
plt.title("Sınıfların Ders Ortalamaları")
plt.xlabel("Sınıflar")
plt.ylabel("Ortalamalar")
plt.show()

print("\n************\n")

print("\n************\n")

# HATA BARLARI
# hata çubukları grafiğini görelim
# x ekseni için 0 ile 30 arasında 30 tane sayı oluşturalım
x=np.linspace(0,10,30)
y=np.random.randint(0,5,30)
# öncelikle saçılım garfiğini çizdirelim
plt.plot(x,y,"bo")
plt.show()

print("\n************\n")

# şimdi hata barları ekleyelim
plt.plot(x,y,"bo")
# y ekseni boyunca olan hata çubuklarının uzunluğunu 1 yapmak için yerr=1 deriz
# fmt argumanı hata çubuklarının renk ve görünümünü ayarlar yani fmt="k." dersek siyah renkli n ve ortasında noktayla belli edilmiş çubular olur
plt.errorbar(x,y,yerr=1,fmt="k.")
plt.show()

print("\n************\n")

# istersek errorbar içine farklı özellikler de ekleyebiliriz
# mesela hata çubujlarının rengi yani ecolor kırmızı olsın
# hata çubujlarının genişliği yani elinewidth=2 olsun
plt.plot(x,y,"bo")
plt.errorbar(x,y,yerr=1,fmt="k.",ecolor="red",elinewidth=2)
plt.show()

print("\n************\n")

print("\n************\n")

# şimdi bar ile hata çubujlarını birlikte gösteren veri setini alalım
# önce iris veri setini yükleyelim
from sklearn.datasets import load_iris
iris=load_iris()

# iris veri setindeki değişkenlerin ortalamalarını ve standart sapmalarını bulalım
# sütunlar boyunca ortalama bulacağımız için axis=0 yazdık
ort=np.mean(iris.data,axis=0)
sd=np.std(iris.data,axis=0)
print(ort)
print(sd)

print("\n************\n")

# şimdi bir aralık değğişkeni alıp bu aralık değikenine de iris veri setinde 4 sayısal değişken olduüu için 4 değerini atadık
aralik=range(4)

# hata çubukları ile iki tane bar grafiği çizdireceğiz
# biri yatay diğeri dikey olsun
# bir düzlemde iki grafik olacaüı içim subplot ile belirtelim
# sublot(1 düzlem var, 2 grafik çizilecek, öncelikle 1. grafik alanına grafik çizilecek)
plt.subplot(1,2,1)

# ilk grafik alanına hata çubukları ile bar grafiği çizdirelim
# mavi renkte osun ve sd'nin hata grafiği çizileceğinden ve sd x ekseninde olduğundan xerr=sd yazılır
# barların konumu için align=center denir
# barları yatay çizmek için barh() kullanılır
plt.barh(aralik,ort,color="b",xerr=sd,alpha=0.7,align="center")

# şimdi grafiğe başlık ekleyelim
plt.title("Yatay Bar Grafiği")

# y eksenindeki etiketlere sayısal değerler yazdıralım
# etşketler iris veri setindeki değişkenlerin ismi olsun
plt.yticks(aralik,iris.feature_names)

# aynı komutları hata çubukları ile düşey barlar için yapalım:
# bir düzlemde iki grafik olacaüı içim subplot ile belirtelim
# sublot(1 düzlem var, 2 grafik çizilecek, öncelikle 2. grafik alanına grafik çizilecek)
plt.subplot(1,2,2)

# ilk grafik alanına hata çubukları ile bar grafiği çizdirelim
# mor renkte osun ve sd'nin hata grafiği çizileceğinden ve sd y ekseninde olduğundan yerr=sd yazılır
# barların konumu için align=center denir
# barları dikey çizmek için bar() kullanılır
plt.bar(aralik,ort,color="m",yerr=sd,alpha=0.7,align="center")

# şimdi grafiğe başlık ekleyelim
plt.title("Dikey Bar Grafiği")

# x eksenindeki etiketlere sayısal değerler yazdıralım
# etşketler iris veri setindeki değişkenlerin ismi olsun
plt.xticks(aralik,aralik)

plt.show()

print("\n************\n")

# barların genişliğini ayarlayabiliriz
# yatay bar grafikleri için heighy , dikey bar grafikleri için width kullanılır
# genişlikler öntanımlı olarak 0.8 ama biz bunakarı 0.5 yapalım
aralik=range(4)
plt.subplot(1,2,1)
plt.barh(aralik,ort,color="b",xerr=sd,height=0.5,alpha=0.7,align="center")
plt.title("Yatay Bar Grafiği")
plt.yticks(aralik,iris.feature_names)

plt.subplot(1,2,2)
plt.bar(aralik,ort,color="m",yerr=sd,width=0.5,alpha=0.7,align="center")
plt.title("Dikey Bar Grafiği")
plt.xticks(aralik,aralik)
plt.show()
