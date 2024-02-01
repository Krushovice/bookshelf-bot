import random


books = ['Война и мир', 'Идиот', 'Мастер и маргарита', '1984',
         'Маленький принц', 'Властелин колец', 'Десять негритят',
         'По ком звонит колокол', 'Три товарища', 'Унесенные ветром']

genres = ['Ужасы', 'Драма', 'Роман',
          'Фэнтези', 'Научная фантастика',
          'Проза', 'Фантастика', 'Новелла',
          'Рассказ', 'Биография', 'Автобиография']


def choice_items(items: list) -> list:
    result = []
    for _ in range(4):
        item = random.choice(items)
        if item not in result:
            result.append(item)
    return result
