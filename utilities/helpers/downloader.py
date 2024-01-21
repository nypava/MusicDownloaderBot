from pytube import YouTube
import os

def download(video_id):
    yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')

    out_file = yt.streams.filter(only_audio=True)[0].download()

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'

    os.rename(out_file, new_file)

    return new_file
