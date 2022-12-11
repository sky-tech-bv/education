'''
First of all you should install python module names pytube.
To make it enter to terminal: pip install pytube.
'''
from pathlib import Path
from pytube import YouTube

def get_link():
    print('To get needed file you should enter full Youtube link.')
    while True:
        link = input("Enter the YouTube video URL: ")
        if link.startswith('https://') != True:
            print('Please enter fuul path of video including "https://" in the begining')
            continue
        return link

def Download(file_name):
    video_path = Path(__file__).parent.resolve()
    link = get_link()
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=video_path, filename=file_name)
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    return str(video_path) + '/'


