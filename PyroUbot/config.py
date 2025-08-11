import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "Id Lu").split()))

API_ID = int(os.getenv("API_ID", "Api id Lu"))

API_HASH = os.getenv("API_HASH", "Api Hash Lu")

BOT_TOKEN = os.getenv("BOT_TOKEN", "Bot Token Lu")

OWNER_ID = int(os.getenv("OWNER_ID", "Owner Id Lu"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "a6q")

MONGO_URL = os.getenv("MONGO_URL", "mongodb lu")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "id Gb / ch lu."))
