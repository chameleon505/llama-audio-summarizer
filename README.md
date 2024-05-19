# llama-audio-summarizer
A Python tool that uses AssemblyAI for transcribing audio files and Llama3 for summarizing the transcriptions


## Description

This script transcribes audio files using AssemblyAI and then summarizes the transcriptions using Llama3. You will need to provide your own API key from [AssemblyAI](https://www.assemblyai.com/).

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/chameleon505/llama-audio-summarizer.git
    cd llama-audio-summarizer
    ```

2. Install the required packages:
    ```sh
    pip install assemblyai
    pip install ollama
    ```

## Usage

1. Replace `apikey` in the script with your own AssemblyAI API key. You can get an API key by signing up at [AssemblyAI](https://www.assemblyai.com/).

2. Run the script with the URL of the audio file you want to transcribe:
    ```sh
    python main.py <FILE_URL>
    ```

   


