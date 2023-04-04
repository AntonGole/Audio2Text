import tkinter as tk
from tkinter import filedialog
from text_generation import transcribe_audio
from file_conversion import *


def select_mp3():
    transcribe_audio(filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")]))


def select_video():
    video_to_mp3(filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")]))
    transcribe_audio('temp/audio.mp3')


def submit_youtube_url():
    youtube_to_mp3(youtube_entry.get())
    transcribe_audio('temp/audio.mp3')


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Audio2Text")

    frame1 = tk.Frame(root)
    frame1.pack(pady=10)

    mp3_button = tk.Button(frame1, text="Select MP3", command=select_mp3, height=4)
    mp3_button.pack(side=tk.LEFT, padx=10)

    video_button = tk.Button(frame1, text="Select Video", command=select_video, height=4)
    video_button.pack(side=tk.LEFT, padx=10)

    youtube_button = tk.Button(frame1, text="Enter YouTube URL", command=lambda: frame2.pack(pady=10), height=4)
    youtube_button.pack(side=tk.LEFT, padx=10)

    frame2 = tk.Frame(root)

    youtube_entry = tk.Entry(frame2, width=40)
    youtube_entry.pack(side=tk.LEFT, padx=10)

    ok_button = tk.Button(frame2, text="OK", command=submit_youtube_url)
    ok_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()