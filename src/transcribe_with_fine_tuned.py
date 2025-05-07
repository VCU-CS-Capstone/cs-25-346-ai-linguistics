from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq, GenerationConfig
import torch
import librosa
import sys

audio_path = sys.argv[1]

#processor = AutoProcessor.from_pretrained("Alsman68/whisper-capstone-aviation-audio-trained")
processor = AutoProcessor.from_pretrained("kohoutck/whisper-small-capstone")
#model = AutoModelForSpeechSeq2Seq.from_pretrained("Alsman68/whisper-capstone-aviation-audio-trained")
model = AutoModelForSpeechSeq2Seq.from_pretrained("kohoutck/whisper-small-capstone")
#config = GenerationConfig.from_pretrained("Alsman68/whisper-capstone-aviation-audio-trained")

audio, sr = librosa.load(audio_path, sr=16000)

inputs = processor(audio, sampling_rate=16000, return_tensors="pt", return_attention_mask=True)

device = "cuda" if torch.cuda.is_available() else "cpu"

model = model.to(device)

with torch.no_grad():
    output_tokens = model.generate(inputs["input_features"].to(device))


result = processor.batch_decode(output_tokens, skip_special_tokens=True)

print('\n')
print(result[0])
