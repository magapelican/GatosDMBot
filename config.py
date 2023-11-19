from os import getenv

from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("TOKEN")
ADMIN_IDS = getenv("ADMIN_IDS").split(":")
CHANNEL_ID = getenv("CHANNEL_ID")
