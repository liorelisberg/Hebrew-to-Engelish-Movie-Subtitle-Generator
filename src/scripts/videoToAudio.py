from moviepy.editor import AudioFileClip
import os


def video_to_audio(dir, video, audio_name, audio_format):
    AudioFileClip(os.path.join(dir, f"{video}")).write_audiofile(os.path.join(dir, f"{audio_name}.{audio_format}"))