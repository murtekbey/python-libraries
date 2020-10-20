import pandas as pd

df = pd.read_csv("datasets/youtube-ing.csv")

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- İkinci 5 kaydı getiriniz.
result = df[5:].head(5)

# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
result = len(df.columns)
result = df.columns

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1,inplace=True)
result = df

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
result = (f'Like Ortalaması: {df["likes"].mean()}\nDislike Ortalaması: {df["dislikes"].mean()}')

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
result = df.head(50)[['likes','dislikes']]

# 7- En çok görüntülenen video hangisidir ?
result = df[(df["views"] == df["views"].max())][["title","views"]]
# result =  df.sort_values("views", ascending=False).head(1)[["title","views"]]

# 8- En düşük görüntülenen video hangisidir?
result = df[(df["views"] == df["views"].min())][["title","views"]]
# result =  df.sort_values("views").head(1)[["title","views"]]

# 9- En fazla görüntülenen ilk 10 video hangisidir ?
result =  df.sort_values("views", ascending=False).head(10)[["title","views"]]

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
result = df.groupby("category_id").mean().sort_values("likes", ascending=False)["likes"]

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
result = df.groupby("category_id").sum().sort_values("comment_count", ascending=False)

# 12- Her kategoride kaç video vardır ?
result = df["category_id"].value_counts()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["title-len"] = df["title"].apply(len) # len fonksiyonunu title içerisine göndeririz ve title içerisindeki karakter uzunluğunu hesaplarız.
result = df

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
'''
# def tagCount(tag):
#     return len(tag.split('|'))

# df["tag-count"] = df["tags"].apply(tagCount)
'''

df["tag-count"] = df["tags"].apply(lambda x: len(x.split('|')))
result = df

# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)


def likedislikeoranhesapla(dataset):
    likesList = list(dataset['likes'])
    dislikesList = list(dataset['dislikes'])

    liste = list(zip(likesList,dislikesList)) # (1020,230), (201,233)
    # likesList ve dislikesList'i zip metodu aracıyla bir tuple listesine çevirdik.
    # likesList ve dislikesList deki index değerine göre her bir eleman tuple listesi içerisine alınacak

    oranListesi = []
    for like,dislike in liste: # (212,1212)
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike)) # videonun popülerlik bilgisi.
    return oranListesi

df["popular_rate"] = likedislikeoranhesapla(df)

print(df.sort_values("popular_rate",ascending=False)[["title","likes","dislikes","popular_rate"]])
# print(result)