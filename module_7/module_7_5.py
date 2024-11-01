import os
import time

directory = '.'
file_ = directory
for user, dirs, filenames in os.walk(directory):
    for file in filenames:
        filepath = os.path.join(file_, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        abs_path = os.path.abspath(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}, Абсолютный путь: {abs_path}')
