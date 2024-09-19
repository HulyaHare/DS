import numpy as np
import matplotlib.pyplot as plt

veri=np.arange(10)
plt.plot(veri)
plt.show()

print("\n*******\n")

plt.plot(veri)
# grafiğe başlık ekleyelim
plt.title("falan")
# grafiğin x eksenini isimlendirelim
plt.xlabel("filan")
plt.show()

print("\n*******\n")

# y değerine karşı x değerinin grafiğini çizelim
x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y)
plt.show()

print("\n*******\n")

# grafiği çizgi tipini ve rengini gösterelim
# öntanımlu olarak rengi mavi, tipi çizgidir
# mesela kırmızı renkte ve nokta nokta çizelim
# kırmızı için r harfi, nokta için o harfi kullanılır
plt.plot(x,y,"ro")
plt.show()

print("\n*******\n")

# listeler ile çalışalım
d=np.arange(0.,5.,0.2)
print(d)
# d ve d grafiğini görelim. rengi kırmızı ve şekli -- olsun
# aynı grafikte d ve d'nin karesinin grafiğini de görelim. rengi blue ve şekli square yani kare olsun
# aynı grafikte d ve d küp grafipini görelim rengi yeşil(greeen), şekli üçgen(tringle yani ^) olsun
plt.plot(d,d,"r--",d,d**2,"bs",d,d**3,"g^")
plt.show()

print("\n*******\n")

# grafiği savefig() ile bilgisayara kayddederiz
#m- mesela png formatında kaydedelim
d=np.arange(0.,5.,0.2)
plt.plot(d,d,"r--",d,d**2,"bs",d,d**3,"g^")
plt.savefig("grafigim1.png") # pdf formatında kaydetömek istedseydik .pdf yazardık

print("\n*******\n")

# dpi çözünürlüğü ayarlar
# bbox_inches grafiğin çevresindeki beyaz alanı kesmemizi sağlar yani tüm ekran sadece grafikle dolar
d=np.arange(0.,5.,0.2)
plt.plot(d,d,"r--",d,d**2,"bs",d,d**3,"g^")
plt.savefig("grafigim2.png",dpi=500,bbox_inches="tight") # pdf formatında kaydetömek istedseydik .pdf yazardık
