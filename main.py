import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers import user
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode



async def main() -> None:
    config: Config = load_config()

    logging.basicConfig(
        level = config.log.level,
        format = config.log.format
    )

    bot = Bot(token = config.bot.token,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(user.router)

    await bot.delete_webhook(drop_pending_updates = True) # clears all previous updates
    await dp.start_polling(bot)

asyncio.run(main())