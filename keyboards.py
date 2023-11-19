from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_post_or_not_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="✅", callback_data="post_img"),
        InlineKeyboardButton(text="❌", callback_data="do_not_post_img")
    )
    return builder.as_markup()
