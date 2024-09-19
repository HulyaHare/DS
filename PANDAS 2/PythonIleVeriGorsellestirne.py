# veri setimiz veri bilimi maaşlarıdır
import pandas as pd

# veri setini yükleuelim
df=pd.read_csv("ds_salaries.csv")
pd.set_option('display.max_rows', None)  # Satır sayısını sınırsız yapar
pd.set_option('display.max_columns', None)  # Sütun sayısını sınırsız yapar
print(df.head())

print("\n*******\n")

# veri setindeki satır ve sütun sayılarına bakalım
print(df.shape)

print("\n*******\n")

# şimdi veri setinin sutunlarının özelliklerini inceleyelim
print(df.info())

print("\n*******\n")

# veri setimizdeki eksik verileri kjontrol etmek için isnull kullanalım
print(df.isnull().sum())

print("\n*******\n")

# tüm verideki eksik veriyi görelim
print(df.isnull().sum().sum())

print("\n*******\n")

# sütunlardaki tek değerlere bakalım
print(df.nunique())

print("\n*******\n")

# yıl sütunundaki tek değerlere bakalım
print(df["work_year"].value_counts())

print("\n*******\n")

# 2023 yılında en fazla talep gören ilk 3 mesleğe bakalım
print(df[df["work_year"]==2023]["job_title"].value_counts().nlargest(3))
print()

# şimdi bu mesleklerin indexlerini resetleyelim
# This is useful when the index needs to be treated as a column, or when the index is meaningless and needs to be reset to the default before another operation
df[df["work_year"]==2023]["job_title"].value_counts().nlargest(3).reset_index()

# şimdi veriyi görselleştirelim
import matplotlib.pyplot as plt
import seaborn as sns

# # grafiğin temasını ayarlayalım:
sns.set_theme()

# grafipin boyutunu ve kalitesini ayarlayalım
sns.set(rc={"figure.figsize":(10,6),"figure.dpi":300})

jobs=df[df["work_year"]==2023]["job_title"].value_counts().nlargest(3).reset_index()

# şimdi fig isminde grafik nesnesi oluşturalım
# bu fig'in içinde ax isminde grafik oluşturalım (subplots())
fig,ax=plt.subplots()

# şimdi bir sütun grafiği çizelim
ax=sns.barplot(ax=ax,data=df,y=jobs["index"],x=jobs.jobs_title)

# şimdi eksemşere ve grafiğe isim verelim
ax.set(ylabel="Job Titles",xlabel="Counts",title="Top 3 Titles in 2023")

# ek olarak grafipe mesleklerin sayısını ekleyelim
# padding=2 diyerek etiketlerin barın üstünden iki birim uzakta görünmeisni sağladıl
# ax.containers, ax üzerinde bulunan tüm grafik öğelerini içeren bir liste döner.
# ax.containers[0] bar graafiğindeki barları temsik eden nesneleri içerire
ax.bar_label(ax.containers[0],padding=2)

plt.show()

print("\n*******\n")

#şimdi tecrübe seviyelerine bnakalım
print(df["experience_level"].unique())
# tecrübe değerlerinin isimerlerşnş dğeiştirelim:
df["experience_level"]=df["experience_level"].replace(("EN","Junior"))
df["experience_level"]=df["experience_level"].replace(("MI","Mid-Level"))
df["experience_level"]=df["experience_level"].replace(("SE","Senir"))
df["experience_level"]=df["experience_level"].replace(("EX","Director"))

# şimdi grafik çizdirelim
fig,ax=plt.subplots()

# countplot() ile herbir kategorinin sayısını hesaplayalım
sns.countplot(ax=ax,data=df,x=df.experience_level)

# eksenleri isimlendirelim
ax.set(xlabel="",ylabel="Counts",title="Experience Levels")

# barların üstüne sayı ekleyelim
ax.bar_label(ax.containers[0])

print("\n*******\n")

# çalışma tiplerine bakalım

print("\n*******\n")


print("\n*******\n")


print("\n*******\n")


print("\n*******\n")


print("\n*******\n")


print("\n*******\n")


print("\n*******\n")


print("\n*******\n")

