# SEABORN İSTATİSTİKSEL GRAFİK ÇİZDİRMEYE YARAR


# burada seaboonrdaki pengurinsi kullanmak için sertifikaları atlama işlemi yapıyoruz
import ssl
import urllib.request

import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context
# bölyece hata almayız


import seaborn as sns
import pandas as pd

# penguen veri setini yükleyelim
data=sns.load_dataset("penguins")
pd.set_option('display.max_rows', None)  # Satır sayısını sınırsız yapar
pd.set_option('display.max_columns', None)  # Sütun sayısını sınırsız yapar

# ilk beş penguen satırını görelim
print(data[:5])

print("\n*******\n")

# veri setinin yapısını görelim
print(data.shape) # 344 satır ve 7 sğtun var

print("\n*******\n")

# seabornda grafik çizerken kullanabileceğiniz temalar vardır
# öntanımlı bir tema seçelim
sns.set_theme()

# grafiğin görüntü kalitesini ayarlayalım
# bu sözlük tipinde olmalıdır
sns.set(rc={"figure.dpi":300})

# şimdi çizdireceğimiz grafiklerin bpyutunu ayalrayalım
sns.set(rc={"figure.figsize":(6,3)})

# şimdi penguenlerin türlerine(species) göre bill_length_mm  ve bill_depth_mm göre saçılım grafiklerini görelim
# x ekseni için bill_length_mm  ve  y ekseni için bill_depth_mm kullanılacaktır
# veri setinin ismi data parametresinde yazılır
# neye göre renklendirme yapacağımız hue ile belli edilir mesela speciese göre yapacağız burda
# hue neye göre olacağını belirler
sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",
                data=data,hue="species")
plt.show()

print("\n*******\n")

# şimdi histogram çizelim
# histplot() ile flipper_length_mm'in histogramını görelim
sns.histplot(x="flipper_length_mm",data=data)
plt.show()

print("\n*******\n")

# şimdi görmek istediğimiz değişkeni y eksenine yazarak grafiği yan çevireliö
sns.histplot(y="flipper_length_mm",data=data)
plt.show()

print("\n*******\n")

# histogramdaki dikdörtgenlerin genişliğini binwidth ile düzenleyelim
sns.histplot(x="flipper_length_mm",data=data,binwidth=3)
plt.show()

print("\n*******\n")

# şimdi histogram grafiğine olasılık dağılım eğrisini ifade eden kde parametresini ekleyekim
sns.histplot(x="flipper_length_mm",data=data,binwidth=3,kde=True)
plt.show()

print("\n*******\n")

# değişkenlerin kategorilerine(species) göre histogramlarını görmek için hue=species
sns.histplot(x="flipper_length_mm",data=data,binwidth=3,kde=True,hue="species")
plt.show()

print("\n*******\n")

print("\n*******\n")

# şimdi species'lerşn fllipper_length_mm'sini gösteren bar grfaipini çizelim
sns.barplot(x="species",y="flipper_length_mm",data=data)
plt.show()

print("\n*******\n")

# öntanımlı olarak barlar dğeerlerin ortalamasına göre hesaplanır
# bunu hue parametresini kullanarak değiştirebilirz
# ama biz barları türlerin çinsiyetine göre  fllipper_length_mm'sini gösrelim
sns.barplot(x="species",y="flipper_length_mm",data=data,hue="sex")
plt.show()

print("\n*******\n")

print("\n*******\n")

# kutu grafiği kategorik bir değişkeni seviyerler arsında sayısal verilerin dağılımını karşılaştormak için kullanılır
# türelere göre flipper_length_mm'in dağılımının kutu grafiğini görelim
sns.boxplot(x="species",y="flipper_length_mm",data=data)
plt.show()

print("\n*******\n")

# türlerin cinsiyete göre flipper_length_mm'in dağılımının kutu grafiğini görelim
sns.boxplot(x="species",y="flipper_length_mm",data=data,hue="sex")
plt.show()

print("\n*******\n")

# violin grafiği kategorik değişkenler arasındaki sayısal değerlerin dağılımını karşılaştırır
# türelere göre flipper_length_mm'in dağılımının violin grafiğini görelim
sns.violinplot(x="species",y="flipper_length_mm",data=data)
plt.show()

print("\n*******\n")

# türlerin cinsiyete göre flipper_length_mm'in dağılımının violin grafiğini görelim
sns.violinplot(x="species",y="flipper_length_mm",data=data,hue="sex")
plt.show()

print("\n*******\n")

print("\n*******\n")

# şimdi aynı grafikte farklı ddeğişkenlkerin grafiklerini çizdirelim
# island değişkeninin 3 ve sex değişkeninin 2 kategorisi olduğundan 6 bölme oluşur
sns.FacetGrid(data,col="island",row="sex")
plt.show()

print("\n*******\n")

# island ve sex değişkenlerine göre pengueknlerin flipper_length_mm'sinin histogram grafiğini görelim
sns.FacetGrid(data,col="island",row="sex").map(sns.histplot,"flipper_length_mm")
plt.show()

print("\n*******\n")

# bölmelre palet genişliklerinin dağılım grafiğini çizdirelim
sns.FacetGrid(data,col="island",row="sex").map(sns.displot,"flipper_length_mm")
plt.show()

print("\n*******\n")

print("\n*******\n")

# değişkenlerin ikili ilişkilerini görmek için pair grsafiğini kullanalım
# bu fonksiyon veri listesindeki herbir sayısal değişkenin karşılıklı grafiklerini oluş-şturur
# şimdi penguen türlerine göre herbirinin karşılıklı saçılım grafiklerini kontol edelim
# yani aynı grafikte heosini çizdiricez
# uzunluğu 3 olsın
sns.pairplot(data,hue="species",height=3)
plt.show()

print("\n*******\n")

# köşe ekseninde histogramların olması için diad_kind parametresi kullanılır
sns.pairplot(data,hue="species",height=3,diag_kind="hist")
plt.show()

print("\n*******\n")

# şimdi sayısal değişkenler arasındaki korelasyonu görmek için heatmap() kullanalım
sns.heatmap(data.corr())
plt.show()

print("\n*******\n")

# herbir hücredki sayısal korelasyon değerini görmek içim annt=true yaz
sns.heatmap(data.corr(),annot=True)
plt.show()
