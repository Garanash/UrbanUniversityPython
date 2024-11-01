def custom_write(file_name, strings):
    strings_position = {}
    file = open(file_name, 'a', encoding='utf-8')
    for i, j in enumerate(strings):
        key = (i + 1, file.tell())
        strings_position[key] = j
        file.write(j + '\n')
    file.close()
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
