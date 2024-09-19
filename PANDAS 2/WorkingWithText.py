import pandas as pd
import numpy as np
veri=["ali","Berk","DENiz",np.nan,"zEYNEP"]

# verinin tüm isimlerinin ilk harfini büyük yapalım
# önce veri Series yapısına çevrilir
isim=pd.Series(veri)
# str niteliği string metotlara ulaşmayı sağlar
# şimdi sadece ilk harfleri büyük yapalım
print(isim.str.capitalize())

print("\n*************\n")

# issimdeki tüm harfleri küçük yapalım:
print(isim.str.lower())

print("\n*************\n")

# isimlerin uzunluklarını bulalım
print(isim.str.len())

print("\n*************\n")

# a harfiyle mi başlıyor ona bakalım
print(isim.str.startswith("a"))

print("\n*************\n")

df=pd.DataFrame(np.random.randn(3,2),
                columns=["Sutun A","Sutun B"],
                index=range(3))
print(df)

print("\n*************\n")

# dataframe columns'u string olduğundan onun içim str kullanalım
print(df.columns)
print()
# sütun isimlerini küçük harf yapalım
print(df.columns.str.lower())

print("\n*************\n")

# sütun isimlerini hem küçük harf yapalım hem de boşlukların yerine alt tire yazalım
print(df.columns.str.lower().str.replace(" ","_"))

print("\n*************\n")

# Series yapısında liste döndürmek
s=pd.Series(["a_b_c","c_d_e",np.nan,"f_g_h"])
print(s)

print("\n*************\n")

# split metoduyla harfleri ayırıp liste yapalım
print(s.str.split("_"))

print("\n*************\n")

# ayrılan listelerin elemanlarına ulaşmak:
# mesle herbir değerin birinci indexe sahip karakterini bulalım
print(s.str.split("_").str.get(1))
# şöyşe de olur: s.str.split("_").str[1]

print("\n*************\n")

# ayrılan değerleri dataframe yapısına dönüştürmek için expand=True yapılır
print(s.str.split("_",expand=True))

print("\n*************\n")

# ayırma işlemini sınırlayabiliriz
# mesela sadece 1 ayırma yapalım
print(s.str.split("_",expand=True,n=1))

print("\n*************\n")

para=pd.Series(["15","-$20","$30000"])
# dolar işaretini kaldıralım
print(para.str.replace("$",""))

print()

# hem - hem de dolar işaretini kaldıralım
# dolar işareti özel karakter olduğu şçin onun önüne kaçış karakteri yani \ getirmemiz gerek
print(para.str.replace("-\$",""))

print("\n*************\n")

# şimdi gerçek veri seti kullanarak pandastaki veri setleri üstünde işlemler yapalım


print("\n*************\n")


print("\n*************\n")


print("\n*************\n")


print("\n*************\n")

