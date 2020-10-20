import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2 # aynı indekse denk gelen elemanları toplar yeni bir satır oluşturur.
result = numbers1 + 10 # aynı indekse denk gelen elemanların her birine +10 ekler.
result = numbers1 - numbers2 # aynı indekse denk gelen elemanların farkları gelir.
result = numbers1 - 10 # aynı indekse denk gelen elemanlarına her birine -10 ekler.
result = numbers1 * numbers2 # aynı indekse denk gelen elemanları çarpar.
result = numbers1 * 10 # aynı şekilde 10 ile tüm elemanları çarpar.
result = numbers1 / numbers2 # aynı indekse denk gelen elemanları böler.
result = numbers1 / 10 # tüm elemanları 10'a böler.

result = np.sin(numbers1) # her bir elemanın sinusunu alır.
result = np.cos(numbers1) # her bir elemanın cosinusunu alır.
result = np.sqrt(numbers1) # her bir elemanın karekökünü alır.
result = np.log(numbers1) # her bir elemanın logaritmasını alır.

mnumbers1 = numbers1.reshape(2,3) 
mnumbers2 = numbers2.reshape(2,3)

result = np.vstack((mnumbers1,mnumbers2)) # yukarıda verilen 2 matrisi dikey olarak birleştirir. (v=vertical)
result = np.hstack((mnumbers1,mnumbers2)) # yukarıda verilen 2 matrisi yatay olarak birleştirir. (h=horizontal) --> 2. matrisi alır ve 1. matrisin sağ tarafına ekler.

result = numbers1 >= 25 # numbers1'deki elemanların hepsine bakar ve bize bool türünde True ya da False değer gönderir.

result = numbers1 % 2 == 0 # numbers1'deki elemanların 2 ye bölümünden kalanının 0 olup olmadığını kontrol eder.
print(numbers1[result]) # bize sadece yukarıdaki result koşulunu sağlayan yani True değerini veren elemanları gönderir.

# print(mnumbers1)
# print(mnumbers2)

print(result)