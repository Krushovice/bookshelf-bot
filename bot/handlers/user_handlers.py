from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import F, Router
from bot.keyboards.markups import yes_no_kb, profile_kb
from bot.lexicon.lexicon_data import LEXICON_RU


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


@router.message(F.text)
async def process_save_answer(message: Message):
    msg = message.text.split(', ')
    if len(msg) < 5:
        await message.answer(text=LEXICON_RU['not_enough'])
    else:
        await message.answer(text=LEXICON_RU['save_books'],
                             reply_markup=profile_kb)


@router.message(F.text == LEXICON_RU['wish_list'])
async def show_wish_list(message: Message):
    pass


@router.message(F.text == LEXICON_RU['check_list'])
async def show_check_list(message: Message):
    pass


@router.message(F.text == LEXICON_RU['category'])
async def show_category(message: Message):
    pass
