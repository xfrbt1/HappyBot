from aiogram import types
from aiogram.filters import CommandStart


from src.loader import dp, db


@dp.message(CommandStart())
async def start_command(
    message: types.Message,
):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    db.create(str(user_id), username=username, full_name=full_name)
    await message.answer(f"Привет, {full_name}!\n" f"Пройти опрос:\n" f"/survey")
