import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "8100453801").split()))

API_ID = int(os.getenv("API_ID", "26977496"))

API_HASH = os.getenv("API_HASH", "8b3fac53ddf21c187ca0b6f9047a5bec)

BOT_TOKEN = os.getenv("BOT_TOKEN", "7742635862:AAGxHmiD946LcOcLsSTei-Yi-l620GKPuuw")

OWNER_ID = int(os.getenv("OWNER_ID", "8100453801"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "a6q")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ajaybabu69f:XF0vwerJ7QuyYJGS@cluster0.1vop5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002500826609"))
