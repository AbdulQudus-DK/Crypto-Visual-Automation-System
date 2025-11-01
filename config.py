import os
from dotenv import load_dotenv

# Load .env file (for local development)
load_dotenv()

# MongoDB Config
MONGODB_URI = os.getenv("MONGODB_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "crypto_db")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME", "articles")

# Telegram Config
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

# Video Generation Config
MEDIA_FOLDER = os.getenv("MEDIA_FOLDER", "media")
BACKGROUND_MUSIC = os.getenv("BACKGROUND_MUSIC", "background.mp3")
VIDEO_DURATION = int(os.getenv("VIDEO_DURATION", 30))

# Scheduler Config
SCHEDULE_INTERVAL_HOURS = int(os.getenv("SCHEDULE_INTERVAL_HOURS", 2))
