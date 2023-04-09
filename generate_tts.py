from TTS.api import TTS

tts = TTS("tts_models/en/ljspeech/glow-tts")

import sys

if (len(sys.argv) < 2):
    print("Usage: python generate_tts.py <input file>")
    exit(1)

file= open(sys.argv[1], "r")

text=file.read()

output_file = sys.argv[1].replace(".txt", ".wav")

tts.tts_to_file(text=text, file_path=output_file)
print(output_file)

file.close()
