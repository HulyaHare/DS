# sıralama yapmak
import pandas as pd
import numpy as np

# SERIES veri yapısı üzerinde sıralama yapmak

s=pd.Series(range(5),index=["e","d","a","b","c"])
print(s)

print("\n************\n")

# indexlerine göre sıralayalım
print(s.sort_index())
print()
# value'lerinde göre sıralama yapmak
print(s.sort_values())

print("\n************\n")

# DATAFRAME yapısındaki veri setini sıralamak
df=pd.DataFrame(np.arange(12).reshape(3,4),
             index=["bir","iki","uc"],
             columns=["d","a","b","c"])
print(df)

print("\n************\n")

print(df.sort_index())
print()
print(df.sort_index(axis=1))

print("\n************\n")

# sıralamayı azalan şekilde yapmak
print(df.sort_index(axis=1,ascending=False))

print("\n************\n")

# value'lere göre sıralama yapmak:
s2=pd.Series([5,np.nan,3,-1,9])
print(s2)
print()
print(s2.sort_values()) # nan olan veri en sonda olur

print("\n************\n")

df2=pd.DataFrame({"a":[5,3,-1,9],"b":[1,-2,1,5]})
print(df2)

print("\n************\n")

# b sürunundaki değerlere göre veri setini sıralayalım
print(df2.sort_values(by="b"))

print("\n************\n")

# birden fazla sütun için sıralama yapmak
# burada önce b sütununa göre sıralar sonra kalanları(eşit olanları) a sütununa göre sıralar
print(df2.sort_values(by=["b","a"]))

print("\n************\n")

# veri setini içeri aktarma:
veri=pd.read_csv("vgsalesGlobale.csv")
# DataFrame'i tamamen gösterme:
# bu işlemi yapmazsak bir kısmına ... koyulmuş şekilde çıktı alırız yani bir kısmını göremeyiz
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
pd.set_option('display.expand_frame_repr', False)  # Tüm DataFrame'i tek satırda gösterme
# head() ile veri setinin ilk 5 değerini görmek
print(veri.head())

print("\n************\n")

# veri setinin Genre sütununu alfabetik sırada sıralayalım
print(veri.Genre.sort_values())
print()
print(veri["Genre"].sort_values()) # eğer iki kelimelikse mesela "Game Name" sğtununu falan sıralamaya çalışıyorsan bu yazım şeklini kullan
# üstte ekrana çıktısı verilen tüm değerlerin type'si Series veri tipidir

print("\n************\n")

# sıralamayı azalan şekilde yapmak:
print(veri["Game Name"].sort_values(ascending=False))

print("\n************\n")

# sütuna göre sıralama yapmak:
print(veri.sort_values("Year"))

print("\n************\n")

# birden çok sütun içim sıralama yapmak içim [] kullanılır
# burada önce Year'a göre sıralanır sonra kalanlar(Yearları eşit olanlar) Genre sütununa göre sıralanır
print(veri.sort_values(["Year","Genre"]))