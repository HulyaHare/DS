# satırları birleştirirler
import pandas as pd
import numpy as np

v1=pd.DataFrame({"anahtar":["a","b","c","c","d","e"],
                 "say1":range(6)})
v2=pd.DataFrame({"anahtar":["b","c","d","e"],
                 "say2":range(4)})
print(v1)
print()
print(v2)

print("\n*******\n")

# iki veri setini birleştirelim
print(pd.merge(v1,v2))

print("\n*******\n")

# hamgi sütuna göre veri setlerinn birleştirileceğini merge fonksiyonuna belirtebiliriz
print(pd.merge(v1,v2,on="anahtar"))

print("\n*******\n")

# eğer birleştirilecek sütun isimleri farklı ise bu sütunşarı ayrı ayrı belirtebiliriz
v3=pd.DataFrame({"anahtar1":["a","b","c","c","d","e"],
                 "say1":range(6)})
v4=pd.DataFrame({"anahtar2":["b","c","d","e"],
                 "say2":range(4)})
print(pd.merge(v3,v4,left_on="anahtar1",right_on="anahtar2"))

print("\n*******\n")

# mesela v3'deki a değerininv4'de karşılığı olmadığından ekrana yazdırılmadı
# eğer a değeri de yazdırılmak isteniyorsa şöyle yapılır
print(pd.merge(v3,v4,left_on="anahtar1",right_on="anahtar2",how="outer"))

print("\n*******\n")

# how yerine laft yazarsan:
# bu soldaki verinin anahtar sütununa göre veri tablosunu oluştır anlammına gelir
# how yerine right yazarsan:
# bu sağdaki verinin anahtar sütununa göre veri tablosunu oluştır anlammına gelir
print(pd.merge(v3,v4,left_on="anahtar1",right_on="anahtar2",how="left"))
print()
print(pd.merge(v3,v4,left_on="anahtar1",right_on="anahtar2",how="right"))

print("\n*******\n")

# veri setindeki ortak değerleri şöyle alırız
print(pd.merge(v3,v4,left_on="anahtar1",right_on="anahtar2",how="inner"))

print("\n*******\n")

# veri setini birleştiriken birden fazxla anahtar sütun kullanmak:
v1=pd.DataFrame({"anahtar":["a","b","c","c","d","e"],
                 "say1":range(6),
                 "rakam":["bir","uc","iki","bir","bir","iki"]})
v2=pd.DataFrame({"anahtar":["b","c","d","f"],
                 "say2":range(4),
                 "rakam":["bir","bir","iki","iki"]})
print(v1)
print(v2)

print("\n*******\n")

# bu iki veri setini, anahtar ve rakam sütunlarına göre birleştirelim
print(pd.merge(v1,v2,on=["anahtar","rakam"])) # ortak değerlere göre birleşir
print()
print(pd.merge(v1,v2,on=["anahtar","rakam"],how="outer"))

print("\n*******\n")

# ismi aynı olanları birleştiriken ismini değişltirip sonuna x,y ekleyip yazar
print(pd.merge(v1,v2,on="anahtar",how="outer"))

print("\n*******\n")

# istersek bu ekleri (x ve y olanı) değiştirebiliriz
print(pd.merge(v1,v2,on="anahtar",how="outer",suffixes=("_veri1","_veri2")))

print("\n*******\n")

# bazı durumlarda birleştirilecek anahtar sütun dataframenin sütununda olabilir
# o zaman birleştirilecel index left index=true ya da right index=true şeklinde olmalıdır
df1=pd.DataFrame({"harf":["a","a","b","b","a","c"],"say":range(6)})
df2=pd.DataFrame({"deger":[3,5,7]},index=["a","b","e"])
print(df1)
print(df2)

print("\n*******\n")

# şimdei df2 veri setinin indexlerine göre veri setlerini birleştirelim
print(pd.merge(df1,df2,left_on="harf",right_index=True))

print("\n*******\n")

# ist4ersek hem right hem left kullanılabilir
sag=pd.DataFrame([[1,2],[3,4],[5,6]],index=["a","c","d"],columns=["ali","nur"])
sol=pd.DataFrame([[7,8],[9,10],[11,12],[13,14]],index=["a","b","e","f"],columns=["efe","ata"])
print(sag)
print(sol)

print("\n*******\n")

# her iki taraftan da birleştirdik
print(pd.merge(sag,sol,right_index=True,left_index=True,how="outer"))

print("\n*******\n")

# birleştirme işlemini join() ile de yapabiliriz
print(sol.join(sag))
print()
# bütün değerleri şöyle görebilirsin
print(sol.join(sag,how="outer"))

print("\n*******\n")

# ikiden fazla veri setini birleştirmek:
diger=pd.DataFrame([[1,3],[5,7],[9,11]],index=["a","b","f"],columns=["buse","sena"])
print(diger)

print("\n*******\n")

# üç veri setini birleştirelim
print(sol.join([sag,diger]))

print("\n*******\n")

# dizilerde aynı bpyutta iki dizi birleştirilebilir
dizi=np.arange(20).reshape(4,5)
print(dizi)
print()

# bu diziyi sütun olarak kendisiyle birleştirelim:
print(np.concatenate([dizi,dizi],axis=1))
print()

# bu diziyi satır olarak kendisiyle birleştirelim:
print(np.concatenate([dizi,dizi],axis=0))

print("\n*******\n")

# pandasta faarklı indexlere sahip verileri birleştirmek
veri1=pd.Series([0,1],index=["a","b"])
veri2=pd.Series([2,3,4],index=["c","d","e"])
veri3=pd.Series([5,6],index=["f","g"])

# verileri satır olarak birleştirmek:
print(pd.concat([veri1,veri2,veri3]))
print()
# verileri sütun olarak birleştirmek:
print(pd.concat([veri1,veri2,veri3],axis=1,sort=False))
print()
# eğer indexlerin kesişimini almak istersek join=inner kullanılır
print(pd.concat([veri1,veri2,veri3],axis=1,sort=False,join="inner"))

print("\n*******\n")

# eğer indexlerin kesişimini almak istersek join=inner kullanılır
veri4=pd.Series([10,11,2],index=["a","b","c"])
print(pd.concat([veri1,veri4],axis=1,join="inner"))

print("\n*******\n")

print("isterseniz veri tablosuna alacağınız değerleri join_axes metoduyla belirleyebilirsin")

print("\n*******\n")

#eksen üzerinde hiyerarşik indexleme yapmak
x=pd.concat([veri1,veri2,veri4],axis=1,keys=["bir","iki","uc"],sort=False)
print(x)

print("\n*******\n")

# bu kodları dataframede de kullanabiliriz
vs1=pd.DataFrame(np.arange(6).reshape(3,2),index=["a","b","c"],columns=["bir","iki"])
vs2=pd.DataFrame(10+np.arange(4).reshape(2,2),index=["a","c"],columns=["uc","dort"])
print(vs1)
print(vs2)

print("\n*******\n")

# hiyerarşik indexlere sahip veri setleri:
print(pd.concat([vs1,vs2],axis=1,keys=["s1","s2"],sort=False))

print("\n*******\n")

# satır indexi olmayan iki veri setini birleştirmek
veri1=pd.DataFrame(np.random.randn(3,4),columns=["a","b","c","d"])
veri2=pd.DataFrame(np.random.randn(2,3),columns=["b","d","a"])
print(veri1)
print(veri2)
print()
print(pd.concat([veri1,veri2],ignore_index=True,sort=False))