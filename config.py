# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20176556"))
API_HASH = getenv("API_HASH", "8136bd26f62a889221fc6d25cebe4e6a")
BOT_TOKEN = getenv("BOT_TOKEN", "7246880320:AAGPRcq_9Lr6x68Ytw1npiCVXthgVZjLg7w")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://akuspart:xswhARGUtukiR4bK@cluster0.dmxsf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
