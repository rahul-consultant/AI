import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

def send_chat_message(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages,
        api_key=openai_api_key
    )
    return response.choices[0].message.content

def generate_audio_response(message):
    response = openai.Audio.create(
        model="text-to-speech",
        input=message,
        api_key=openai_api_key
    )
    return response.content