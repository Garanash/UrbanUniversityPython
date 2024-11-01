# Домашнее задание по теме "Обзор сторонних библиотек Python".

import numpy as np
import pandas as pd
import requests as rq

response = rq.get("https://ya.ru/")
print(response)
with open("test.tdifferences = np.zeros((1, 1000))xt", "wb") as file:
    file.write(response.content)

print("numpy")
np_array = np.arange(15).reshape(3, 5)
print(np_array)
print(np_array.shape)
print(np_array.size)
print(np_array.dtype.name)
print(type(np_array))

print("pandas")
df = pd.DataFrame(np_array)
print(df)
print(df.sum())
print(df.dtypes)
