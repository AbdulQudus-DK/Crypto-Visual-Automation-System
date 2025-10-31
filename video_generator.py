
import os
import random
import requests
from PIL import Image, ImageDraw, ImageFont
from pymongo import MongoClient
from newspaper import Article
from moviepy.editor import ImageClip, AudioFileClip
from config import (
    MONGODB_URI,
    MONGO_DB_NAME,
    MONGO_COLLECTION_NAME,
    MEDIA_FOLDER,
    BACKGROUND_MUSIC,
    VIDEO_DURATION
)

def generate_videos():
    os.makedirs(MEDIA_FOLDER, exist_ok=True)

    client = MongoClient(MONGODB_URI)
    db = client[MONGO_DB_NAME]
    collection = db[MONGO_COLLECTION_NAME]

    items = list(collection.find().limit(10))
    if not items:
        print("⚠️ No items found.")
        return []

    selected_items = random.sample(items, min(5, len(items)))
    created_videos = []

    bg_music_path = BACKGROUND_MUSIC if os.path.exists(BACKGROUND_MUSIC) else None

    for idx, item in enumerate(selected_items):
        title = item.get("title", "Untitled")
        link = item.get("link")
        video_path = f"{MEDIA_FOLDER}/video_{idx}.mp4"

        # Skip if already created
        if os.path.exists(video_path):
            print(f"⏩ Skipping duplicate video: {title}")
            continue

        try:
            # Extract image
            article = Article(link)
            article.download()
            article.parse()
            image_url = article.top_image
            if not image_url:
                continue

            img_data = requests.get(image_url, timeout=10).content
            image_path = f"{MEDIA_FOLDER}/image_{idx}.jpg"
            with open(image_path, "wb") as f:
                f.write(img_data)

            # Add caption
            img = Image.open(image_path).convert("RGB")
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("arial.ttf", 40)

            caption = title[:120]
            text_w, text_h = draw.textsize(caption, font=font)
            draw.rectangle(
                [(0, img.height - text_h - 80), (img.width, img.height)],
                fill=(0, 0, 0)
            )
            draw.text(
                ((img.width - text_w) / 2, img.height - text_h - 40),
                caption,
                fill="white",
                font=font
            )

            captioned_path = f"{MEDIA_FOLDER}/captioned_{idx}.jpg"
            img.save(captioned_path)

            # Create video
            image_clip = ImageClip(captioned_path).set_duration(VIDEO_DURATION)
            if bg_music_path:
                audio_clip = AudioFileClip(bg_music_path).subclip(0, VIDEO_DURATION)
                image_clip = image_clip.set_audio(audio_clip)

            image_clip.write_videofile(
                video_path,
                fps=24,
                codec="libx264",
                audio_codec="aac",
                verbose=False
            )

            created_videos.append(video_path)

        except Exception as e:
            print(f"❌ Error creating video for '{title}': {e}")

    print("✅ Video generation complete.")
    return created_videos
