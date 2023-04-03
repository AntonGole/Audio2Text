import speech_recognition as sr
from pydub import AudioSegment
from os import remove


def transcribe_audio(audio_file, output_txt_file):
	recognizer = sr.Recognizer()

	segments = split_audio_into_segments(audio_file)

	# To export the segments as separate wav files:
	for idx, segment in enumerate(segments):
		segment.export(f'temp/segment_{idx}.wav', format="wav")

		with sr.AudioFile(f'temp/segment_{idx}.wav') as source:
			audio = recognizer.record(source)

		try:
			text = recognizer.recognize_google(audio)
			with open(output_txt_file, 'w') as txt_file:
				txt_file.write(text)
			print(f"Transcription saved to {output_txt_file}")
		except sr.UnknownValueError:
			print("SpeechRecognition could not understand the audio")
		except sr.RequestError as e:
			print(f"Could not request results from the Google Web Speech API; {e}")


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


audio_file_path = "temp/test.wav"
output_txt_file = "test.txt"
transcribe_audio(audio_file_path, output_txt_file)