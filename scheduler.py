
from apscheduler.schedulers.background import BackgroundScheduler
from video_generator import generate_videos
from telegram_sender import send_videos_to_channel
from config import SCHEDULE_INTERVAL_HOURS

scheduler = BackgroundScheduler()

def scheduled_job():
    print("🕒 Running scheduled job...")
    videos = generate_videos()
    if videos:
        send_videos_to_channel(videos)
    else:
        print("⚠️ No new videos generated this round.")

def start_scheduler():
    scheduler.add_job(
        scheduled_job,
        "interval",
        hours=SCHEDULE_INTERVAL_HOURS,
        id="video_job",
        replace_existing=True
    )
    scheduler.start()
