import logging
from uuid import uuid4
from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Hi!')


def help_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Help!')