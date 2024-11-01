def personal_sum(numbers):
    sam = 0
    incorrect_data = 0
    kol = 0
    for i in numbers:
        try:
            sam += i
            kol += 1
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return (sam, incorrect_data, kol)


def calculate_average(numbers):
    try:
        sam = personal_sum(numbers)
        ret = sam[0] / sam[2]
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    else:
        return ret


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
