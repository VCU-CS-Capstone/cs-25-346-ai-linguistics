import whisper
import sys

audio_path = sys.argv[1]

model = whisper.load_model('medium')

result = model.transcribe(audio_path)

print(result['text'])