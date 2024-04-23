def getHatCats(num_cats, num_rounds):
    # Инициализация массива, где каждый элемент представляет кошку.
    # Значение False означает, что на кошке нет шапки.
    hats = [False] * num_cats

    # Проходим по каждому кругу
    for i in range(1, num_rounds + 1):
        # На каждом i-ом круге переключаем состояние шапки на каждой i-ой кошке
        for j in range(i - 1, num_cats, i):
            hats[j] = not hats[j]

    # Формирование списка индексов кошек, у которых остались шапки
    hatted_cats = [index + 1 for index, has_hat in enumerate(hats) if has_hat]
    return hatted_cats

# Тестирование функции с 100 кошками и 100 кругами
hatted_cats = getHatCats(100, 100)
print("Cats with hats:", hatted_cats)

