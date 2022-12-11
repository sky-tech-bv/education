from moviepy import editor
from download_video import Download
from os import chdir

def main():
    audio_name = get_audio_name()
    video_name = audio_name +'.mp4'
    video_path = Download(video_name)
    video = editor.VideoFileClip(video_path + video_name)
    audio = video.audio
    chdir(video_path)
    audio.write_audiofile(f'{audio_name}.mp3')

def get_audio_name():
    while True:
        audio_name = input('Enter a final audio file name: ')
        if audio_name == '':
            print('Your choise is empty. Please try again.')
            continue
        return audio_name
    
if __name__ == '__main__':
    main()