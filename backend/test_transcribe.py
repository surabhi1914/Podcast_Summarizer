from whisper_transcriber import transcribe_audio
from summarizer import summarize_text
from chapters import generate_chapters

if __name__ == "__main__":
    file_path = "../uploads/sample.mp3"  # Put a sample .mp3 or .wav here
    transcript, whisper_segments = transcribe_audio(file_path)
    # print("\n🎧 Transcription:\n", text)

    
    # print("\n🧠 Summary:\n")
    # summary = summarize_text(text)
    # print(summary)

    

    print("\n📌 Topic Chapters:\n")
    chapters = generate_chapters(whisper_segments, num_chapters=5)
    for chapter in chapters:
        print("🕒", chapter)