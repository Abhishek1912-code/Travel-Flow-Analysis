import yt_dlp
import os

def download_video(url, output_path):
    if not os.path.exists(output_path):
        print("Downloading video...")
        ydl_opts = {
            'outtmpl': output_path,
            'format': 'best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    else:
        print("Video already exists:", output_path)
