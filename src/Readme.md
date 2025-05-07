# Source Code Folder
To be structured as needed by project team.

python scripts to run transcriptions of audio with the base whipser model and with the fine tuned model are provided in this directory

## Setup Instructions

### 1. Create virtual enviorment
```bash
python -m venv venv
```

### 2. Activate enviorment
```bash
source venv/bin/activate
```

### 3. Install required package
```bash
pip install reqirements.txt
```

### 4. Install ffmpeg with Homebrew
```bash
brew install ffmpeg
```

## Running transcription

### Running transcribe_with_base.py
python file can be run from command line and will print out results to command line

```bash
python3 transcribe_with_base.py /path/to/audio.wav
```

the same command can be used for the fine tuned model 
```bash
python3 transcribe_with_fine_tuned.py /path/to/audio.wav
```


Please document here
| Subdirectory Name | Description |
|---|---|
| | |
| | |
| | |
| | |
| | |
