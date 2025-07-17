# 🎧 Podcast Summarizer with Highlights & Chapters

> Automatically transcribe, summarize, and chapter-mark podcasts or any audio content using OpenAI Whisper, HuggingFace Transformers, and Streamlit.

---

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)
![Streamlit App](https://img.shields.io/badge/Built%20with-Streamlit-orange)
![License](https://img.shields.io/github/license/surabhi1914/Podcast_Summarizer)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

---

## 🧠 What It Does

🎧 Upload any `.mp3` or `.wav` podcast/audio file  
📝 Get a full **transcript** using OpenAI Whisper  
🧠 View a **clean summary** of the content using HuggingFace Transformers  
📌 Auto-detect **topic chapters** with real timestamps  
📄 Export everything as `.txt` or **formatted PDF**  
🎵 Audio player with chapter links (optional)

---

## 🚀 Demo

Coming soon — or [run locally](#-installation)

---

## 🛠️ Tech Stack

| Tool | Role |
|------|------|
| [OpenAI Whisper](https://github.com/openai/whisper) | Speech-to-text (ASR) |
| [HuggingFace Transformers](https://huggingface.co/transformers/) | NLP summarization |
| [SentenceTransformers](https://www.sbert.net/) + `KMeans` | Topic clustering |
| [Streamlit](https://streamlit.io/) | Frontend UI |
| `fpdf` | PDF export |
| `tempfile`, `os`, `sys` | Local file & path management |

---

## 💻 Installation

### 🔧 1. Clone the repository

```bash
git clone https://github.com/surabhi1914/Podcast_Summarizer.git
cd Podcast_Summarizer
```

### 🐍 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate.bat       # Windows
```

### 📦 3. Install dependencies
```bash
pip install -r requirements.txt
```
⚠️ Make sure ffmpeg is installed on your system for Whisper to work

## ▶️ Usage

```bash
streamlit run frontend/app.py

```

## ✨ Features

- [x] Upload MP3/WAV files  
- [x] Transcribe using Whisper  
- [x] Summarize using BART (`facebook/bart-large-cnn`)  
- [x] Auto-chapter detection with real audio timestamps  
- [x] PDF export with formatting  
- [x] Clean UI using Streamlit  
- [ ] Firebase/Supabase integration for cloud saving (coming soon)  
- [ ] Deploy to Streamlit Cloud (in progress)

---

## 📄 Output Formats

- `.txt` file: Full summary + chapters + transcript  
- `.pdf` file: Styled summary report with section headers  

---

## 📁 Project Structure

Podcast_Summarizer/
├── backend/
│ ├── whisper_transcriber.py
│ ├── summarizer.py
│ ├── chapters.py
│ └── pdf_exporter.py
├── frontend/
│ └── app.py
├── uploads/
├── requirements.txt
└── README.md


---

## 🤖 Powered By

- [OpenAI Whisper](https://openai.com/research/whisper)
- [HuggingFace Transformers](https://huggingface.co/models)
- [Sentence Transformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io/)

---

## 🧑‍💻 Author

**Surabhi Nair**  
📫 [GitHub: @surabhi1914](https://github.com/surabhi1914)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).




