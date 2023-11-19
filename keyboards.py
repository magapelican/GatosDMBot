from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_post_or_not_kb(msg_id, sender_id) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="✅", callback_data=f"post_img_{msg_id}"),
        InlineKeyboardButton(text="❌", callback_data=f"do_not_post_img_{sender_id}_{msg_id}")
    )
    return builder.as_markup()
