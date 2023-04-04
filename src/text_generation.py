import speech_recognition as sr
from pydub import AudioSegment

from src.file_conversion import convert_to_wav

import os


def transcribe_audio(audio_file):
	recognizer = sr.Recognizer()

	segments = split_audio_into_segments(audio_file)

	# Remove temp full .wav file
	if os.path.exists(audio_file):
		os.remove(audio_file)
	else:
		print(f'The file {audio_file} does not exist and therefore can not be removed')

	# To export the segments as separate wav files:
	for idx, segment in enumerate(segments):
		segment.export(f'temp/segment_{idx}.wav', format="wav")

		with sr.AudioFile(f'temp/segment_{idx}.wav') as source:
			audio = recognizer.record(source)

		try:
			text = recognizer.recognize_google(audio)
			with open(f'{audio_file}_transcription.txt', 'a') as txt_file:
				txt_file.write(text)
			print(f'Transcription saved to {audio_file}_transcription.txt')
		except sr.UnknownValueError:
			print('SpeechRecognition could not understand the audio')
		except sr.RequestError as e:
			print(f'Could not request results from the Google Web Speech API; {e}')

		# Remove temp segmented .wav file
		if os.path.exists(f'temp/segment_{idx}.wav'):
			os.remove(f'temp/segment_{idx}.wav')
		else:
			print(f'The file temp/segment_{idx}.wav does not exist and therefore can not be removed')


def split_audio_into_segments(file_path, segment_duration=40):
	audio = AudioSegment.from_wav(file_path)
	audio_length = len(audio)
	segments = []

	for i in range(0, audio_length, segment_duration * 1000):
		start_time = i
		end_time = i + (segment_duration * 1000)
		segment = audio[start_time:end_time]
		segments.append(segment)

	return segments


input_file_path = 'YOUR_VIDEO/MP3_FILE_PATH'
convert_to_wav(input_file_path)

transcribe_audio(f'temp/{input_file_path}_converted.wav')
