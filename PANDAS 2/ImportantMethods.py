import pandas as pd
import numpy as np

s=pd.Series([1,2,3,4],index=["a","b","c","d"])
print(s)

print("\n*******\n")

print(s["a"])

print("\n*******\n")

# reindex(): belirleriğimiz indexlere göre veriyi yeniden düzenler
# s'deki indexleri değiştirip s2'ye eşitle
# daha önceden var olan değerler aynı şekilde olur ama var olmayanlar NaN olur
s2=s.reindex(["m","d","a","c","k"])
print(s2)

print("\n*******\n")

# reindex() ile boş değerlere atama yapmak
s3=pd.Series(["mavi","sarı","mpr"],index=[0,2,4])
print(s3)

print("\n*******\n")

# s3'deli boş değerleri yani NaN olanları doldurmak:
print(s3.reindex(range(6),method="ffill"))

print("\n*******\n")


df=pd.DataFrame(np.arange(9).reshape(3,3),index=["a","c","d"]
                                         ,columns=["ali","efe","can"])
print(df)

print("\n*******\n")

# df'nin indexlerini değiştirme
df2=df.reindex(["d","c","b","a"])
print(df2)

print("\n*******\n")

# sütunları indexlemek:
isim=["efe","nur","ali"]
print(df.reindex(columns=isim)) # nur için değer girmediğimiz için NaN oldu

print("\n*******\n")

# loc ve iloc ile istediğimiz satır ve sütunu seçebiliriz
# loc metodu ile satırları indexleyebiliriz
# loc metoduyla satırları a,c,d olan df veri etinin satırlarını c,d,a yapalım
print(df.loc[["c","d","a"]])

print("\n*******\n")

# drop() metodu ile istediğin satır veuya sütunu silebilirsin
s=pd.Series(np.arange(5.),index=["a","b","c","d","e"])
print(s)

print("\n*******\n")

# b satırını silelim
yeni_s=s.drop("b")
print(yeni_s)

print("\n*******\n")


# birden fazla satır silmek için drop() fonksiyonu içine silinecek satırları liste şeklinde yaz
s=s.drop(["c","d"])
print(s)

print("\n*******\n")

veri=pd.DataFrame(np.arange(16).reshape(4,4),
                  index=["ali","can","efe","nur"],
                  columns=list("ABCD"))
print(veri)

print("\n*******\n")

# drop metodu ile ali ve efe satırlarını sil
print(veri.drop(["ali","efe"]))

print("\n*******\n")


# sütun silmek için axic=1 kullanılır
# satır silmek için axis=0 kullanılır

# A ismindeki sütunu silelim
print(veri.drop("A",axis=1))

print("\n*******\n")

# Ali satırını silelim
print(veri.drop("ali",axis=0))

print("\n*******\n")

# sütunların ortalamalarını almak
print(veri.mean())

print("\n*******\n")

# mean() metodu içinde axis=1 dersem satır ortalaması alır çünkü axis=1 diyerek herbir sütunu topladık
print(veri.mean(axis=1))

print("\n*******\n")

# mean metodu içinde axis=0 dersen sütun oralaması alır çünkü herbir satırı toplar
print(veri.mean(axis=0))

print("\n*******\n")

print("axis=1 yerine axis=columns yazabilirsin aynı şeydir")
print("axis=0 yerine axis=index yazabilirsin aynı şeydir")
