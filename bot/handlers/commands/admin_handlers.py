from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import Router
from bot.keyboards  import yes_no_kb, profile_kb
from bot.lexicon.lexicon_data import LEXICON_RU
from bot.core.models  import AsyncOrm

# from bot.utils.search import get_book_info


router = Router(name=__name__)
