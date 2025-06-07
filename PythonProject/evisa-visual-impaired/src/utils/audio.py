def text_to_speech(message, openai):
    response = openai.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=message
    )
    return response.content

def play_audio(audio_content):
    from io import BytesIO
    from pydub import AudioSegment
    from pydub.playback import play

    audio_stream = BytesIO(audio_content)
    audio = AudioSegment.from_file(audio_stream, format="mp3")
    play(audio)