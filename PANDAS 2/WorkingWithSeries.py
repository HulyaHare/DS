

import pandas as pd


# Veri seti oluşturma
data = {
    'Year': [1983, 1983, 1983, 1990, 1995, 2000, 2005, 2005, 2005, 2015, 2016, 2017, 2017],
    'Game Name': ['Game1', 'Game2', 'Game3', 'Game4', 'Game5', 'Game6', 'Game7', 'Game8', 'Game9', 'Game10', 'Game11', 'Game12', 'Game13'],
    'Developer': ['Dev1', 'Dev2', 'Dev3', 'Dev4', 'Dev2', 'Dev6', 'Dev7', 'Dev8', 'Dev9', 'Dev10', 'Dev11', 'Dev12', 'Dev13'],
    'Publisher': ['Pub1', 'Pub2', 'Pub3', 'Pub2', 'Pub2', 'Pub6', 'Pub7', 'Pub8', 'Pub6', 'Pub10', 'Pub11', 'Pub12', 'Pub13'],
    'Platform': ['Platform1', 'Platform2', 'Platform3', 'Platform4', 'Platform5', 'Platform6', 'Platform7', 'Platform8', 'Platform9', 'Platform10', 'Platform11', 'Platform12', 'Platform13'],
    'Genre': ['Action', 'Action', 'Action', 'Action', 'Sports', 'Action', 'Fighting', 'RPG', 'Fighting', 'Simulation', 'Platformer', 'Music', 'Party'],
    'NA_Sales': [1.2, 2.3, 2.3, 4.0, 5.6, 2.2, 3.4, 4.5, 5.5, 2.1, 3.3, 4.4, 1.1],
    'EU_Sales': [0.9, 1.8, 2.7, 3.6, 4.4, 1.9, 2.6, 3.2, 4.3, 1.8, 2.5, 3.3, 1.0],
    'JP_Sales': [0.5, 1.2, 1.5, 2.0, 2.5, 0.9, 1.3, 1.9, 2.4, 0.8, 1.2, 1.6, 0.6],
    'Other_Sales': [0.2, 0.4, 0.6, 0.8, 1.0, 0.3, 0.4, 0.6, 0.7, 0.2, 0.4, 0.5, 0.3],
    'Global_Sales': [2.8, 2.8, 7.9, 10.4, 4.9, 10.4, 7.7, 10.4, 10.4, 4.9, 7.4, 9.8, 3.0],
    'Critic_Score': [85, 88, 91, 85, 87, 84, 89, 90, 92, 83, 86, 88, 80],
    'User_Score': [8.2, 8.5, 8.7, 8.3, 8.4, 8.1, 8.6, 8.8, 9.0, 8.0, 8.3, 8.5, 7.9],
    'Rating': ['E', 'T', 'M', 'E', 'E', 'T', 'M', 'E', 'E', 'T', 'M', 'E', 'E']
}

oyunlar = pd.DataFrame(data)

# CSV dosyasına yazma
oyunlar.to_csv('vgsalesGlobale.csv', index=False, encoding='utf-8')

# veri seti import edildi
oyunlar=pd.read_csv("vgsalesGlobale.csv")

# DataFrame'i tamamen gösterme
# bu işlemi yapmazsak bir kısmına ... koyulmuş şekilde çıktı alırız yani bir kısmını göremeyiz
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)  # Tüm DataFrame'i tek satırda gösterme


print(oyunlar)

print("\n*************\n")

#veri setinin ilk beş satırını gösterir
print(oyunlar.head())

print("\n*************\n")

# veri setindeki değişkenlkerin veri tipini verir
print(oyunlar.dtypes)

print("\n*************\n")

# oyunlar veri setindeki Genre değişkeninin tanımsal değerlerini verir
print(oyunlar.Genre.describe())

print("\n*************\n")

# Genre değişkeni içerisindeki değerler ve o değerlerin sayısını verir
print(oyunlar.Genre.value_counts())

print("\n*************\n")

# her bir değerin yüzdesini görmek:
print(oyunlar.Genre.value_counts(normalize=True))

print("\n*************\n")

# objenin veri tipini görmek:
print(type(oyunlar.Genre.value_counts()))

print("\n*************\n")

# ilk beş değeri görmek
print(oyunlar.Genre.value_counts().head())

print("\n*************\n")

# tekrar eden değerleri tek olarak görmek
print(oyunlar.Genre.unique())

print("\n*************\n")

# tekrar etmeyen toplam kaç tür olduğunu görmek
print(oyunlar.Genre.nunique())

print("\n*************\n")

# iki değişkenin karşılıklı değerlerinin kaç tane olduğunu tablo olarak görmek:
print(pd.crosstab(oyunlar.Genre, oyunlar.Year))

print("\n*************\n")

# değişkenin tanımsal istatistiklerini görmek: (sayısı, ortalaması, standast sapması gibi değerler)
print(oyunlar.Global_Sales.describe())

print("\n*************\n")

# bu sayısal değişkenin direk ortalamasını almak
print(oyunlar.Global_Sales.mean())

print("\n*************\n")

# bu sayısal değişkenin kaçar tane olduklarıdır
print(oyunlar.Global_Sales.value_counts())

print("\n*************\n")
print("\n*************\n")


# series veri tipini görselleştirmek:
# grafiği direk görebiliriz
oyunlar.Year.plot(kind="hist")
import matplotlib.pyplot as plt
plt.show()

print("\n*************\n")

# genre'nin sayısal değerlerinin bar grafiği:
oyunlar.Genre.value_counts().plot(kind="bar")
plt.show()