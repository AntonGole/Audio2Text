# Python code to convert video to audio
import moviepy.editor as mp
from pydub import AudioSegment

import os, shutil


def video_to_wav(video_file):
    # Remove any old temp files
    for filename in os.listdir('temp'):
        file_path = os.path.join('temp', filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    # Load the video file using MoviePy
    clip = mp.VideoFileClip(video_file)

    # Extract the audio from the video clip
    audio = clip.audio

    # Define the output file path for the audio
    output_audio_file = f'temp/{video_file}_converted.wav'

    # Write the extracted audio to the output file in MP3 format
    audio.write_audiofile(output_audio_file)


def mp3_to_wav(mp3_file):
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(f'temp/{mp3_file}_converted.wav', format='wav')


def convert_to_wav(file):
    if file.endswith('.mp3'):
        mp3_to_wav(file)

    else:
        video_to_wav(file)
