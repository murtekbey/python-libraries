import pandas as pd
import numpy as np

#data
numbers =   [20,30,40,50] # data türünü int64(integer) olarak tanımlar.
letters = ['a','b','c','d'] # data türünü obje olarak tanımlar.
# letters = ['a','b','c',20] # data türünü yine obje olarak tanımlar.
scalar = 5
dict = {'a':10,'b':20,'c':30,'d':40} # key-value bilgisi oluştururuz.
random_numbers   = np.random.randint(10,100,6)

# pandas_series = pd.Series()
# pandas_series = pd.Series(numbers)
# pandas_series = pd.Series(letters)
# pandas_series = pd.Series(scalar, [0,1,2,3]) # scalardan gelen 5 bilgisini verdiğimiz index kadar arttılır ve hepsine scalar değerini verir.
# pandas_series = pd.Series(dict) # index değerleri key değeriyle değişir ve karşısına value değerlerini yazar.
# pandas_series = pd.Series(random_numbers) # rasgele üretilen sayılar pandas serisi olarak karşımıza gelir.

pandas_series = pd.Series([20,30,40,50], ['a','b','c','d']) # her bir numaraya kendi key bilgimizi vermiş oluruz.

# result = pandas_series[0] # pandas seriesin içindeki 20 bilgisi gelir.
# result = pandas_series[-1] # pandas seriesin içindeki 50 bilgisi gelir.
# result = pandas_series[:2] # ilk 2 elemanı gelir.
# result = pandas_series[-2:] # son 2 elemanı gelir.
# result = pandas_series['a'] # a keyine karşılık gelen 20 bilgisi gelir.
# result = pandas_series['d'] # d keyine karşılık gelen 50 bilgisi gelir.
# result = pandas_series[['a','c']] # a ve c keyine karşılık gelen 20,40 bilgisi gelir.

# result = pandas_series.ndim # 1 boyutlu bir liste olduğu bilgisi gelir.
# result = pandas_series.dtype # data türünü söyler.
# result = pandas_series.shape # 4 elemanlı tek boyutlu bir liste olduğu bilgisi gelir.
# result = pandas_series.sum() # elemanların toplamının 140 olduğu bilgisi gelir.
# result = pandas_series.max() # en büyük eleman
# result = pandas_series.min() # en küçük eleman
# result = pandas_series + pandas_series # elemanları birbirine toplar index sırasına göre.
# result = pandas_series + 50 # her elemana 50 ekler.

result = np.sqrt(pandas_series) # numpy'un karekök hesaplama metodu üzerinden pandas verilerinin her birinin karekök bilgisini aldık.
result = pandas_series >= 50 # 50'den büyük yada eşit sayıların bool tipiyle True yada False olarak yazdırdık.
result = pandas_series % 2 == 0 # sayıların çift sayı olup olmadığını True ya da False değer ile getirebiliriz.

# print(pandas_series[pandas_series % 2 == 0]) # sadece çift sayıları getirir.

# print(pandas_series)
# print(result)

opel2018 = pd.Series([20,30,40,10],['astra','corsa','mokka','insignia']) 
opel2019 = pd.Series([40,30,20,10],['astra','corsa','Grandland','insignia'])

total =  opel2018 + opel2019 # mokka bilgisine karşılık gelen ilk listede 40 fakat diğer listede mokka bilgisine karşılık gelen bi bilgi olmadığı için NaN(Not a number) bilgisi gelir.
                             # aynı şey Grandland için de geçerli oluyor. NaN
                             
print(total['astra']) # sadece astra bilgisi gelir.