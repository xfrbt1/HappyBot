from aiogram.types import Message

from src.loader import dp


@dp.message()
async def common_text_handler(message: Message) -> None:
    await message.answer(text="Пройди опрос!")
