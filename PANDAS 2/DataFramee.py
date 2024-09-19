# dataframe veri tipi birden fazla sütundan oluşur, çok boyutludur
# yani her sütunda farklı veri tipleri barındırabilen bir dikdörtgendir
import pandas as pd
veri={"isim":["Ali","Can","Efe","Ayşe","Buse","Alp","Nur"],
      "puan":[90,80,85,75,95,60,65],
      "spor":["Güreş","Futbol","Kayak","Yüzme","Tenis","Karete","Sörf"],
      "cinsiyet":["E","E","E","K","K","E","K"]}

df=pd.DataFrame(veri)
print(df)

print("\n************\n")

# ilk beşini verir
print(df.head())

print("\n************\n")

# son beş satır
print(df.tail())


print("\n************\n")

# baştan iki satır
print(df.head(2))

print("\n************\n")

# son iki satır
print(df.tail(2))

print("\n************\n")

# sütunlarun sırasını değiştirmek
df=pd.DataFrame(veri,columns=["isim","spor","cinsiyet","puan"])
print(df)

print("\n************\n")

# sözlükte olmayan yeni bir sütun ismi eklemek

# değerlerini eklemezsen eksik veri olarak görünür
df=pd.DataFrame(veri,columns=["isim","spor","cinsiyet","puan","yas"])
print(df)

print("\n************\n")

# değerleri şöyle ekle
df=pd.DataFrame(veri,columns=["isim","spor","cinsiyet","puan","yas"]
                ,index=["bir","iki","üç","dört","beş","altı","yedi"])
print(df)

print("\n************\n")

# veri setindeki belirli bir sütunu almak
print(df["spor"])
# print(df.spor)  --> bu da olurdu

print("\n************\n")

# birden fazla sütunu almak
sutunlar=["isim","spor"]
print(df[sutunlar])

print("\n************\n")

# belirli satırı seçmek:
print(df.loc["bir"])

print("\n************\n")

# belirli birden fazla satırı seçmek:
print(df.loc[["bir","iki"]])

print("\n************\n")

# yaş sütununa değerler atamak
df["yas"]=18
print(df)

print("\n************\n")

# sütuna liste atamak (yani böylece farklı değerler atayailiriz
değerler=[17,18,19,17,18,20,18]
df["yas"]=değerler
print(df)

print("\n************\n")

# 70 üserinde puan alanların dersten geçtiğini gösteren kod:
index = 0
for note in df["puan"]:
      if note>70:
            """
            burası şöyle olailirdi normalde:
            print(df["isim"][index],note,"puan ile dersten geçti")
            ama böyle yazarsan çıktı verce bile gelecekte bir hata alabileceğinin hata mesajını verir yani böyle yazmamalısın
            """
            #şöyle yaz:  (iloc, dataframe dizilerin indexlenmesini sağlar
            print(df["isim"].iloc[index], note, "puan ile dersten geçti")
      else:
            # üsttte anlattığım aynı sebepten dolayı şöyle olmalı:
            print(df["isim"].iloc[index], note, "puan ile dersten kaldı")
      index += 1

print("\n************\n")

# 70 üzeri not alanların geçtiğini gösteren kod: 2. yolu
df["gecti"]=df.puan>70
print(df)

print("\n************\n")

# bir sütun silmek
del df["gecti"]
print(df)

print("\n************\n")

# sözlük ile dataframe oluşturmak:
notlar={"Mat":{"Ali":85,"Efe":90,"Nur":95},
        "Fiz":{"Ali":90,"Efe":80,"Nur":75}}
puan=pd.DataFrame(notlar)
print(puan)

print("\n************\n")

# satırlar ve sütunların  yerini değiştirmek
print(puan.T)
# böyle yaparsak kalıcı olarak yer değiştirir: puan=puan.T

print("\n************\n")

# satır ve sütunlara isim vermek:
puan.index.name="isim" # satıra isim vermek
puan.columns.name="ders" # sütuna isim vermek
print(puan)

print("\n************\n")

# dataframedeki veri setini iki boyutlu diziye dönüştürmek:
print(puan.values)

print("\n************\n")

# veriyi herhangi bir şekilde değiştirilemek hale getirmek:
index=puan.index
# mesela şunu artık yapamazsın: index[1]="Can"
