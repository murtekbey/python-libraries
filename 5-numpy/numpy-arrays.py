import numpy as np

result = np.array([1,3,5,7,9])
# result = np.arange(1,10) # 1'den, 10'a kadar eleman oluşturur. 10 dahil değil.
# result = np.arange(10,100,3) # 10 ile 100 arasında bir dizi oluşturur. 3'er 3'er artarak devam eder. 100 dahil değil.
# result = np.zeros(10) # 10 tane sıfır gönderir.
# result = np.ones(10) # 10 tane 1 gönderir. Her bir eleman float bir değere karşılık gelir.
# result = np.linspace(0,100,5) # verdiğimiz başlangıç ve bitiş sayılarını 5 eşit parçaya böler. [0. 25. 50. 75. 100.]
# result = np.linspace(0,5,5) # [0.   1.25    2.5     3.75    5.]
# result = np.random.randint(0,10) # 0 ile 10 arasında bir sayı üretir. 10 dahil değil.
# result = np.random.randint(20) # başlangıç değeri vermeden 0 ile 20 arasında bir sayı üretir. 20 dahil değil.
# result = np.random.randint(1,10,3) # rasgele üretilmiş 1 ile 10 arasında 3 tane sayı gönderir.
# result = np.random.rand(5) # 0 ile 5 arasında, 5 tane sayı üretir.
# result = np.random.randn() # creates an array of specified shape and fills it with random values as per standard normal distribution. (belirli bir şekil dizisi oluşturur ve standart normal dağılıma göre rastgele değerlerle doldurur.)

'''
np_array = np.arange(50) # 0'dan 50'ye kadar bir dize oluşturur.
np_multi = np_array.reshape(5,10) # 5'e 10'luk bir matris oluşturur. (50 tane sayıyı 5 parçaya, 10'ar 10'ar böler.)

print(np_multi.sum(axis=1)) # satırların toplamını verir. (bir dize içerisindeki 10 elemanın toplamı)
print(np_multi.sum(axis=0)) # sütunların toplamını verir. (her sütundaki sırasıyla elemanların toplamı)

# [ 45 145 245 345 445] (axis=1)
# [100 105 110 115 120 125 130 135 140 145] (axis=0)

# [[ 0  1  2  3  4  5  6  7  8  9]
#  [10 11 12 13 14 15 16 17 18 19]
#  [20 21 22 23 24 25 26 27 28 29]
#  [30 31 32 33 34 35 36 37 38 39]
#  [40 41 42 43 44 45 46 47 48 49]]
print(np_multi)
'''

rnd_numbers = np.random.randint(1,100,10) # 1 ile 10 arasında 10 tane random sayı üretir.
print(rnd_numbers)
# result = rnd_numbers.max() # üretilen sayılardan en büyüğünü verir.
# result = rnd_numbers.min() # üretilen sayılardan en küçüğünü verir.
# result = rnd_numbers.mean() # üretilen sayıların ortalamasını bize verir.
# result = rnd_numbers.argmax() # üretilen en büyük sayının kaçıncı index de olduğunu söyler.
# result = rnd_numbers.argmin() # üretilen en küçük sayının kaçıncı index de olduğunu söyler.
print(result)

