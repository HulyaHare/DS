"""
bu derste şunlar öğrenilecek
çizgi grafiği çizme
renk ve stil ayarları
eksen ayarları
çizgilerin altını doldurma
grafik stilleri
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# style metodu ile grafiğin görünüşünü ayarlayabiliriz
print(plt.style.available)
plt.style.use('seaborn-v0_8-whitegrid')

print("\n*******\n")

# grafik için öncelikle bir grafik nesnesi ve bir grafik alanı oluştrurulur
fig=plt.figure()
ax=plt.axes()
# daha çizmediğimiz için grafik şuan boş

# şimdi x ekseni için 0-10 arasında eşit aralıklı 100 değer alalım
x=np.linspace(0,10,100)
# şimdi de y eksemi için değer oluşturalım
y=np.sin(x)
# şimdi grafiği oluşturalım
ax.plot(x,y)
plt.show()

print("\n*******\n")

# eğer bir grafikte birden fazla çizgi grafiği görmek istersek plt.plıt birden fazla kez yazılır
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.show()

print("\n*******\n")

# istersek çizgi grafiklerinin renklerini ve stillerini komrtol edebiliriz
plt.plot(x,np.sin(x-1),color="blue") # renk adı girildi
plt.plot(x,np.sin(x-2),color="r") # renk isminin kısaltılmış hali girildi red'in r'ai
plt.plot(x,np.sin(x-3),color="0.75") # grafiğin grilik değerini girdik
plt.plot(x,np.sin(x-4),color="#000000") # hex kodunu girdik
plt.show()
# eğer kendiöiz renkkler, girmeseydik otomatik olarak farklı renkler verilirdi

print("\n*******\n")

# çizgi stili için linestile kullanılır
plt.plot(x,x+1,linestyle="solid")
plt.plot(x,x+2,linestyle="dashed") # kesik çizgi
plt.plot(x,x+3,linestyle="dashdot") # kesik çizgi ve nokta
plt.plot(x,x+4,linestyle="dotted") # nokta olarak gösterir
plt.show()

print("\n*******\n")

# kelimeler yerine semboller de kullanılabilir
plt.plot(x,x+1,linestyle="-")
plt.plot(x,x+2,linestyle="--") # kesik çizgi
plt.plot(x,x+3,linestyle="-.") # kesik çizgi ve nokta
plt.plot(x,x+4,linestyle=":") # nokta olarak gösterir
plt.show()

print("\n*******\n")

# hem renk hem de çizgi stillerini aynı anda girelim
plt.plot(x,x+1,"-r")
plt.plot(x,x+2,"--b")
plt.plot(x,x+3,"-.g")
plt.plot(x,x+4,":k") # mesela burda kesik çizgili siyah olur çünkü k siyah oluyo
plt.show()

print("\n*******\n")

# eksenlerin aralıklarını belirleyelim
plt.plot(x,np.sin(x))
plt.xlim(-5,20) # x ekseni -5'den 20'ye kadar olsun
plt.ylim(-3,3) # y ekseni -3'den 3'e kadar olsun
plt.show()

print("\n*******\n")

# eksenlerden birini ters çevirelim:
# mesela y ekseninin değerlerini ters çevirelim
plt.plot(x,np.sin(x))
plt.xlim(-5,20) # x ekseni -5'den 20'ye kadar olsun
plt.ylim(3,-3) # y ekseni -3'den 3'e kadar olsun
plt.show()

print("\n*******\n")

# axis matodu ile de x ve y eksenleri için sınır girebiliriz
plt.plot(x,np.sin(x))
# axis([x ekseni için değerler, y ekseni için değerler])
plt.axis([-5,10,-3,3])
plt.show()

print("\n*******\n")

# axis metodunun tight gibi otomatik ayarlara izin veren opsiyonlaru vardır
# yani grafiği değerlere göre otomatik ayarlar
plt.plot(x,np.sin(x))
# axis([x ekseni için değerler, y ekseni için değerler])
plt.axis("tight")
plt.show()

print("\n*******\n")

print("\n*******\n")

# şimdi grafiğe etiket vermeyi öprenelim
# grafiğe title() ile başlık verelim
# eksenleri de xlabel() ylabel() ile izimlendirelim
plt.plot(x,np.sin(x))
plt.title("Bir sinüs eğrisi")
plt.xlabel("x değerleri")
plt.ylabel("sin(x) değerleri")
plt.show()

print("\n*******\n")

# bir grafikte birden fazla çizgi grafiği varsa, çizgilerin isimlerini gösteren levha şeklinde legend kullanılır
# kendimiz isimlendirmek istersek label kullanılırız
plt.plot(x,x+2,"-r",label="hülya")
plt.plot(x,x+4,":b",label="hare")
plt.legend() # çizgilerin isimlerini göstermeyi sağlar
plt.show()

print("\n*******\n")

print("\n*******\n")

# şimdi çizgi grafiklerinin alt bölgelerini dolduralım
yas=[25,26,27,28,29,30,31,32,33,34,35] # prohramcıların
maas=[38496,42000,46752,49320,53200,56000,62316,64938,67317,68748,73753] # genel yazılımcıların maaşların ortalama maaşları
py_maas=[45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640] # python geliştiricilerin ortalama maaşları
# şimdi yaşlara göre genel ve python prohrm gelişriricilerin maaşlarını görelim
# marker yaparak her kesişime nokta koyduk
plt.plot(yas,maas,"-r",marker=".")
plt.plot(yas,py_maas,"--b",marker=".")
plt.show()

print("\n*******\n")

# bu çizgilere legend ekleyelim yani isimlerini tabloya yazdıralım
plt.plot(yas,maas,"-r",marker=".")
plt.plot(yas,py_maas,"--b",marker=".")
plt.legend(["Bütün Geliştiriciler","Python Geliştiriciler"])
plt.show()

print("\n*******\n")

# şimdi fill_between ile grafiğin altını dolduralım
# ilk değer x'in değerlerini, ikincisine altı doldurulşacak çizgi grafiğinin ismi girilir
# alpha ile de dldurulacak alanın görünürlüğü girilir
plt.plot(yas,maas,"-r",marker=".")
plt.plot(yas,py_maas,"--b",marker=".")
plt.legend(["Bütün Geliştiriciler","Python Geliştiriciler"])
plt.fill_between(yas,py_maas,alpha=0.40)
plt.show()
# böylece python geliştiricilerinin maaşlarının gösterildği çizgi grafiğinin altı boyanmış oldu

print("\n*******\n")

#doldurulacak alan için y ekseninden belitli bir değer seçilebilir
plt.plot(yas,maas,"-r",marker=".")
plt.plot(yas,py_maas,"--b",marker=".")
plt.legend(["Bütün Geliştiriciler","Python Geliştiriciler"])
ortanca_maas=57287
plt.fill_between(yas,py_maas,ortanca_maas,alpha=0.40)
plt.show()

print("\n*******\n")

print("\n*******\n")

# ŞİMDİ GRAFİK STİLLERİNİ BELİRLEYELİM

# şimdiyre kadar grafik zemini olaraqk çizgili zemin kullandık. Bu zemini değiştirelim
# kullanabileceğimiz grafik stilerini görmek için style.available diyelim
# mesela fivethirtyeight stilini kullanalım
print(plt.style.available)
plt.style.use("fivethirtyeight")
plt.plot(yas,maas,"-r",marker=".")
plt.plot(yas,py_maas,"--b",marker=".")
plt.legend(["Bütün Geliştiriciler","Python Geliştiriciler"])
ortanca_maas=57287
plt.fill_between(yas,py_maas,ortanca_maas,alpha=0.40)
plt.show()

print("\n*******\n")

# ayrıca grafik stili olarak xkc metodu da kullanılabilir
plt.xkcd() # karalama tarzı grafik gösteirr
plt.plot(yas,maas,"-r",marker=".")
plt.plot(yas,py_maas,"--b",marker=".")
plt.legend(["Bütün Geliştiriciler","Python Geliştiriciler"])
ortanca_maas=57287
plt.fill_between(yas,py_maas,ortanca_maas,alpha=0.40)
plt.show()
