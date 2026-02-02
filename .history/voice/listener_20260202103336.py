import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer

model = Model("voice/model")
samplerate = 16000
q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def listen():
    rec = KaldiRecognizer(model, samplerate)

    print("🎙 Listening...")

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000,
                           dtype='int16', channels=1, callback=callback):
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    return text
