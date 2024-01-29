from aiogram.types import Message
from aiogram import F, Router
from bot.keyboards.reply_keyboard import yes_no_kb, profile_kb
from bot.lexicon.lexicon_data import LEXICON_RU
from bot.core.models.orm import AsyncOrm
from bot.utils.search import get_book_info
from bot.utils.ai_engine import generate_ai


router = Router(name=__name__)


@router.message(F.text == LEXICON_RU["yes_button"])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU["yes"])


@router.message(F.text == LEXICON_RU["no_button"])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU["no"])


@router.message(F.text)
async def recomend_book(message: Message):
    # user_id = await AsyncOrm.select_reader_by_username(
    #     username=message.from_user.username
    #     )
    # books = await AsyncOrm.select_books(user_id=user_id)

    answer = await generate_ai(message.text)

    if answer:
        await message.reply(answer)
    else:
        await message.answer(text=LEXICON_RU["other_answer"])
