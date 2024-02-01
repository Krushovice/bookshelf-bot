from aiogram.types import (ReplyKeyboardMarkup,
                           ReplyKeyboardRemove,
                           KeyboardButton)


rmk = ReplyKeyboardRemove()


class ButtonText():
    PROFILE = "Профиль"
    ADD_BOOK = "Добавить книгу"
    RECOMENDIZE = "Новая рекомендация"
    CHECK_LIST = "Список прочитанного 📜"
    CATEGORIES = "Желаемые книги 🙏"
    WISH_LIST = "Любимые категории 📊"


def get_on_start_kb():
    button_profile = KeyboardButton(text=ButtonText.PROFILE)
    button_add = KeyboardButton(text=ButtonText.ADD_BOOK)
    button_recomend = KeyboardButton(text=ButtonText.RECOMENDIZE)
    markup = ReplyKeyboardMarkup(
        keyboard=[[button_profile],
                  [button_add],
                  [button_recomend],
                  ],
        resize_keyboard=True,
    )
    return markup


def get_profile_kb():
    button_check_list = KeyboardButton(text=ButtonText.CHECK_LIST)
    button_category = KeyboardButton(text=ButtonText.CATEGORIES)
    button_wish_list = KeyboardButton(text=ButtonText.WISH_LIST)

    markup = ReplyKeyboardMarkup(
        keyboard=[[button_check_list],
                  [button_category],
                  [button_wish_list],
                  ],
        resize_keyboard=True,
    )
    return markup
