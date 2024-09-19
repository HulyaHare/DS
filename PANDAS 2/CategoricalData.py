import pandas as pd
import numpy as np

# bir veriyi kategorik yapıya nasıl çevireceğimizi ve kategorik veriyi kullanmayuı öğrenicez
veri=pd.Series(["ali","efe","ali","ali"]*3)
print(veri)

print("\n*******\n")


# verideki unique değerleri görelim:
print(pd.unique(veri))

print("\n*******\n")

# verilerin tekrar sayılarını görelim
print(pd.value_counts(veri))

print("\n*******\n")

# bu değerlere sayısal deperler atayalım:
degerler=pd.Series([0,1,0,0]*3)
adlar=pd.Series(["ali","efe"])
print(adlar.take(degerler))
# işte böylece adları kategorik olarak temsil ettik
# yani ali'ye 0 değerini atadık ve efe'ye 1 değerini atadık

print("\n*******\n")

"""
 elemanları tamsayı olarak ifade etmeye kategorik temsil denir
 farklı değerlerin oluşturduğu diziye kategoriler ya da verinin seviyeleri denir
 kategorileri gösteren tamsayıya ise kategorik kodlar denir
"""

# pandasta veriler için özel kategorik kodlar vardır
print(veri)
print()
# verinin uzunluğunu N değişkenine atayalım:
N=len(veri)

df=pd.DataFrame({"isim":veri,
                 "no":np.arange(N),
                 "not":np.random.randint(40,100,size=N),
                 "kilo":np.random.uniform(50,70,size=N)},
                columns=["no","isim","not","kilo"])
print(df)

print("\n*******\n")

# isim sütununu ekrana yazdıralım:
print(df["isim"])
print()
# isim kategorisinin tipine bakalım
print(type(df["isim"]))

print("\n*******\n")

# şimdi isim sütununu kategorik yapıya çevirelim:
isim_kat=df["isim"].astype("category")
print(isim_kat)

print("\n*******\n")

# isim_kat verisindeki değerleri x değişkenine atayalım
x=isim_kat.values
# x değişkenindeki kategorileri görelim
print(x.categories)

print("\n*******\n")

# kategorik kodları görmek istersen şunu yap:
print(x.codes)

print("\n*******\n")

# direk dataframedeki sütunu direk kateoriye çevirmek:
df["isim"]=df["isim"].astype("category")
print(df.isim)

print("\n*******\n")

# direk olarak kategorik değişken oluşturmak:
veri_kat=pd.Categorical(list("abcde"))
print(veri_kat)

print("\n*******\n")

# istersek herhangi bir veriyi pandasın categorical metodu ile direk kategorik hale getirebiliriz
print(pd.Categorical(["muz","elma","kivi","muz","elma"]))

print("\n*******\n")

# istersek kategorik kodlaması verilen veriyi kategorik hale getirebiliriz
insanlar=["bebek","cocuk","genc","yasli"]
kodlar=[0,1,2,3,0,1,0,0]
# şimdi insanlar verisini kodlara göre kategorik hale getirelim
insan_kat=pd.Categorical.from_codes(kodlar,insanlar)
print(insan_kat)

print("\n*******\n")

# veriyi sıralı halde kategorilemek için ordered=True yapmalısım
insan_kat=pd.Categorical.from_codes(kodlar,insanlar,ordered=True)
print(insan_kat)

print("\n*******\n")

# sıralı olmayan kategorik veriyi as_ordered() ile sıralı hale getirmek
print(insan_kat.as_ordered())

print("\n*******\n")

# eğermverileri kategorik hale getirirsek groupby() kullanmak daha kolay olur
data=np.random.randn(1000)
# şimdi veriyi aralıklara bölelim
ara=pd.qcut(data,4)
print(ara)

print()

# ara değğişkeninin tipine bakalım (kategoriktir)
print(type(ara))

print("\n*******\n")

# bu aralıklara etiket atayalım
ara=pd.qcut(data,4,labels=["Q1","Q2","Q3","Q4"])
print(ara)

print("\n*******\n")

# etiketlenmiş aralık kategorilerinin uç değerlerini görmek istiyoruz
# grouby() ile bazı özet istatistikleiri hesaplayalım
# önce aralıkları series yapısına çevirelim
ara=pd.Series(ara,name="ceyrek")
# aralık satyısını, aralıkların min-max değerlerimi bulalım
print(pd.Series(data).groupby(ara).agg(["count","min","max"]).reset_index())

print("\n*******\n")

# şimdi kategorik tiiplerin performansını inceleyelim
"""
BÜTÜK VERİLERLE ÇALIŞIRKEN KATEGORİK YAPIDA ÇALIŞMAK PERFORMANSI ARTTIRIR
"""
N=10000000
say=pd.Series(np.random.randn(N))
etiket=pd.Series(["a","b","c","d"]*(N//4))
kat=etiket.astype("category")
# şimdi kategorik ve kategorik olmayan verinin bellek kullanımını inceleyelim

# önce kategorik olmayan etiket değişkeninin kullandıüı veriye bakalım (yani bellekte kapladığı alan)
print(etiket.memory_usage())

# şimdi kategorik hale getirilmiş verinim kullandığı belleğe bakalım
print(kat.memory_usage())

# görüldüğü gibi kategorik veri, kategorik olmayan veriye gmre daha az bellek kullanır


print("\n*******\n")

# şimdi kategorşk metorlara bakalım
s=pd.Series(["a","b","c","d"]*2)
s_kat=s.astype("category")
print(s_kat)

print("\n*******\n")

# cat niteliği kategorikal metotlara ulaşmamızı sağlar
# mesela verinin kod metodunu kullanalım
print(s_kat.cat.codes)
print()
# veya verinin kategori metodunu kullanalım
print(s_kat.cat.categories)

print("\n*******\n")

# kategorileri arttırmak içim set_categories kullan
yeni_kat=["a","b","c","d","e"]
print(s_kat.cat.set_categories(yeni_kat))

print("\n*******\n")

# kullanılmayan kategorşler şöyle kesilir: remove_unusued_categories()
s2_kat=s_kat[s_kat.isin(["a","b"])]
print(s2_kat)
# şimdi categories içinde olan ama s2_cat iöinde olmadığı için kullanılmayan kategorileri çıkartalım
print(s2_kat.cat.remove_unused_categories())

print("\n*******\n")

# dummy değişkeni oluşturma
# yani veriyi dönüştürüp dataframe haline getiricez
print(pd.get_dummies(s_kat))

print("\n*******\n")

