import pytube
import pandas as pd


def download(x):
    video_url = x
    try:
        print()
        print("Video Downloading")
        print()
        youtube = pytube.YouTube(video_url)
        youtube.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download(path_to_store)
        print("Video downloaded")
    except:
        print("Error")
        txt_file = open("Error_links.txt", "a")
        txt_file.write(video_url+"\n")
        txt_file.close()


# Enter the location for the video to be downloaded
path_to_store = "J:\My Drive\Research\Videos"

# Enter the URL of the video.
URL = ""

download(URL)
