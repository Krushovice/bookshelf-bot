from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.lexicon.lexicon_data import LEXICON_RU


# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# Создаем кнопки навигации профиля
button_1 = KeyboardButton(text=LEXICON_RU['check_list'])
button_2 = KeyboardButton(text=LEXICON_RU['category'])
button_3 = KeyboardButton(text=LEXICON_RU['wish_list'])
button_4 = KeyboardButton(text=LEXICON_RU['list_readers'])
button_5 = KeyboardButton(text=LEXICON_RU['recomendize'])


profile_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1],
              [button_2],
              [button_3],
              [button_4],
              [button_5]],
    resize_keyboard=True,
    one_time_keyboard=True
)
