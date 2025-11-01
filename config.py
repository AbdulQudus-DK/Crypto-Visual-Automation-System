import os
from dotenv import load_dotenv

# Load environment variables from .env file (locally)
load_dotenv()

# Database
MONGODB_URI = os.getenv("MONGODB_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "CryptoDB")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME", "articles")

# Media and video
MEDIA_FOLDER = os.getenv("MEDIA_FOLDER", "media")
BACKGROUND_MUSIC = os.getenv("BACKGROUND_MUSIC", "assets/background.mp3")
VIDEO_DURATION = int(os.getenv("VIDEO_DURATION", 15))
