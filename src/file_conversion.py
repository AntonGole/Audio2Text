# Python code to convert video to audio
import moviepy.editor as mp


def video_to_mp3(video_file):
    # Load the video file using MoviePy
    clip = mp.VideoFileClip(video_file)

    # Extract the audio from the video clip
    audio = clip.audio

    # Define the output file path for the audio
    output_audio_file = "Audio File.mp3"

    # Write the extracted audio to the output file in MP3 format
    audio.write_audiofile(output_audio_file)
