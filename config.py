import os


class Config(object):
    API_HASH = os.environ.get("38c131498b9cdeacde8f1f763d466840")
    BOT_TOKEN = os.environ.get("7134410001:AAH3yecgCvxiCm5JpZs76iLBeU1OW12X1TE")
    TELEGRAM_API = os.environ["28361260"]
    OWNER = os.environ.get("5845177357")
    OWNER_USERNAME = os.environ.get("killerboy098")
    PASSWORD = os.environ.get("hello")
    LOGCHANNEL = os.environ.get("-1002068157366")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
