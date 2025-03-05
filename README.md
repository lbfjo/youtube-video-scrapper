# PROD2 Video Merger

## 📌 Overview
This Python script fetches and merges the latest **PROD2 rugby résumé videos** from YouTube, allowing easy access to all match highlights in a single video file.

## 🚀 Features
- **Fetches videos** from the official PROD2 YouTube channel
- **Filters only résumé videos** (excluding "Zapping" and "Top Essais")
- **Downloads the videos** using `yt-dlp`
- **Merges them into a single video** using `FFmpeg`
- **Saves the final video** for easy access

## 🛠️ Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YourUsername/prod2-video-merger.git
cd prod2-video-merger
```

### 2️⃣ Install Dependencies
```bash
pip install yt-dlp google-api-python-client
sudo apt-get install ffmpeg  # Linux/macOS (For Windows, install from https://ffmpeg.org/)
```

## 🔧 Usage
### 1️⃣ Set Up YouTube API
1. Get a **YouTube Data API v3** key from [Google Cloud Console](https://console.cloud.google.com/)
2. Replace `YOUR_YOUTUBE_API_KEY` in `script.py` with your actual API key

### 2️⃣ Run the Script
```bash
python script.py
```

The script will:
- Fetch résumé videos from PROD2 YouTube channel
- Download them using `yt-dlp`
- Merge them using `FFmpeg`
- Save the final merged video as `merged_video.mp4`

## 📂 Output
- Merged video saved as `merged_video.mp4`
- JSON file `prod2_resumes.json` containing fetched video metadata

## 🏗️ Roadmap
- Add support for different leagues
- Automate weekly video fetching
- Create a web interface for easy access

## 🤝 Contributing
Feel free to open issues or submit PRs to improve the project!

## 📜 License
This project is open-source and available under the **MIT License**.

---
✨ **Developed by [Your Name]** | Follow for updates! 🚀

