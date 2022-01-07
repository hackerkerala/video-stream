import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "dlwrml")
ALIVE_NAME = getenv("ALIVE_NAME", "Levina")
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
BOT_USERNAME = getenv("BOT_USERNAME", "veezvideobot")
MONGO_DB_URI = getenv("MONGO_DB_URI")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cleo_invida")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VeezSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/005de39b81113102c30d7.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ALBINPRAVEEN/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/182aebbf0843de559b78c.mp4")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/1dfad3ba0e793d656bb54.mp4")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f0ea7df065866e3e158b1.mp4")
