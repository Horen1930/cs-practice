def count_items(values):
    d = {}

    for key in values:
        if key in d:
            d[key] += 1
        else:
            d[key] = 1

    return d

print(count_items(["ошибка", "запуск", "ошибка", "проверка"]))
