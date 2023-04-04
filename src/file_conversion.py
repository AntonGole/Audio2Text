from utils import remove_temp_files
import moviepy.editor as mp
from pytube import YouTube


def video_to_mp3(video_file):
    """
    Convert a video file to an MP3 audio file.

    :param video_file: The path to the video file.
    """
    # Remove any temporary files before processing
    remove_temp_files()

    # Load the video file using MoviePy
    clip = mp.VideoFileClip(video_file)

    # Extract the audio from the video clip
    audio = clip.audio

    # Define the output file path for the audio
    output_path = "temp"
    filename = "audio.mp3"
    output_audio_file = f'{output_path}/{filename}'

    # Write the extracted audio to the output file in MP3 format
    audio.write_audiofile(output_audio_file)

    print(f"Audio extracted to {output_path}/{filename}")


def youtube_to_mp3(url):
    """
    Download the audio from a YouTube video and save it as an MP3 file.

    :param url: The URL of the YouTube video.
    """
    # Remove any temporary files before processing
    remove_temp_files()

    # Create a YouTube object with the video URL
    yt = YouTube(url)

    # Get the first audio-only stream available for the video
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Define the output file path for the downloaded audio
    output_path = "temp"
    filename = "audio.mp3"

    # Download the audio stream to the specified output path and filename
    audio_stream.download(output_path=output_path, filename=filename)

    print(f"Audio downloaded to {output_path}/{filename}")
