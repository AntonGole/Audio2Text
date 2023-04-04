import whisper


def transcribe_audio(audio_file):
    """
    Transcribe an audio file using the Whisper ASR model.

    :param audio_file: The path to the audio file.
    """
    # Load the Whisper ASR model
    model = whisper.load_model("base")

    # Transcribe the audio file using the model
    result = model.transcribe(audio_file)

    # Save the transcribed text to an output file
    with open('output.txt', 'w') as txt_file:
        txt_file.write(result["text"])