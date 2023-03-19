from os import getenv
from dotenv import load_dotenv

import microphonetotext
import common
import chatbot
import texttospeech


common.logger_config()


def waifuu():
    """
    Waifu goes hereee
    """
    load_dotenv()
    microphone = microphonetotext.MicrophoneInput()
    chatapp = chatbot.ChatApp()
    speech = texttospeech.TextInput()
    while True:
        print("Speak now")
        text = microphone.speech_to_text()
        if text is False:
            continue
        response = chatapp.chat(text)
        extract_text = response["choices"][0]["message"]["content"]
        speech_response = speech.text_to_speech(extract_text)


if __name__ == "__main__":
    load_dotenv()
    waifuu()
