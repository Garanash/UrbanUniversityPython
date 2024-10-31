# Импорт необходимых библиотек
import io

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, LSTM, Input
from tensorflow.keras.models import Sequential

# Загрузка данных
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(io.StringIO(requests.get(url).text))

# Просмотр первых строк данных
print(data.head())

# Преобразование данных
data = data['Passengers'].values.astype(float)

# Нормализация данных
scaler = MinMaxScaler(feature_range=(0, 1))
data_normalized = scaler.fit_transform(data.reshape(-1, 1))


# Создание обучающих и тестовых выборок
def create_dataset(data, time_step=1):
    X, y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 0])
    return np.array(X), np.array(y)


time_step = 20
X, y = create_dataset(data_normalized, time_step)

# Разделение на обучающие и тестовые данные
train_size = int(len(X) * 0.8)
test_size = len(X) - train_size
X_train, X_test = X[0:train_size], X[train_size:]
y_train, y_test = y[0:train_size], y[train_size:]

# Изменение формы данных для LSTM [samples, time steps, features]
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# Построение модели LSTM
model = Sequential()
model.add(Input(shape=(time_step, 1)))
model.add(LSTM(50, return_sequences=True))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

# Компиляция и обучение модели
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, batch_size=1, epochs=50)

# Предсказание и оценка модели
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# Обратное преобразование предсказанных значений к исходной шкале
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)
y_train = scaler.inverse_transform([y_train])
y_test = scaler.inverse_transform([y_test])

# Визуализация результатов
plt.figure(figsize=(10, 6))
plt.plot(scaler.inverse_transform(data_normalized), label='Исходные данные')

# Построение прогноза для обучающей выборки
plt.plot(np.arange(time_step, train_size + time_step), train_predict, label='Прогноз (обучение)')

# Построение прогноза для тестовой выборки
plt.plot(np.arange(train_size + time_step, train_size + time_step + len(test_predict)), test_predict,
         label='Прогноз (тест)')

plt.legend()
plt.xlabel('Месяцы')
plt.ylabel('Количество пассажиров')
plt.title('Прогнозирование количества международных авиапассажиров с помощью LSTM')
plt.show()
