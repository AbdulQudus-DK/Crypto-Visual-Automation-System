# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB configuration
MONGODB_URI = os.getenv("MONGODB_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")

# Media and video settings
MEDIA_FOLDER = os.getenv("MEDIA_FOLDER", "media")
BACKGROUND_MUSIC = os.getenv("BACKGROUND_MUSIC", "background.mp3")
VIDEO_DURATION = int(os.getenv("VIDEO_DURATION", 10))

# Telegram configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
