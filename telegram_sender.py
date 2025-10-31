# telegram_sender.py
import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID

def send_videos_to_channel(video_paths):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendVideo"

    for path in video_paths:
        with open(path, "rb") as video:
            response = requests.post(url, data={"chat_id": TELEGRAM_CHANNEL_ID}, files={"video": video})
            if response.status_code == 200:
                print(f"🎬 Sent: {path}")
            else:
                print(f"⚠️ Failed to send {path}: {response.text}")
