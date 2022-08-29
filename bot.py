import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram


if __name__ == "__main__" :
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "RenameBot",
#         bot_token=Config.TG_BOT_TOKEN,
#         api_id=Config.APP_ID,
#         api_hash=Config.API_HASH,
        bot_token= "5594793092:AAGM82wZFn43aiU5ceWrFvhFvS4V3XjGkwI" ,
        api_id= int(13003049),
        api_hash= "5c37465fe653a28519bb8b9b68269f5f",
        plugins=plugins
    )
    Config.AUTH_USERS.add(1378380156)
    app.run()
