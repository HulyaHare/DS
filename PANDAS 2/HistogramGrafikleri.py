import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# grafipin stilini belirleyelim
plt.style.use("fivethirtyeight")

# normal dağılımdan bir veri seti oluşturalım
veri=np.random.randn(1000)

# histogram grafiğini çizelim
# histogramların kenar çizgilerini görelim ve rengi siyah olsun edgecolor="black"
plt.hist(veri,edgecolor="black")

# grafiğe başlık verelim
plt.title("Histogramlar")

# eksenleri isimlendirelim
plt.xlabel("Değerler")
plt.ylabel("Frekanslar")

plt.show()

print("\n************\n")

# dikdörtgenlerin sayısını bins ile kendimiz belirleyelim (bunu yapmazsak az önceki gibi otomatik bölünür)
plt.hist(veri,edgecolor="black",bins=10)
plt.title("Histogramlar")
plt.xlabel("Değerler")
plt.ylabel("Frekanslar")
plt.show()

print("\n************\n")

# bins argumanına dikdörtgenlerin herbirinin sınırını belirlendiği liste girelim
# yani dikgörtgen sayısı listenin uzunluğunun bir eksiği kadar olur çünkü:
# herbirinin genişliği sırasıyla bins listesindeki değerler olur şunun gibi:
# [-3,-2]  [-2,-1]  [-1,0]  [0,1]  [1,2]  [2,3]
bins=[-3,-2,-1,0,1,2,3]
plt.hist(veri,edgecolor="black",bins=bins)
plt.title("Histogramlar")
plt.xlabel("Değerler")
plt.ylabel("Frekanslar")
plt.show()

print("\n************\n")

# histogrwama verinin ortanca değerini gösteren bir çizgi ekleyelim ve rengi kırmızı olsun
ortanca=np.median(veri)
plt.axvline(ortanca,color="red")
bins=[-3,-2,-1,0,1,2,3]
plt.hist(veri,edgecolor="black",bins=bins)
plt.title("Histogramlar")
plt.xlabel("Değerler")
plt.ylabel("Frekanslar")
plt.show()

print("\n************\n")

# birkaç değişkenin histogramlarını karşılaştıralım
# x'lerin ilk argumanı ortalama, ikinci argumanı standart sapma, üçüncü argumanı gözlem sayısı olsun
x1=np.random.normal(0,0.8,1000)
x2=np.random.normal(-3,2,1000)
x3=np.random.normal(2,1,1000)
# şimdi bu değişlenlşerin historgram grafiklerini çizdirelim
# histogramın tipi stepfilled olsun ve yarım görünürlükte olsun
plt.hist(x1,histtype="stepfilled",alpha=0.5)
plt.hist(x2,histtype="stepfilled",alpha=0.5)
plt.hist(x3,histtype="stepfilled",alpha=0.5)
plt.show()

print("\n************\n")

print("\n************\n")

# İKİ BOYUTLU HİSTOGRAM ÇİZELİM
mean=[0,0]
cov=[[1,1],[1,2]] # kovaryans
x,y=np.random.multivariate_normal(mean,cov,1000).T
print(x)
print(y)
print()
# şimdi verinin iki boyutlu grafiğini görelim
plt.hist2d(x,y,bins=30,cmap="Reds")
cb=plt.colorbar()
cb.set_label("Dikdörtgenlerin Sayısı") # kırmızı rengin koyuluğu dikdörtgenlerin sayısını gösterir
plt.show()


print("\n************\n")

print("\n************\n")


film=pd.read_csv("imbdratings.txt")
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)  # Tüm DataFrame'i tek satırda gösterme
print(film.head())

print("\n************\n")

# veri setindeki duration sütununun histogramını görelim:

# grafiğin stilini ggplot yapalım
plt.style.use("ggplot")

# dikdörtgenlerin uzunlukları 17 ve 259 arasında 10'ar artacak şekilde olsun
bins=np.arange(70,250,10)
# x ekseninin etiketlerini bins değişkeni olsun
plt.xticks(bins)

# bar çizgileri siyah olsun
# barlaın rengi mor olsın
plt.hist(film.duration,edgecolor="black",color="m",bins=bins)

# grafiğin ismi imdbdeki filmlerin sürelerinin histogramları olsun
plt.title("imdbdeki filmlerin sürelerinin histogramları")

# x ekseninin adı Süreler olsın
# y ekseninin etiketi Frekanslar olsın
plt.xlabel("Süreler")
plt.ylabel("Frekanslar")

plt.show()
