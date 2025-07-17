
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import streamlit as st
import streamlit.components.v1 as components
from backend.whisper_transcriber import transcribe_audio
from backend.summarizer import summarize_text
from backend.chapters import generate_chapters
import tempfile
from backend.pdf_exporter import generate_pdf


st.set_page_config(page_title = "Podcast Summarizer", layout = "wide")
st.title("🎧 Podcast Summarizer with Highlights & Chapters")

uploaded_file = st.file_uploader("Upload an audio file (MP3 or WAV)", type=["mp3", "wav"])

if uploaded_file:

    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.audio(file_path)




    #Transcribe the audio
    with st.spinner("🔁 Transcribing audio..."):
        transcript, whisper_segments = transcribe_audio(file_path)
        st.subheader("🎧 Transcription")
        st.write(transcript)

    #Summarize the transcription
    with st.spinner("🧠 Summarizing..."):
        summary = summarize_text(transcript)
        st.subheader("🧠 Summary")
        st.write(summary)

    #Generate chapters
    with st.spinner("📌 Generating chapters..."):
        chapters = generate_chapters(whisper_segments, num_chapters=5)
        st.subheader("📌 Topic Chapters")
        for chapter in chapters:
            st.write(f"🕒 {chapter}")

    full_report = "🎧 Podcast Summary Report\n\n"
    full_report += "🧠 Summary:\n" + summary + "\n\n"
    full_report += "🕒 Chapters:\n" + "\n".join(chapters) + "\n\n"
    full_report += "📝 Transcript:\n" + transcript

    # Generate PDF and create download button
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        generate_pdf(summary, chapters, transcript, tmp_file.name)
        with open(tmp_file.name, "rb") as f:
            pdf_bytes=f.read()
            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_bytes,
                file_name="podcast_summary.pdf",
                mime="application/pdf"
            )
