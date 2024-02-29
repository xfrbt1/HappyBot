import logging

from aiogram import Bot


async def message_for(bot: Bot, chat_id: str, text: str = "event"):
    try:
        await bot.send_message(chat_id=chat_id, text=text)
    except Exception as error:
        logging.exception(error)
