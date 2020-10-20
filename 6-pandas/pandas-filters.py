import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns=["Column1","Column2","Column3","Column4","Column5"])

result = df
result = df.columns # dataframe içerisinde bulunan columnları verir.
result = df.head() # ilk 5 kaydı çağırır.
result = df.head(10) # ilk 10 kaydı çağırır.
result = df.tail() # son 5 kaydı çağırır.
result = df.tail(10) # son 10 kaydı çağırır.
result = df["Column1"].head() # ilk 5 kaydı alır ve sadece Column1'i getirir.
result = df.Column1.head() # df["Column1"].head() ile aynı. ALTERNATIF
result = df[["Column1","Column2"]].head() # ilk 5 kaydın Column1 ve Column2'yi getirir.
result = df[["Column1","Column2"]].tail() # son 5 kaydın Column1 ve Column2'yi getirir.
result = df[5:15][["Column1","Column2"]].head() # ilk 5 değil daha sonraki 5'i almış oluyoruz çünkü başta indeksimizi 5 den başlattık.
result = df[5:15][["Column1","Column2"]].tail() # 15 den sonraki son 5 kaydı getirir.

result = df > 50 # df içerisindeki tüm Column'lara bakar ve içerisindeki bilgilerden 50 den büyük tüm sayılara "True" olmayanlara "False" bilgisi yazdırır.
result = df[df > 50] # df içerisindeki tüm Column'lara yine bakar ve True,False yerine True olan yerlerde bize sayıyı gösterir olmayan yerlerde NaN bilgisini verir.
result = df[df%2==0] # çift olanları gösterir diğerlerine NaN bilgisini verir.
result = df["Column1"] > 50 # sadece Column1 içindeki koşullara bakar ve True ya da False değeri getirir.
result = df[df["Column1"] > 50]["Column1"] # Column1'de sadece 50'den büyük sayıları getirir.
result = df[df["Column1"] > 50][["Column1","Column2"]] # Burda bize Column2'yide getirir fakat Koşula uyup uymadığına bakılmaz.

result = df[(df["Column2"] > 50) & (df["Column1"] <= 70)] # 2 koşul birden verdik. burda verdiğimiz koşul Column2'deki değerlerin 50 den büyük olması ve Column1'deki değerlerin 70 den küçük olması.
result = df[(df["Column2"] > 50) & (df["Column1"] <= 70)][["Column1","Column2"]] # sadece column1 ve column2 yi getirmek istiyosak.

result = df[(df["Column2"] > 50) | (df["Column1"] <= 70)] # 2 koşuldan sadece 1'nin doğru olması yeterli.
result = df[(df["Column2"] > 50) | (df["Column1"] <= 70)][["Column1","Column2"]]

result = df.query("Column1 >= 50 & Column1 % 2 == 0") # query metodu aracıylada bulabiliriz.
result = df.query("Column1 >= 50 & Column1 % 2 == 0")["Column1"]
result = df.query("Column1 >= 50 | Column1 % 2 == 0")["Column1"]
print(result)