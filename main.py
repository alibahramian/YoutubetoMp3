from fileinput import filename
from ssl import Options
import youtube_dl

def run():
    video_url = input("Please enter Youtube video url: ")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    Options={
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }

    with youtube_dl.YoutubeDL(Options) as ydl:
        ydl.download([video_info['webpage_url']])


    print("Download complete...{}".format(filename))


if __name__ == '__main__':
    run()

