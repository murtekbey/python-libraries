import numpy as np

# Python Listesi
py_list = [1,2,3,4,5,6,7,8,9]

# Numpy Array
np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3) # 3 e 3 lük dizeler haline getirdik.

print(py_multi)
print(np_multi)

print(np_array.ndim) # Kaç boyutlu olduğunu söyler - 1 boyutlu
print(np_multi.ndim) # 2 boyutlu

print(np_array.shape)
print(np_multi.shape)