import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bca","ade","cba","dea"]
}

df = pd.DataFrame(data)

def kareal(x):
    return x * x

kareal2 = lambda x: x * x

result = df
result = df["Column2"].unique() # benzeri olmayan değerleri getirir. listede 2 tane 20 varsa sadece birini getirir.
result = df["Column2"].nunique() # 4 tane tekil bilgi kolonun içerisinde mevcut.
result = df["Column2"].value_counts() # aynı bilginin kaç kere tekrarlandığını söyler --> örn; 20, 2 kere tekrarlanmış. 
result = df["Column1"] * 2 # 2 ile çarpılmış değerleri gelir.
result = df["Column1"].apply(kareal) # fonksiyonları gönderebiliriz. 
result = df["Column1"].apply(kareal2) # lambda metodunu gönderebiliriz.
result = df["Column1"].apply(lambda x: x * x)
result = df["Column3"].apply(len) # her bir elemanın kaç karakterli olduğunu söyler.
df["Column4"] = df["Column3"].apply(len) # orjinal liste üzerinde bir güncelleme olur ve column4 üzerinden column3 deki karakter sayılarını söyler.
result = df.columns
result = len(df.columns)
result = len(df.index)
result = df.info
result = df.sort_values("Column2") # küçükten büyüğe sıralanmış şekilde gelir.
result = df.sort_values("Column3") # alfabetik sıralama yapar.
result = df.sort_values("Column3", ascending = False) # alfabetik sıralamanın tersine göre dizim yapar.

# print(result)

data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)

print(df.pivot_table(index="Ay",columns= "Kategori", values= "Gelir")) # index değerini Aylara göre, columns değerlerini Kategoriye göre, values değerlerini Gelir'in yerlerine yazdırdık.
