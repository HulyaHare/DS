# Series tipindeki değerler toplanırken, aynı ,ndex değerleri birbiriyle toplanır
# eğer indexler eşleşmezse eksik veri olur

import pandas as pd
import numpy as np

s1=pd.Series(np.arange(4),index=["a","c","d","e"])
s2=pd.Series(np.arange(5),index=["a","c","e","f","g"])

print(s1)
print()
print(s2)

print("\n************\n")

# karşılıklı index değerleri eşlesen değerler toplanır, eşleşmeyenler NaN olur
print(s1+s2)

print("\n************\n")

# aynı durum DataFrame için de geçerlidir
df1=pd.DataFrame(np.arange(6).reshape(2,3),
                 columns=list("ABC"),
                 index=["ali","efe"])
df2=pd.DataFrame(np.arange(9).reshape(3,3),
                 columns=list("ACD"),
                 index=["ali","can","efe"])
print(df1)
print()
print(df2)

print("\n************\n")

# index değerleri uyuşanlar toplanır kalanlar NaN
print(df1+df2) # bunun yerinde şu da olur: df1.add(df2)

print("\n************\n")

# NaN çıkan değerlere istediğimiz değeri atayabiliriz mesela 0 atayalım
print(df1.add(df2,fill_value=0))

print("\n************\n")

# değerlerin çarpmaya göre tersi alınmış halini göster
print(1/df1)

print("\n************\n")

# çıkarma için sub, bölme işlemi için div, çarpma işlemi için mul, üs alma işlemi için pow
print(df1*3)
print(df1.mul(3))

print("\n************\n")

# satırlar ile ilgili işlem yapmak
s=df2.iloc[1]
print(df2)
print(s)

print("\n************\n")

"""
[0,0]-[0,0]  [0,1]-[1,0]  [0,2]-[2,0]
[1,0]-[0,0]  [1,1]-[1,0]  [1,2]-[2,0]
[2,0]-[0,0]  [2,1]-[2,0]  [2,2]-[2,0]

0-3  1-4  2-5
3-3  4-4  5-5
6-3  7-4  8-5
"""
# böylece df2'nin satırlarından s'in satırları çıkartılmış oldu
print(df2-s)

print("\n************\n")

# sütunlar ile ilgili işlem yapmak
s2=df2["A"]
print(df2)
print(s2)

print("\n************\n")

# sütun ile işlem yapmak için axis değeri index!e eşitlenir
# böylece df2'nin sütunlarundan s2'nin sütunları çıkartılmış oldu
print(df2.sub(s2,axis="index"))

print("\n************\n")

vs=pd.DataFrame(np.random.randn(4,3),
                columns=list("ABC"),
                index=["ali","berk","can","efe"])
print(vs)

print("\n************\n")

# elemanları mutlak değere almak
print(np.abs(vs))

print("\n************\n")

# sütunların maximum ve minimum değerleri arasındaki farkı yazdırmak
f=lambda x:x.max()-x.min()
# şimdi bu fonksiyonu apply metodu ile veri setine uygulayalım:
# böylece f fonsiyonu her sütundaki en büyük ve en küçük değerleri bulup birbirinden çıkarttı
print(vs.apply(f))

print("\n************\n")

# f fonksiyonunu satırlar üzerine uygulamak:
print(vs.apply(f,axis=1))

print("\n************\n")

# apply()'ı kendi yazdığımız fonksiyon üzerine uygulamak
def f(x): return x**2
print(vs.apply(f))