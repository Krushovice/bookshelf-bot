import asyncio
import logging
import sys
from bot.config_data.config_reader import settings

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from bot.handlers import user_handlers
from bot.database.orm import AsyncOrm

# Bot token can be obtained via https://t.me/BotFather
logger = logging.getLogger(__name__)


async def main() -> None:
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # proxy_url = settings.proxy_url
    # connector = TCPConnector(ssl=False)
    # session = ClientSession(connector=connector, trust_env=True, url=proxy_url)

    dp = Dispatcher()
    bot = Bot(token=settings.bot_token,
              parse_mode=ParseMode.HTML)
    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    # dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await AsyncOrm.create_tables()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        stream=sys.stdout)
    asyncio.run(main())
