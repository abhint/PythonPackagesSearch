from uuid import uuid4
from bot.helpers.search.pypi import default_pip, pip_search
from telegram import (
    InlineQueryResultArticle,
    ParseMode,
    InputTextMessageContent,
    ParseMode
)


class Results():
    DEFAULT_PIP = []
    package, description, link = default_pip()
    for i in range(len(package)):
        DEFAULT_PIP.append(
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=package[i],
                description=description[i],
                input_message_content=InputTextMessageContent(
                    f'Name: {package[i]} \nDescription: {description[i]} \nURL: {link[i]}',
                    parse_mode=ParseMode.HTML
                ),
                thumb_url="https://pypi.org/static/images/logo-small.png",
                thumb_width=100,
                thumb_height=88
            ))
    def search(query):
        PIP_SEARCH = []
        package, description, link = pip_search(query)
        for i in range(len(package)):
            PIP_SEARCH.append(
                InlineQueryResultArticle(
                    id=str(uuid4()),
                    title=package[i],
                    description=description[i],
                    input_message_content=InputTextMessageContent(
                        f'Name: {package[i]} \nDescription: {description[i]} \nURL: {link[i]}',
                        parse_mode=ParseMode.HTML
                    ),
                    thumb_url="https://pypi.org/static/images/logo-small.png",
                    thumb_width=100,
                    thumb_height=88
                ))
        return PIP_SEARCH