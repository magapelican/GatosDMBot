from aiogram.filters import BaseFilter
from aiogram.types import Message

import config


class IsAdminFilter(BaseFilter):

    async def __call__(self, message: Message) -> bool:
        return str(message.from_user.id) in config.ADMIN_IDS
