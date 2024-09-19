# veri setinin özet istatistiklerini bulmak
import pandas as pd
import numpy as np

df=pd.DataFrame([[2.4,np.nan],[6.3,-5.4],[np.nan,np.nan],[0.75,-1.3]],
                index=["a","b","c","d"],
                columns=["bir","iki"])
print(df)

print("\n************\n")

# sğtundaki sayıları toplamını sütun altına yazmak
print(df.sum())

print("\n************\n")

# satırların toplamını bulmak:
# axis=1 ya da axis=columns yazabilirsin
print(df.sum(axis=1))

print("\n************\n")

# satırların ortalamasını bulmak:
print(df.mean(axis=1))

print("\n************\n")

# ama görüldüğü gibi mean yazdığımızdqa eksik veriler dahil edilmedi
"""
 skipna=False olarak ayarlandığında, eksik değerler işlemeye dahil edilir ve bir NaN değeri varsa işlemin sonucu da NaN olur. 
 Aksi takdirde, skipna=True (varsayılan ayar) olarak ayarlanırsa, eksik değerler yoksayılır ve kalan değerler üzerinden işlem yapılır.
"""
print(df.mean(axis=1,skipna=False))
print(df.mean(axis=1,skipna=True))

print("\n************\n")

# sütunlardaki maximum değere sahip satır değerlerini yazdırmak
# yani mesela "bir" sütununa bakılır ve en yüksek değere sahip sütunun adı yani "b" ekrana yazılır
print(df.idxmax())
print()
# min değeri bulmak:
print(df.idxmin())

print("\n************\n")

# cumulative toplamı bulmak için cumsum() kullan:
print(df.cumsum())

print("\n************\n")

# veri setinin özet istatistiklerini elde etmek:
print(df.describe())

print("\n************\n")

# korelasyon katsayısını bulmak:

# Veri seti oluşturma
data = {
    "Canak_yaprak_boyu":[5.1,4.9,4.7,4.6,5.0],
    "Canak_yaprak_eni":[3.5,3.0,3.2,3.1,3.6],
    "Tac_yaprak_boyu":[1.4,1.4,1.3,1.5,1.4],
    "Tac_yaprak_eni":[0.2, 0.2, 0.4, 0.2, 0.6]
}
iris = pd.DataFrame(data)
# CSV dosyasına yazma
iris.to_csv('vgsalesGlobale.csv', index=False, encoding='utf-8')
# veri seti import edildi
iris=pd.read_csv("vgsalesGlobale.csv")
# DataFrame'i tamamen gösterme
# bu işlemi yapmazsak bir kısmına ... koyulmuş şekilde çıktı alırız yani bir kısmını göremeyiz
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)  # Tüm DataFrame'i tek satırda gösterme
print(iris)

print("\n************\n")

# iris verisindeki Tac_yaprak_boyu'nu kullanarak Tac_yaprak_eni2nin ikili kırelasyonunu bulmak
print(iris["Tac_yaprak_boyu"].corr(iris["Tac_yaprak_eni"]))

print("\n************\n")

# bütün değişkenlerin ikili korelasyonunu görmek
print(iris.corr())

print("\n************\n")

# bütün değişkenlerin ikili covariancelerini görmek:
print(iris.cov())

print("\n************\n")

# corrwit metodu ile bir değişken ve başka bir değişkenin ikili karşılaştırmalarını(correlation kastsayısını bılmak) elde etmek:
print(iris.corrwith(iris.Canak_yaprak_boyu))

print("\n************\n")

s=pd.Series(["b","b","b","b","c","c","a","a","a"])
print(s)

# veri setinde bir den fazla değer varsa ve bu değerleri tek görmek istersek unique() kullan
print(s.unique())

print("\n************\n")

# değerlerin sıklığını valuecount() ile görmek:
print(s.value_counts())

print("\n************\n")

# istediğimiz değerlerin her bir satırda olup olmadığını tek tek kontol etmek
print(s.isin(["b","c"]))
print()
# bu değerlerin bulunduğu satırları görmek:
print(s[s.isin(["b","c"])])