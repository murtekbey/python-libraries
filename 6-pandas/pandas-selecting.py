import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3),index = ["A","B","C"], columns = ["Column1","Column2","Column3"])

result = df
result = df["Column1"]
result = type(df["Column1"]) # <class 'pandas.core.series.Series'>
result = df[["Column1","Column2"]]

# loc["row","column"] => loc["row"] => loc[":","column"]
result = df.loc["A"] # A satırını seri olarak gönderir
result = type(df.loc["A"]) # <class 'pandas.core.series.Series'>
result = df.iloc[2] # index numaraları kendiniz A,B,C diye verseniz dahi iloc metoduyla normal usul index numaralarına ulaşabilirsin.
result = df.loc[:,"Column1"] # sadece Column1 gelir.
result = df.loc[:,["Column1","Column2"]] # df[["Column1","Column2"]] ile aynı

result = df.loc[:,"Column1":"Column3"] # başlangıç ve bitişler dahil olmak üzere Column1 den Column3 e kadar gelir. Column 3 de dahil.
result = df.loc[:,:"Column3"] #  df.loc[:,"Column1":"Column3"] ile aynı görev.
result = df.loc["A":"B",:"Column3"] #  A dan B' ye kadar getirir. -> index numaralarını değiştirdiğimiz için string olarak belirtiyoruz.
result = df.loc[:"B",:"Column3"] # Baştan başlayıp B'ye kadar getirir.
result = df.loc["A","Column2"] # A indeksinin Column2 sindeki bilgiyi getirir.
result = df.loc["C","Column1"] # C indeksinin Column1 indeki bilgiyi getirir.
result = df.loc[["A","B"],["Column1","Column2"]] # A ve B indeksinin Column1 ve Column2 deki bilgileri getirir.

df["Column4"] = pd.Series(randn(3), ["A","B","C"]) # 4. Column'da eklenir ve 3 tane değer yazdırılır.
df["Column5"] = df["Column1"] + df["Column3"] # 5. Column'da eklenir ve Column1 ile Column3 ' ün toplamı yazdırılır.

result = (df.drop("Column5", axis = 1)) # Column5'i silmemizi sağlar. FAKAT axis değeri vermemiz gerekiyo çünkü axis=1 değeri bize Column'un yukardan aşağı silinmesi gerektiği bilgisini verir.
                                    # print(df) diye yazdırıldığında Orjinal içerikte bir değişiklik olmaz yani Column5 silinmez.

df.drop("Column5", axis = 1, inplace = True) # inplace = True metoduyla df nin içerisindeki orjinal bilgiyi de değiştirmiş oluruz.

print(result)
print(df)