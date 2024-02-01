from aiogram.types import Message
from aiogram import F, Router
from bot.keyboards import get_profile_kb, get_on_start_kb
from bot.lexicon.lexicon_data import LEXICON_RU
# from bot.core import AsyncOrm
# from bot.utils import get_book_info
# from bot.utils import generate_ai


router = Router(name=__name__)


# @router.message(F.text == LEXICON_RU["wish_list"])
# async def show_wish_list(message: Message):
#     pass


# @router.message(F.text == LEXICON_RU["check_list"])
# async def show_check_list(message: Message):
#     user_id = await AsyncOrm.select_reader_by_username(
#         username=message.from_user.username
#     )
#     books = await AsyncOrm.select_books(user_id=user_id)
#     msg = "\n".join(books)
#     await message.answer(text=msg)


# @router.message(F.text == LEXICON_RU["list_readers"])
# async def show_category(message: Message):
#     readers = await AsyncOrm.select_readers_by_selectin()

#     response = ""
#     for reader in readers:
#         response += f"{reader.username}:\n"
#         for book in reader.books:
#             response += f"- {book.name}\n"
#         response += "\n"

#     await message.answer(text=response)

# @router.message(Command("add_book"))
# async def command_add_book_handler(message: Message):
#     await message.answer(text=LEXICON_RU["/add_book"])


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
