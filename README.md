# Audio2Text
Audio2Text is a Python application that transcribes audio from MP3 files, video files, or YouTube URLs. It supports popular video formats like MP4, AVI, and MKV. The transcriptions are saved in a plain text file.

## Installation
Clone this repository:
```
git clone https://github.com/AntonGole/audio2text.git
```

Install the required dependencies:

```
pip install whisper
```
```
pip install moviepy
```
```
pip install tkinter
```
```
pip install pytube3
```

## Usage
Run the main script:

```
python main.py
```

The GUI will open, providing you with three options:

Select MP3: Click this button to choose an MP3 file to transcribe.
Select Video: Click this button to choose a video file to transcribe.
Enter YouTube URL: Click this button to show a text entry field where you can paste a YouTube URL, then click "OK" to transcribe the video.
After the transcription process is complete, the transcribed text will be saved in output.txt.

## Dependencies
* tkinter
* moviepy
* pytube3
* whisper

## License
MIT
