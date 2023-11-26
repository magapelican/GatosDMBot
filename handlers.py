from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import config
import database
from filters import IsAdminFilter
from keyboards import get_post_or_not_kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Salam, vac!")


@router.message(F.photo, ~IsAdminFilter())
async def on_pic_send_to_admins(message: Message, bot: Bot):
    photo_id = message.photo[-1].file_id  # message.photo[-1] to get pic of biggest size
    full_name = message.from_user.first_name + " " + message.from_user.last_name
    username = "@" + message.from_user.username
    caption = f"Sent by {full_name} {username}"

    for admin_id in config.ADMIN_IDS:
        await bot.send_photo(
            chat_id=admin_id, photo=photo_id,
            reply_markup=get_post_or_not_kb(message.message_id, message.from_user.id),
            caption=caption
        )

    params = (message.message_id, photo_id)
    database.save_user_data(params)


@router.callback_query(F.data.startswith("post_img"))
async def post_img_to_channel(callback: CallbackQuery, bot: Bot):
    msg_id = callback.data.split("_")[-1]
    await bot.send_photo(config.CHANNEL_ID, database.get_file_id(int(msg_id)))
    database.delete_user_data(int(msg_id))
    await callback.message.delete()


@router.callback_query(F.data.startswith("do_not_post_img"))
async def dont_post_img_to_channel(callback: CallbackQuery, bot: Bot):
    msg_id = callback.data.split("_")[-1]
    sender_id = callback.data.split("_")[-2]
    await bot.send_message(sender_id, "Админу не понравилась твоя публикация((")
    await callback.message.delete()
    database.delete_user_data(int(msg_id))
