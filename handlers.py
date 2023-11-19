from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import config
from filters import IsAdminFilter
from keyboards import get_post_or_not_kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Salam, vac!")




@router.message(F.photo, ~IsAdminFilter())
async def send_on_message(message: Message, bot: Bot):
    global sender_id 
    sender_id = message.from_user.id

    photo_id = message.photo[-1].file_id  # message.photo[-1] to get pic of biggest size
    user_name = message.from_user.first_name
    for admin_id in config.ADMIN_IDS:
        await bot.send_photo(
            chat_id=admin_id, photo=photo_id,
            reply_markup=get_post_or_not_kb(),
            caption="Sent by " + user_name
        )
        #await bot.send_message(admin_id, "Sent by " + user_name)


@router.callback_query(F.data == "post_img")
async def post_img_to_channel(callback: CallbackQuery):
    await callback.message.answer("i work")
    await callback.answer()


@router.callback_query(F.data == "do_not_post_img")
async def dont_post_img_to_channel(callback: CallbackQuery, bot: Bot):
    await bot.send_message(sender_id, "Админу не понравилась твоя публикация((")
    await callback.message.delete()
