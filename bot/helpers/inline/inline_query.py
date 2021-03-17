from bot.helpers.search.results import Results
from telegram import Update
from telegram.ext import CallbackContext

def inlinequery(update: Update, _: CallbackContext) -> None:
    query = update.inline_query.query 
    if query == "":
        update.inline_query.answer(Results.DEFAULT_PIP)
    else:
        update.inline_query.answer(Results.search(query))