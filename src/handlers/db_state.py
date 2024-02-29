from aiogram import types
from aiogram.filters import Command
from aiogram.types import FSInputFile

from src.config.settings import get_settings
from src.config.config import decode_approach
from src.loader import dp, db
from src.utils.utils import create_plot_picture


@dp.message(Command("db_state"))
async def db_state_command(message: types.Message):

    settings = get_settings()
    filename = settings.diagram
    user_id = str(message.from_user.id)
    admins_ids_list = settings.admin_id.split()

    if user_id in admins_ids_list:
        await message.answer(
            f"current data base state\n"
            f"_______________________\n"
            f"rows: {len(db)}\n"
            f"_______________________\n"
            f"{str(db)}"
        )
        count = create_plot_picture(db, decode_approach, filename)
        caption = f"counter:\n{str(count)}\n\ndecode:\n{str(decode_approach)}"
        input_file = FSInputFile(filename)
        await message.answer_photo(photo=input_file, caption=caption)

    else:
        await message.answer(f"no permission")
