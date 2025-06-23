from RealtimeSTT import AudioToTextRecorder
import pyttsx3


def process_text(text):
        pyttsx3.speak(text)

if __name__ == "__main__":
        recorder = AudioToTextRecorder()

        print("\n--- STS STARTED ---\n")
        while True:
                recorder.text(process_text)
