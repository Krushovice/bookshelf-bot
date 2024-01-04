from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import F, Router
from bot.keyboards.markups import yes_no_kb, profile_kb
from bot.lexicon.lexicon_data import LEXICON_RU
from bot.database.orm import AsyncOrm


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)


@router.message(Command('help'))
async def command_help_handler(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(Command('profile'))
async def show_profile_handler(message: Message):
    await message.answer(text=LEXICON_RU['/profile'], reply_markup=profile_kb)


@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'])


@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])


@router.message(F.text == LEXICON_RU['wish_list'])
async def show_wish_list(message: Message):
    pass


@router.message(F.text == LEXICON_RU['check_list'])
async def show_check_list(message: Message):
    user_id = await AsyncOrm.select_reader_by_username(
            username=message.from_user.username
            )
    books = await AsyncOrm.select_books(user_id=user_id)
    msg = '\n'.join(books)
    await message.answer(text=msg)


@router.message(F.text == LEXICON_RU['category'])
async def show_category(message: Message):
    pass


@router.message(F.text)
async def process_save_answer(message: Message):
    msg = message.text.split(', ')
    if len(msg) < 5:
        await message.answer(text=LEXICON_RU['not_enough'])
    else:
        await AsyncOrm.insert_reader(first_name=message.from_user.first_name,
                                     last_name=message.from_user.last_name,
                                     username=message.from_user.username)

        user_id = await AsyncOrm.select_reader_by_username(
            username=message.from_user.username
            )
        await AsyncOrm.insert_books(reader_id=user_id,
                                    book_names=msg)

        await message.answer(text=LEXICON_RU['save_books'],
                             reply_markup=profile_kb)
