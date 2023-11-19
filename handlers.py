import requests
import os
import io
#from PIL import Image # пока не скачал библиотеку

from config import URI_INFO, URI

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

#CommandHandler
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Salam, vac!")