from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from bot.keyboards import register_profile, rmk
from bot.utils.states import Form
from bot.utils.choice_helper import books, genres, choice_items
from bot.lexicon.lexicon_data import LEXICON_RU


router = Router(name=__name__)


@router.message(Command("register"))
async def register_user_handler(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU["/register"])
    await state.set_state(Form.username)
    await message.answer(
        text=LEXICON_RU['ask_username'],
        reply_markup=register_profile(message.from_user.username)
    )


@router.message(Form.username)
async def form_username(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(Form.books)
    await message.answer(LEXICON_RU['ask_books'],
                         reply_markup=register_profile(choice_items(books)))


@router.message(Form.books)
async def form_books(message: Message, state: FSMContext):
    books = list(message.text)
    if len(books) > 1:
        await state.update_data(books=message.text.split(', '))
        await state.set_state(Form.genre)
        await message.answer(LEXICON_RU['ask_genre'],
                             reply_markup=register_profile(
                                 choice_items(genres)
                                 )
                             )
    else:
        await message.answer(LEXICON_RU['not_list'])


@router.message(Form.genre)
async def form_genre(message: Message, state: FSMContext):
    if message.text.isalpha():
        await state.update_data(genre=message.text)
        data = await state.get_data()
        await state.clear()

        print(data)  # Тут должна быть работа с БД
        await message.answer(LEXICON_RU['success'], reply_markup=rmk)

    else:
        message.answer("Введите пожалуйста любимый жанр")
