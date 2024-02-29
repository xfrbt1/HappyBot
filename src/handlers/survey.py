from aiogram import types
from aiogram.filters import Command
from aiogram.types import CallbackQuery

from src.loader import dp, db
from src.config.config import age_groups_list, approach_list, approach_dict
from src.keyboards.inline import abstract_keyboard
from src.utils.utils import approach_text


@dp.message(Command("survey"))
async def survey_command(message: types.Message):
    text = "Выбери возрастную группу: "
    await message.answer(text=text, reply_markup=abstract_keyboard(age_groups_list))


@dp.callback_query(lambda call: call.data in age_groups_list)
async def age_group_handler(call: CallbackQuery):
    user_id = call.from_user.id
    db.update(str(user_id), age_group=str(call.data))
    text = "Выбери подход, который находишь самым привлекательным:\n\n{}"
    await call.message.edit_text(
        text=text.format(approach_text(approach_dict)),
        reply_markup=abstract_keyboard(approach_list),
    )


@dp.callback_query(lambda call: call.data in approach_list)
async def approach_id_handler(call: CallbackQuery):
    user_id = call.from_user.id
    db.update(str(user_id), approach_id=str(call.data))
    await call.message.edit_text("Спасибо за прохождение опроса!")
