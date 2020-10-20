import pandas as pd

df = pd.read_csv("datasets/nba.csv")
# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- Toplam kaç kayıt vardır ?
result = len(df.index) # indexlerin toplam sayısı.

# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?
result = df["Salary"].mean()

# 4- En yüksek maaşı ne kadardır ?
result = df["Salary"].max()

# 5- En yüksek maaşı alan oyuncu kimdir ?
result = df[df["Salary"] == df["Salary"].max()]["Name"].iloc[0] # Burada üretilen koşula gelen kayıt bize gelmiş olur. iloc ile index seçimi yapabiliriz.

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
result = df[(df["Age"] >= 20) & (df["Age"] <= 25)][["Name","Team","Age"]].sort_values("Age", ascending = False) 
    # ilgili kolon koşula uyduğu takdir de bize gelecektir. 
    # sort_values ile büyükten küçüğe dizdik. ascending metodunu False yaparak azalan şekilde gelmesini sağladık.

# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
result = df[(df["Name"] == "John Holland")]["Team"].iloc[0] # .iloc ile indexe göre bi seçim yapıp seri yerine sadece takım bilgisini aldık.

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
result = df.groupby("Team").mean()["Salary"]

# 9- Kaç farklı takım mevcut ?
result = len(df.groupby("Team")) # 30 takım bilgisi olduğunu görürüz.
result = df["Team"].nunique() # nunique bize tekrarlanan alanları teke indirip bize bunun sayısını veriyordu.
result = df["Team"].unique() # tekrarlanan alanları teke indirir ve bize toplam 30 tane farklı takımdan oluşan listeyi gönderir.

# 10- Her takımda kaç oyuncu oynamaktadır ?
result = df["Team"].value_counts() # Team alanı içerisinde bize kaç tane value olduğunu, kaç tane değer olduğunu bize söyler. var olan değer kadar oyuncu vardır.

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
df.dropna(inplace = True) # NaN değerleri işin içinden çıkartalım. Yoksa hata verir. inplace = True dediğimiz zaman orjinal listeyi günceller.
# result = df[df.Name.str.contains("and")]["Name"]

def str_find(name):
    if "and" in name.lower():
        return True
    return False

result = df[df["Name"].apply(str_find)] # önemli olan seçtiğimiz koşulun True ya da False değer göndermesi. içerisinde and geçiyorsa True, değilse False değer göndericek.
print(result)