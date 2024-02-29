from aiogram.types import Message

from src.loader import dp


@dp.message()
async def common_text_handler(message: Message) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    await message.answer(f"{message.text}")
