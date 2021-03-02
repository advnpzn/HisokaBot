from telegram.ext import Updater
import logging
from HisokaBot.helpers.constants import BOT_TOKEN


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
logger.info(msg="Logging started...")

updater = Updater(BOT_TOKEN)
dp = updater.dispatcher
