from aiogram.types import InlineQuery, InputMediaVideo, InlineQueryResultArticle, InputTextMessageContent
from loader import dp
from utils.yt_vid_get import video_from_yt


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
