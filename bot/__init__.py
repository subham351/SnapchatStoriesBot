import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID","29329572"))
    API_HASH = os.environ.get("API_HASH","b5d7c5d840ce6cd794c1754af5276bac")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5946687137:AAHMwOvlYwKY2vc3r5F0oax0kuZS-RV6WIM")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","Tc_Lottery_Group_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
