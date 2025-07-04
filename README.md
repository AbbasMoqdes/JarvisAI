# 🤖 Jarvis AI Assistant

A fully integrated Python-based **AI Voice Assistant** with a real-time GUI, system automation, voice interaction, and AI capabilities — inspired by Marvel's J.A.R.V.I.S.

---

## 🎯 Features

- 🎤 **Voice Interaction**: Speak to Jarvis using your microphone, get instant responses.
- 💬 **Natural Responses**: Uses LLaMA 3 via Groq for intelligent, contextual replies.
- 🗣 **Text-to-Speech**: Edge TTS for realistic voice synthesis.
- 🧠 **Smart Decision Making**: Classifies tasks (general, automation, search, image).
- 🌐 **Real-Time Search**: Uses Python + BeautifulSoup to fetch live web answers.
- 🧾 **Content Generation**: Creates letters, notes, poems, code, and more.
- 💻 **System Automation**: Open/close apps, control volume, search Google/YouTube.
- 🖼️ **Image Generation**: (Optional) Initiates visual generation via prompt.
- 🪟 **Custom PyQt5 GUI**: Fullscreen, animated interface with mic control and chat log.

---

## 🧩 Tech Stack

| Area               | Technology                          |
|--------------------|--------------------------------------|
| Language           | Python 3.10+                         |
| GUI                | PyQt5                                |
| Voice              | edge-tts, pygame, SpeechRecognition  |
| AI                 | LLaMA 3 via Groq API                 |
| Automation         | AppOpener, keyboard, webbrowser      |
| Web Search         | pywhatkit, requests, BeautifulSoup   |
| File Handling      | OS, dotenv, JSON                     |
| Async Execution    | asyncio, threading                   |

---

## 🛠 Installation

```bash
git clone https://github.com/yourusername/Jarvis-AI.git
cd Jarvis-AI
pip install -r requirements.txt
