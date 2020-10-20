import pandas as pd
import numpy as np

df = pd.read_csv('imdb.csv')

# 1. Dosya hakkındaki tüm bilgiler
result = df
result = df.columns
result = df.info

# 2. ilk 5 kaydı gösterin.
result = df.head()

# 3. ilk 10 kaydı gösterin.
result = df.head(10)

# 4. son 5 kaydı gösterin.
result = df.tail()

# 5. son 10 kaydı gösterin.
result = df.tail(10)

# 6. Sadece Movie_Title kolonunu gösterin.
result = df["Movie_Title"]

# 7. Movie_Title kolonunun ilk 5 kaydı.
result = df["Movie_Title"].head()

# 8. Movie_Title ve Rating kolonunun ilk 5 kaydı.
result = df[["Movie_Title","Rating"]].head()

# 9. Movie_Title ve Rating kolonunun son 7 kaydı.
result = df[["Movie_Title","Rating"]].tail(7)

# 10. Movie_Title ve Rating kolonunun ikinci 5 kaydını getirin. 
result = df[5:][["Movie_Title","Rating"]].head()

# 11. Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0 üzeri olan kayıtlardan ilk 50 tanesini getirin.
result = df[df["Rating"]>= 8.0][["Movie_Title","Rating"]].head(50)

# 12. Yayın tarihi 2014-2015 arasında olan tüm filmlerin isimlerini getiriniz.
result = df[(df["YR_Released"]>=2014) & (df["YR_Released"]<=2015)][["Movie_Title","YR_Released"]]

# 13. Değerlendirme sayısı 100.000'den büyük ya da imdb puanı 8-9 arasında olan tüm filmleri getirin.
result = df[(df["Num_Reviews"] >= 100000) | ((df["Rating"] >= 8.0) & (df["Rating"] <= 9.0))][["Movie_Title","Num_Reviews","Rating"]]


print(result)