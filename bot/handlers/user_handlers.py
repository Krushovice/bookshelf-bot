from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import F, Router
from bot.keyboards.markups import yes_no_kb, profile_kb
from bot.lexicon.lexicon_data import LEXICON_RU
from bot.database.orm import AsyncOrm
from bot.utils.search import get_book_info


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


@router.message(F.text == LEXICON_RU['list_readers'])
async def show_category(message: Message):
    readers = await AsyncOrm.select_readers_by_selectin()

    response = ""
    for reader in readers:
        response += f"{reader.username}:\n"
        for book in reader.books:
            response += f"- {book.name}\n"
        response += "\n"

    await message.answer(text=response)


# @router.message(F.text == LEXICON_RU['recomendize'])
# async def recomend_book(message: Message):
#     user_id = await AsyncOrm.select_reader_by_username(
#         username=message.from_user.username
#         )
#     books = await AsyncOrm.select_books(user_id=user_id)

#     msg = LEXICON_RU['recomendize'] + ':' + ', '.join(books)
#     answer = await generate_openai(msg)

#     if answer:
#         await message.reply(answer)
#     else:
#         await message.answer(text=LEXICON_RU['other_answer'])


@router.message(F.text)
async def process_save_answer(message: Message):
    msg = message.text.split(', ')
    if len(msg) == 1:
        await AsyncOrm.insert_reader(first_name=message.from_user.first_name,
                                     last_name=message.from_user.last_name,
                                     username=message.from_user.username)

        user_id = await AsyncOrm.select_reader_by_username(
            username=message.from_user.username
            )

        for name in msg:
            book_info = get_book_info(name)
            await AsyncOrm.insert_book(reader_id=user_id,
                                       book_info=book_info
                                       )

        # # await AsyncOrm.insert_books(reader_id=user_id,
        # #                             book_list=book_list
        #                             )

        await message.answer(text=LEXICON_RU['save_books'],
                             reply_markup=profile_kb)


# @router.message(F.text)
# async def recomend_book(message: Message):
#     # user_id = await AsyncOrm.select_reader_by_username(
#     #     username=message.from_user.username
#     #     )
#     # books = await AsyncOrm.select_books(user_id=user_id)

#     answer = await generate_ai(message.text)

#     if answer:
#         await message.reply(answer.content)
#     else:
#         await message.answer(text=LEXICON_RU['other_answer'])
