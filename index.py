import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

import config
from handlers import router
from is_user_admin import IsAdminFilter

bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(F.photo, ~IsAdminFilter(config.ADMIN_ID))
async def send_on_message(message: Message):
    photo_id = message.photo[2].file_id
    user_name = message.from_user.first_name
    await bot.send_photo(chat_id=config.ADMIN_ID, photo=photo_id)
    await bot.send_message(config.ADMIN_ID, "Sent by " + user_name)
    # await bot.send_photo(config.ADMIN_ID, img)


async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
