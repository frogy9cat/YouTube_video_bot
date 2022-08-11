from aiogram.types import InlineQuery, InputMediaVideo, InlineQueryResultArticle, InputTextMessageContent
from aiogram import types
from loader import dp
from utils.yt_vid_get import video_from_yt
from aiogram.dispatcher.filters.builtin import Text
from io import BytesIO
from pytube import YouTube


@dp.inline_handler()
async def inline_video_search(inline_query: InlineQuery):
    text = inline_query.query
    result = video_from_yt(text)
    items=[]
    if result:
        for i, re in enumerate(result):
            item = InlineQueryResultArticle(
            id=i,
            title=re['title'],
            description=(f"{re['channel']}\n{re['views']}"),
            thumb_url=re["image"],
            input_message_content=InputTextMessageContent(f"{re['url']}"),
            )
            items.append(item)
    if items:
        await inline_query.answer(results=items, cache_time=1)



@dp.message_handler(Text(startswith="http")) 
async def get_video(message:types.Message):
    await message.answer("Видео загружается...")
    link=message.text  
    buffer=BytesIO() 
    url=YouTube (link) 
    if url.check_availability() is None:
        video=url.streams.get_highest_resolution()
        video.stream_to_buffer(buffer=buffer) 
        buffer.seek(0) 
        filename=url.title
        await message.reply_video(video=buffer, caption=f"{filename}\n@python_b_end") 
    else:
        await message.answer("Неверный формат ссылки.")