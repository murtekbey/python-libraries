import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index=['a','c','e','f','h'], columns=['column1','column2','column3'])

df = df.reindex(['a','b','c','d','e','f','g','h'])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn

result = df
result = df.drop("column1",axis=1) # kolon(sütunu) siler.
result = df.drop(["column1","column2"],axis=1)
result = df.drop('a',axis=0) # satırı siler
result = df.drop(['a','b','h'],axis=0)

result = df.isnull()
result = df.notnull()
result = df.isnull().sum() # null değerlerini sayar.
result = df["column1"].isnull().sum()
result = df[df["column1"].isnull()]
result = df[df["column1"].isnull()]["column1"]
result = df[df["column1"].notnull()] # sorgulamamızı column1'e göre yaptık. ama tüm columnlar gelir çünkü özel istekde bulunmak gerek.
result = df[df["column1"].notnull()]["column1"] # bu şekilde.

result = df.dropna() # nan olan satırı siler --> default axis=0 ayarlıdır.
result = df.dropna(axis=1) # nan olan kolonu(sütunu) siler.
result = df.dropna(how = "any") # herhangi bir nan bulursa o satırı siler.
result = df.dropna(how = "all") # tüm satırlar nan olmadığı sürece o satırı getirir. hepsinin nan olması gerek silmesi için.
result = df.dropna(subset=["column1","column2"], how="all") # özel olarak column belirterek nan'ları arar ve siler. hepsinin nan olması gerekli.
result = df.dropna(subset=["column1","column2"], how="any") # özel olarak column belirterek nan'ları arar ve siler. herhangi birinin nan olması yeterli.
result = df.dropna(thresh=2) # en az 2 veri olması gerekiyor getirmesi için. yoksa siler.
result = df.dropna(thresh=4) # en az 4 veri olması gerekiyor getirmesi için. yoksa siler.

result = df.fillna(value = "no input") # boş alanları doldurur.
result = df.fillna(value = 1)

result = df.sum() # kolonların içindeki satırların toplamı
result = df.sum().sum() # kolonların birbiriyle toplamı.
result = df.size
result = df.isnull().sum() # kolonlar içinde null değeri olan satırların toplamı
result = df.isnull().sum().sum() # kolonların içindeki null değerlerin toplamının tüm kolonların birbiriyle toplamı.

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet

result = df.fillna(value= ortalama(df)) # tüm null olan yerlere hesaplanan ortalama değerini yazdırdık.

print(result)
