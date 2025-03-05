import os
import sys
import json
import datetime
import subprocess

try:
    from googleapiclient.discovery import build
except ModuleNotFoundError:
    print("Error: googleapiclient is not installed. Install it using: pip install google-api-python-client")
    sys.exit(1)

# Set up YouTube API
API_KEY = "API-KEY"  # Replace with your actual API key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
PROD2_CHANNEL_ID = "UCu98ro1AIOu-4wtZxDRS6Tg"
OUTPUT_DIR = "/content/downloaded_videos"

def get_prod2_resumes():
    """Fetch the latest PROD2 résumé videos from YouTube."""
    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    except Exception as e:
        print(f"Error initializing YouTube API: {e}")
        sys.exit(1)

    published_after = (datetime.datetime.utcnow() - datetime.timedelta(days=14)).isoformat("T") + "Z"

    try:
        request = youtube.search().list(
            channelId=PROD2_CHANNEL_ID,
            part="snippet",
            maxResults=10,
            publishedAfter=published_after,
            type="video",
            order="date"
        )
        response = request.execute()
    except Exception as e:
        print(f"Error fetching video data: {e}")
        sys.exit(1)

    videos = []
    for item in response.get("items", []):
        video_title = item["snippet"]["title"]
        if "J22" in video_title:  # Only select résumé videos
            video_data = {
                "title": video_title,
                "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                "published_at": item["snippet"]["publishedAt"]
            }
            videos.append(video_data)

    if not videos:
        print("No 'Résumé' videos found. Consider adjusting the search filter.")

    return videos

def download_videos(video_urls):
    """Downloads videos using yt-dlp."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    downloaded_files = []

    for url in video_urls:
        print(f"Downloading: {url}")
        output_path = os.path.join(OUTPUT_DIR, "%(title)s.%(ext)s")
        command = ["yt-dlp", "-f", "bestvideo+bestaudio", "--merge-output-format", "mp4", "-o", output_path, url]

        try:
            subprocess.run(command, check=True)
            downloaded_files.append(output_path.replace("%(title)s", ""))
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {url}: {e}")

    return downloaded_files

def merge_videos(video_files, output_filename="merged_video.mp4"):
    """Merges videos using ffmpeg."""
    if not video_files:
        print("No videos to merge.")
        return

    merge_list_path = os.path.join(OUTPUT_DIR, "merge_list.txt")

    with open(merge_list_path, "w") as f:
        for video in video_files:
            f.write(f"file '{video}'\n")

    output_path = os.path.join(OUTPUT_DIR, output_filename)

    merge_command = ["ffmpeg", "-f", "concat", "-safe", "0", "-i", merge_list_path, "-c", "copy", output_path]

    try:
        subprocess.run(merge_command, check=True)
        print(f"Merged video saved as: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error merging videos: {e}")

if __name__ == "__main__":
    prod2_videos = get_prod2_resumes()

    video_urls = [video["url"] for video in prod2_videos]
    downloaded_files = download_videos(video_urls)

    merge_videos(downloaded_files)
