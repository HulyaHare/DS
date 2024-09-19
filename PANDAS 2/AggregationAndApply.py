#aggregate ile hem kendi yazdığımız fonksiyonları hem de groupby('ın kkendi fonksiyonlarını kullanabiliriz
import pandas as pd
import numpy as np
vs=pd.DataFrame({"anahtar":list("ABC")*2,
                 "veri1":range(6),
                 "veri2":np.arange(5,11)})
print(vs)

print("\n************\n")

# "AGGREGATE" YERİNE KISALTIP "AGG" YAZABİLİRSİN AYNI ŞEY

# vs veri setini anahtar sütuna göre gruplamdıralım
grup=vs.groupby("anahtar")

# gruplanmış veri setine agregate metodunu kullanarak bazı fonksiyonları uygulayalım
print(grup.aggregate(["min",np.median,"max"]))

print("\n************\n")

# sözlük yapısını kullanarak herbir sütun için farklı fonksiyon kullanabilir
# mesela veri1 için min değerlerini, veri2 için max değerlerini bulalım
print(grup.agg({"veri1":"min","veri2":"max"}))

print("\n************\n")

# kendi yazdığımız fonksiyonu da gruplara ayrılmış veri seti üstünde çalıştırabiliriz
# önce bir fonksiyon yazalım:
def f(x):
    return x.max()-x.min()
# bu fonksiyonu gruplanmış veriye uygulauyalım
print(grup.agg(f))

print("\n************\n")

print("\n************\n")

# hiyererşik indexlere sahip veri setlerinde birden fazla fonksiyon uygulamak
veri=pd.DataFrame({"harf":list("ABC")*4,
                   "sayi":["bir","iki"]*6,
                   "v1":np.random.randn(12),
                   "v2":np.arange(10,33,2)})
print(veri)

print("\n************\n")

# önce harf ve sayı sütunşarına göre gruplayalım
grup=veri.groupby(["harf","sayi"])
grup_v1=grup["v1"]

# bu grup_1 değişkeninin ortalamalrını bulalım
print(grup_v1.agg("mean"))

print("\n************\n")

# bir veriye birden fazla fonksiyon da uygulayabiliriz
# bunun için fonksiyonları liste içinde yazmamız lazım
print(grup_v1.agg(["mean","std",f]))

print("\n************\n")

# sütunlara isim vermek şöyle olur:
# tupla yapısı içinde sütun ismi ve fonksiyon yazarak işlemleri gerçekleştirebiliriz
print(grup_v1.agg([("falan","mean"),("filan",np.std)]))

print("\n************\n")

# birden fazla sütun içinde fonksiyonlar uygulanabilir
# önce uygulanacak fonksiyonları fonk değişkenine atayalım
fonk=["mean","count","max"]
# şimdi de gruplanmış nesneleri sütunlara göre düzenleyelim
sonuc=grup[["v1","v2"]].agg(fonk)
print(sonuc)

print("\n************\n")

# istersek sadece istediğimiz sütunnun sonuçlarını görebiliriz
print(sonuc["v1"])

print("\n************\n")

# sütunlara ayrı ayrı fonksiyonlar da uygulanabilir
print(grup.agg({"v1":["count","max","mean"],
                "v2":"sum"}))

print("\n************\n")

# eğer indexlerin hiyeranşikal olmasını İSTEMEZSEK:
print(veri.groupby(["harf","sayi"],as_index=False).mean())

print("\n************\n")

# apply metodu parçalara ayrılmış grupların her birinin herhangi bir fonksiyona uygulamak için kullanılır:
# veri setini harf sütununa göre gruplandıralım
grup=veri.groupby("harf")

# gruptaki herbir kategori için v2'nin özet istatistiklerini görmek
print(grup["v2"].apply(lambda x:x.describe()))

print("\n************\n")

# A ve B sınıfındaki öğrencilerin matematik puanlarınmı gösteren bir veri seti oluşturalım
mat=pd.DataFrame({"sinif":list("AB")*3,
                  "ogr":["ali","efe","nur","eda","ata","can"],
                  "puan":[60,70,np.nan,55,np.nan,80]})
print(mat)
# şimdi sımıflara göre grupları oluşturalım:
grup=mat.groupby("sinif")
print(grup)

print("\n************\n")

# grupların puan ortalamasını ekrana yazdırmak
print(grup.mean(numeric_only=True))

print("\n************\n")

# eksik verileri ortalama ile dolduracak fonksitoyn yazalım
fonk=lambda f:f.fillna(f.mean())
print(grup.apply(fonk))

print("\n************\n")

# isstersek başlangıçta belirlenen değeleri eksik verilerin yerine atayabiliriz.
# mesela A kategorisindeki eksik değerşer yerine 100, B kategorisindeki eksik değerler yerine 50 atayalım
deger={"A":100,"B":50}
fonk2=lambda f:f.fillna(deger[f.name])
# şimdi de bu fonksiyonu apply ile gruplanmış veri üstüme uygulayalım:
print(grup.apply(fonk2))