import pandas as pd

# series veri tipi bir sütundan oluşur yani bir boyutludur

obje=pd.Series([1,"Ali",3.5,"Hey"])
print(obje)

print("\n*******\n")

print(obje[3])

print("\n*******\n")

# objenin değerlerini verir
print(obje.values)

print("\n*******\n")

obje=pd.Series([1,"Ali",3.5,"Hey"], index=["a","b","c","d"])
print(obje)

print("\n*******\n")

print(obje["c"])

print("\n*******\n")

print(obje.index)

print("\n*******\n")

puan={"Ali":80,"Can":80,"Efe":75,"Buse":95}
nt=pd.Series(puan)
print(nt)


print("\n*******\n")

print(nt["Can"])

print("\n*******\n")

print(nt[nt>85])

print("\n*******\n")

print(nt>85)

print("\n*******\n")

nt["Can"]=60
print(nt)

print("\n*******\n")

nt[nt<80]=83
print(nt)

print("\n*******\n")

print("Efe" in nt)

print("\n*******\n")

# matematiksel işlem de yapılabilir
print(nt/10)

print("\n*******\n")

# pythonda eksik veriyi bulur yani null varsa true döner
print(nt.isnull())
