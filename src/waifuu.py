from os import getenv
from dotenv import load_dotenv

import microphonetotext
import common
import chatbot


common.logger_config()


def waifuu():
    """
    Waifu goes hereee
    """
    load_dotenv()
    init_microphone = microphonetotext.MicrophoneInput()
    init_chatapp = chatbot.ChatApp()
    while True:
        print("Speak now")
        text = init_microphone.speech_to_text()
        if text is False:
            continue
        response = init_chatapp.chat(text)


if __name__ == "__main__":
    load_dotenv()
    waifuu()
