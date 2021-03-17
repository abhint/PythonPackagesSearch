#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler, InlineQueryHandler
from bot.helpers.commands.cmd import start, help_command
from bot.helpers.inline.inline_query import inlinequery
from bot import Config

def main() -> None:
    updater = Updater(Config.BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(InlineQueryHandler(inlinequery))
    if Config.ENV:
        updater.start_webhook(
            listen="0.0.0.0",
            port=Config.WEBHOOK_PORT,
            url_path=Config.BOT_TOKEN
        )
        updater.bot.set_webhook(url=Config.WEBHOOK_URL + Config.BOT_TOKEN)
    else:
        updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
