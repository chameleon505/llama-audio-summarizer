import ollama
import assemblyai as aai
import sys

# Replace with your API key
aai.settings.api_key = "apikey"

if len(sys.argv) != 2:
    print("Usage: python main.py <FILE_URL>")
    sys.exit(1)

# URL of the file to transcribe
FILE_URL = sys.argv[1]
config = aai.TranscriptionConfig(speaker_labels=True)

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(
  FILE_URL,
  config=config
)

content = 'Summarize this text:'+transcript.text

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': content,
  },
])
print(response['message']['content'])





