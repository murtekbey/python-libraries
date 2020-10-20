import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]
result = numbers[-1]
result = numbers[0:3] # en sağdaki değeri almaz 0,1 ve 2. indeksdeki elemanları alır.
result = numbers[:3] # en baştan başlar.
result = numbers[3:] # 3. indeksden başlar sona kadar gider.
result = numbers[::] # baştan sona kadar tüm liste gelir.
result = numbers[::-1] # sağdan sola doğru 1'er 1'er artıcak şekilde karşımıza gelir. yani listeyi tersten yazdırırız.
result = numbers[::-2] # sağdan sola doğru 2'şer 'şer artıcak şekilde karşımzıa gelir. listeyi yine tersten yazdırmış oluruz.

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]]) # 2 boyutlu bir matris oluşturduk. içerideki her bir liste elemanı bir satır olarak geçer.
result = numbers2[0] # 0. satıra ulaşırız.
result = numbers2[2] # 2. satıra ulaşırız
result = numbers2[0,2] # 0. satırın, 2. indexindeki elemana ulaşırız.
result = numbers2[2,1] # 2. satırın, 1. indexindeki elemana ulaşırız.
result = numbers2[:,2] # her satırın, 2. indexindeki elemana ulaşırız.
result = numbers2[:,0] # her satırın, 0. indexindeki elemana ulaşırız.
result = numbers2[:,0:2] # her satırın, 0 ile 2. indeksi arasındaki elemanları getirir. (2 dahil değil her zaman olduğu gibi!)
result = numbers2[-1,:] # son satırdaki, bütün indeks elemanlarını getirir.
result = numbers2[:2,:2] # 0 ve 1. satırdaki, 1. ve 2. indeks elemanlarını getirir.

# print(result)

arr1 = np.arange(0,10)
# arr2 = arr1 # referans kopyalaması (ikisi de aynı adresi tutuyor.)  # arr2 deki değişik yapman arr1'dede değişiklik yapmana sebep olur. çünkü bellek üzerinde aynı adresi tutuyorlar.
arr2 = arr1.copy() # bu yöntem sayesinde arr2 içerisinde yaptığın değişiklik arr1'in içeriğini etkilemez. çünkü arr2 için bir kopyalama işlemi yaptık.

arr2[0] = 20

print(arr1)
print(arr2)

