import whisper
model = whisper.load_model("base") 

def transcribe_audio(file_path):

    
    result = model.transcribe(file_path)
    full_text = result["text"]
    segments = result["segments"]

    return full_text, segments
