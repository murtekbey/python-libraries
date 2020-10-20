import numpy as np

# 1-
result = np.array([10,15,30,45,60])

# 2-
result = np.arange(5,15)

# 3-
result = np.arange(50,100,5)

# 4-
result = np.zeros(10)

# 5-
result = np.ones(10)

# 6-
result = np.linspace(0,100,5)

# 7-
result = np.random.randint(10,30,5)

# 8-
result = np.random.randn(10)

# 9-
np_array = np.random.randint(10,50,15) # --> .reshape metodu devamına eklenebilir.
np_multi = np_array.reshape(3,5)
# print(np_multi)

# 10-
result = np_multi.sum(axis=1) # satırların toplamı
result = np_multi.sum(axis=0) # sütunların toplamı

# 11-
result = np_multi.max()
result = np_multi.min()
result = np_multi.mean()

# 12-
result = np_multi.argmax()

# 13-
numbers = np.arange(-50,50)
result = numbers[:3]

# 14-
result = numbers[::-1]

# 15-
result = np_multi[0]

# 16-
result = np_multi[1,2]

# 17-
result = np_multi[:,0]

# 18-
result = np_multi ** 2

# 19-
ciftler = numbers[numbers % 2 == 0]
result = ciftler[ciftler>0]
print(result)