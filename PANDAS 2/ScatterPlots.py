import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# iki değişken arasındaki ilişkiyi görmek için saçılım grafikleri kullanılır
# gözlem değerleri noktalar ile gösterilir

# stili seçelim
plt.style.use('seaborn-v0_8-whitegrid')
iris=pd.read_csv("iris.txt")
print(iris.head())

print("\n*******\n")

# şimdi saçılım grafiğini çidirelim
# önce grafşk nesnesi ve gradik alanı oluşturalım
fig=plt.figure() # grafik nesnesi
ax=plt.axes() # grafik alanı
# şindi sepal boy ve sepal enin saçılım grafiklerini çizdirelim
# noktaların şeklini artı yapalım (üçgen yapmak istesetdik v yazardık)
plt.plot(iris.sepal_boy,iris.sepal_en,"+")
plt.show()

print("\n*******\n")

# noktaların rengini kırmızı yapalım şeklini üçgem yapalım
# kırmızı için r yazılır üçgen için v yazılır yani rv olur
plt.plot(iris.sepal_boy,iris.sepal_en,"rv")
plt.show()

print("\n*******\n")

# noktaların(üçgenlerin) boyutunu değiştirelim bunun için markesize kullanalım
plt.plot(iris.sepal_boy,iris.sepal_en,"rv",markersize=20)
plt.show()

print("\n*******\n")

# saçılım grafiğini scatter metodu ile de çizdirebiliriz
# sepal en ve petal enin saçılım grafiğini çizdirelim
# noktaların boyutunu s argumanıyla ayarlayabiliriz
# noktaların rengi için c argumanı kullanılır mesela mor için "m" yazılır
# noktaların şekli için marker kullanılır mesela marker="v" olursa üçgen olur
# noktaların dış çizgileriniin rengini edgecolor ile yapabiliriz mesela edgecolor="black" diğererk dış çizgilerini siyah yapabiliriz
# noktaların dış çicgilerinin kalınlığı için linewidth kullanılır
# alpha argumanı noktaların görünürlüğünü ayarlar
plt.scatter(iris.sepal_en,iris.petal_en,
            s=75, # noktanın boyutu
            c="m", # noktanın rengi
            marker="v", # noktanın şekli
            edgecolors="black", # noktanın dış çizgisimim rengi
            linewidths=1, # noktanın dış çizgisimim kalınlığı
            alpha=0.75) # noktanın saydamlığı
plt.show()

print("\n*******\n")

# şimdi noktaların griliğini belirleyelim (alpha ile de görünürlüğünü arttıralım
# 0 ile 10 arasında 150 tane sayı oluşturalm
renk=np.random.randint(0,10,len(iris))
plt.scatter(iris.sepal_en,iris.petal_en,s=100,c=renk,alpha=1)
plt.show()

print("\n*******\n")

# yine noktaların griliğini aynı yolla ayarlayacaüız ama bu sefer kırmızı olcaklar yani kırmızının farklı tonları olacaklar
# bu cmaps ile yapılır ve rengin ilk harfi büyük olur ve çoğul olur aynı Reds gibi
renk=np.random.randint(0,10,len(iris))
plt.scatter(iris.sepal_en,iris.petal_en,s=100,c=renk,cmap="Reds",alpha=1)
# cmap="viridis" yazarsak noktalar daha canlı renkler olurlar
plt.show()

print("\n*******\n")

# grafiğe sayı değerlerini renkşer ile gösteren çubuk grafiği ekleyebiliriz
renk=np.random.randint(0,10,len(iris))
plt.scatter(iris.sepal_en,iris.petal_en,s=100,c=renk,cmap="viridis",alpha=1)
cbar=plt.colorbar()
cbar.set_label("Seviyeler") # renk barını isimlendirdik
plt.show()

print("\n*******\n")

# noktaların bpyutlarını da farklı yapabilriiz bunun için s değişkenini boyutlar listesine eşitleyeceğiz
# böylece farklı boyutlarda noktalar oluşacak
renk=np.random.randint(0,10,len(iris))
boyutlar=np.random.randint(50,500,len(iris))
plt.scatter(iris.sepal_en,iris.petal_en,s=boyutlar,c=renk,cmap="viridis",alpha=1)
cbar=plt.colorbar()
cbar.set_label("Seviyeler")
plt.show()

print("\n*******\n")

renk=np.random.randint(0,10,len(iris))
boyutlar=np.random.randint(50,500,len(iris))
plt.scatter(iris.sepal_en,iris.petal_en,s=boyutlar,c=renk,cmap="viridis",alpha=1)
cbar=plt.colorbar()
cbar.set_label("Seviyeler")
# eksenleri isimlendirelim ve grafiğe başlık verelim
plt.xlabel("Sepal En")
plt.ylabel("Petal En")
plt.title("İris Çiçeği Sepan En Petal En Saçılım Grafiği")
plt.show()

print("\n*******\n")

# grafiğin stilini tekrar değiştirelim
print(plt.style.available)
# grafiğin stili 'fivethirtyeight' olsun:
plt.style.use('fivethirtyeight')
# ayrıca grafiğin şeklini değiştirelim mesşea karalama tarzı olsun:
plt.xkcd()
renk=np.random.randint(0,10,len(iris))
boyutlar=np.random.randint(50,500,len(iris))
plt.scatter(iris.sepal_en,iris.petal_en,s=boyutlar,c=renk,cmap="viridis",alpha=1)
cbar=plt.colorbar()
cbar.set_label("Seviyeler")
# eksenleri isimlendirelim ve grafiğe başlık verelim
plt.xlabel("Sepal En")
plt.ylabel("Petal En")
plt.title("İris Çiçeği Sepan En Petal En Saçılım Grafiği")
plt.show()