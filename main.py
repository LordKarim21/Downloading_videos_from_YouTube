import os
from pytube import YouTube
import ffmpeg

URL = r'https://www.youtube.com/watch?v=3FWqP80fNJM'
DOWNLOAD_DIRECTORY = r'C:\Users\User\PycharmProjects\Downloading_videos_from_YouTube'


def download_video(url):
    yt = YouTube(url)
    # yt.streams.get_highest_resolution().download(DOWNLOAD_DIRECTORY)
    # это для ленивых.
    # не максимальная качество
    stream_video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first()
    print(stream_video)
    stream_video.download(DOWNLOAD_DIRECTORY, 'video.mp4')
    if not stream_video.is_progressive:
        stream_audio = yt.streams.get_audio_only()
        stream_audio.download(DOWNLOAD_DIRECTORY, 'audio.mp4')
        combine(os.path.join(DOWNLOAD_DIRECTORY, 'audio.mp4'), os.path.join(DOWNLOAD_DIRECTORY, 'video.mp4'))


def combine(audio, video):
    audio_stream = ffmpeg.input(audio)
    video_stream = ffmpeg.input(video)
    ffmpeg.output(audio_stream, video_stream, os.path.join(DOWNLOAD_DIRECTORY, 'result.mp4')).run()


if __name__ == '__main__':
    download_video(URL)
