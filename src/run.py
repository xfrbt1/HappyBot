import asyncio
from aiogram import Bot
from aiogram.types import BotCommand

from src.dbrepo.dict_store import DictStore
from src.utils.message_for import message_for
from src.config.settings import get_settings
from src.handlers import dp


async def main() -> None:
    settings = get_settings()
    bot = Bot(token=settings.token)

    start_command = BotCommand(command="start", description="Старт")
    survey_command = BotCommand(command="survey", description="Опрос")
    db_command = BotCommand(command="db_state", description="DataBase")

    await bot.set_my_commands([start_command, survey_command, db_command])
    await message_for(bot, settings.admin_id, "✅BOT START WORK")
    await dp.start_polling(bot)
    await message_for(bot, settings.admin_id, "❎END OF WORK")


if __name__ == "__main__":
    asyncio.run(main())
