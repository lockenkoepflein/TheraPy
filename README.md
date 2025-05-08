# 🧠 TheraPy – Conversational Therapy Chatbot

**Status:** 🛠 Under active development  
**Technologies:** Python, Flask, Hugging Face Transformers, DialoGPT

TheraPy is a simple chatbot designed to interact with users in natural language and serve as a virtual companion in emotionally difficult moments. It combines a web-based Flask frontend with a conversational AI backend using a pre-trained model from Hugging Face.

---

## 🎯 Project Goals

- 🤖 **Conversational Interaction**: Create a chatbot that feels emotionally responsive and empathetic
- 🌐 **Web-Based Interface**: Allow access via a simple browser-based UI using Flask
- 🧠 **NLP-Powered**: Use a pre-trained transformer model (DialoGPT) to generate responses
- ☁️ **Future Hosting**: Deploy the chatbot on PythonAnywhere

---

## 🚀 Features

- **DialoGPT Integration**: Uses the pre-trained `microsoft/DialoGPT-medium` model via Hugging Face Transformers
- **Flask Backend**: Serves a minimalistic UI with chat input and dynamic response rendering
- **Session Memory**: Keeps conversational context during a session
- **Clean Project Structure**: Ready for further enhancements (e.g. sentiment analysis, logging)

---

## 🔧 Installation & Setup

> ⚠️ Recommended: Create the virtual environment **outside** the project folder to avoid pushing it accidentally.

```bash
# 1. Clone this repository
git clone https://github.com/your-username/therapy-chatbot.git
cd therapy-chatbot

# 2. Create virtual environment one level above the project folder
cd ..
python -m venv venv-therapy
venv-therapy\Scripts\activate  # Windows
# or
source venv-therapy/bin/activate  # macOS/Linux

# 3. Re-enter project folder
cd therapy-chatbot

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
python run.py
```

➡️ Then open your browser at `http://127.0.0.1:5000`

---

## 🔮 Planned Features

- 🧭 Custom conversation flows (e.g. CBT techniques)
- 💬 Sentiment-aware response generation
- 🔐 GDPR-friendly local/session-based conversation history
- 🌈 UI improvements for better accessibility and aesthetics

---

## 🛡 Disclaimer

This project is for **educational and experimental purposes only**.  
It does **not provide real psychological or medical advice** and should **not be used as a substitute for professional help**.

---

## 📄 License

MIT License – see [LICENSE](LICENSE) for details.
