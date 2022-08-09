from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from utils.pic_for_help import get_info_pic
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer_photo(photo=get_info_pic(), caption="Инлайн бот для поиска, возвращающий ссылку на видео в ютуб.")
