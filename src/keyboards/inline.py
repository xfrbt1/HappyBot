from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardMarkup,
)


def abstract_keyboard(buttons_list: list[str], rows: int = 1) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    [
        builder.button(text=button_txt, callback_data=button_txt)
        for button_txt in buttons_list
    ]
    builder.adjust(rows)
    return InlineKeyboardMarkup(inline_keyboard=builder.export())
