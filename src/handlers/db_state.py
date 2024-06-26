from aiogram import types
from aiogram.filters import Command
from aiogram.types import FSInputFile

from src.config.settings import get_settings
from src.config.config import decode_approach
from src.loader import dp, db
from src.utils.utils import create_plot_picture, get_entire_count


@dp.message(Command("db_state"))
async def db_state_command(message: types.Message):
    settings = get_settings()
    filepath = settings.data_path + settings.diagram
    user_id = str(message.from_user.id)
    admins_ids_list = settings.admin_id.split()

    if user_id in admins_ids_list:
        text: str = f"current data base state\n" f"rows: {len(db)}\n" f"{str(db)}\n"
        counter: dict = create_plot_picture(db, decode_approach, filepath)
        all_polls: int = get_entire_count(counter)
        input_file = FSInputFile(filepath)
        caption: str = (
            f"polls:\n{str(all_polls)}\n\n"
            f"counter:\n{str(counter)}\n\n"
            f"decode:\n{str(decode_approach)}\n\n"
        )
        await message.answer_photo(photo=input_file, caption=text+caption)

    else:
        await message.answer(f"no permission")
