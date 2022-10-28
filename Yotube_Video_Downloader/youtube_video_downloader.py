import pytube
import pandas as pd


def download(x):
    video_url = x
    try:
        print()
        print("Video Downloading")
        print()
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download(path_to_store)
        print("Video downloaded")
    except:
        print("Error")
        txt_file = open("Error_links.txt", "a")
        txt_file.write(video_url+"\n")
        txt_file.close()


path_to_store = "J:\My Drive\Research\Videos"
path_to_csv = 'url-list.csv'

data = pd.read_csv(path_to_csv)

url_list = data["URL"].values.tolist()

# this was my assigned list, comment this line as well as change mylist to url_list to get video of all the files
mylist = url_list[51:77]

for i in mylist:  # change it to url_list to get all videos in file
    download(str(i))

print()
