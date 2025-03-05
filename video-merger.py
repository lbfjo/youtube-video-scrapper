import os
import subprocess

# Path where your downloaded videos are stored
VIDEO_DIR = "/content/downloaded_videos"
OUTPUT_FILE = "/content/merged_video.mp4"

def create_merge_list(video_dir):
    """Creates a list of video files to merge."""
    video_files = sorted([f for f in os.listdir(video_dir) if f.endswith(".mp4")])

    if not video_files:
        print("No MP4 files found in the directory!")
        return None

    merge_list_path = os.path.join(video_dir, "merge_list.txt")

    with open(merge_list_path, "w") as f:
        for video in video_files:
            f.write(f"file '{os.path.join(video_dir, video)}'\n")

    return merge_list_path

def merge_videos(merge_list_path, output_path):
    """Merges videos using FFmpeg."""
    if merge_list_path is None:
        print("No videos to merge.")
        return

    merge_command = ["ffmpeg", "-f", "concat", "-safe", "0", "-i", merge_list_path, "-c", "copy", output_path]

    try:
        subprocess.run(merge_command, check=True)
        print(f"✅ Merged video saved as: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error merging videos: {e}")

# Run the merging process
merge_list = create_merge_list(VIDEO_DIR)
merge_videos(merge_list, OUTPUT_FILE)
