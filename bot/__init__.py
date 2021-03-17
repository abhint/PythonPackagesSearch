import os
import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


class Config:
    ENV = bool(os.environ.get('ENV', False))
    try:
        if ENV:
            BOT_TOKEN = os.environ.get("BOT_TOKEN")
            WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
            WEBHOOK_PORT = int(os.environ.get("PORT"))
            logger.info(f"BOT START WITH WEBHOOK\nURL: {WEBHOOK_URL}\nPORT: {WEBHOOK_PORT}")
        else:
            from local_server import Bot
            BOT_TOKEN = Bot.TOKEN
            logger.info("BOT START LOCAL SERVER CONFIG")
    except OSError as error:
        print(error)
