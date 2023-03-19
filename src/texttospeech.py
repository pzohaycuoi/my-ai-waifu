import os
import azure.cognitiveservices.speech as speechsdk
import common

common.logger_config()


class TextInput:
    """
    Convert text to speech
    """
    def __init__(self):
        self.speech_config = speechsdk.SpeechConfig(
            subscription=os.environ.get('SPEECH_KEY'),
            region=os.environ.get('SPEECH_REGION'))

        self.audio_config = speechsdk.audio.AudioOutputConfig(
            use_default_speaker=True)

        # The language of the voice that speaks.
        self.speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"

        self.speech_synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=self.speech_config, audio_config=self.audio_config)

    @common.log_function_call
    def text_to_speech(self, text):
        """
        Text to speech
        """
        speech_synthesis_result = self.speech_synthesizer.speak_text_async(
            text).get()
        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            # print(f"Speech synthesized for text: {text}")
            return speech_synthesis_result
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print(f"Speech synthesis canceled: {cancellation_details.reason}")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                raise speechsdk.CancellationReason.Error


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    while True:
        a = TextInput()
        a.text_to_speech()
