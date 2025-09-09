import speech_recognition as sr

class Transcriber:
    def __init__(self, lang: str = "en-US"):
        self.r = sr.Recognizer()
        self.lang = lang

    def transcribe(self, wav_path: str) -> str:
        with sr.AudioFile(wav_path) as source:
            audio = self.r.record(source)  #
        try:
            return self.r.recognize_google(audio, language=self.lang)
        except Exception:
            return ""