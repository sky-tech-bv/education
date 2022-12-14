from pytube import YouTube
from pathlib import Path
from moviepy import editor
import os


def main():
    print('This program get audio file by URL YouTube video. Enjoy!')
    # yt = YouTube(str(input("Enter URL of youtube video: \n")))
   
    link = input('Enter URL of youtube video: \n')
    yt = YouTube(link)

    video = yt.streams.filter(only_audio=True).first()
    out_path = Path(__file__).parent.resolve()
    out_file = video.download(output_path=out_path)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    # video = yt.streams.filter().first()
    # out_path = Path(__file__).parent.resolve()
    # out_file = video.download(output_path=out_path)
    # base, ext = os.path.splitext(out_file)
    # video = editor.VideoFileClip(base + ext)
    # audio = video.audio
    # audio.write_audiofile(f'{base}.mp3')

    # #
    # # new_file = base + '.mp3'
    # # os.rename(out_file, new_file)
    # print(yt.title + " has been successfully downloaded.")
    
if __name__ == '__main__':
    main()





