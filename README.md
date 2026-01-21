
# Personal Therapy Assistant 🤖🧠

A conversational therapy-style chatbot built with the **Groq API**, designed to provide supportive and context-aware responses based on prior interactions. The app uses **Streamlit** for its user interface and implements memory so the assistant can respond with continuity across multiple user messages. 

## 🔍 About

**Personal Therapy Assistant** is an interactive AI chatbot that simulates supportive conversation. It is built for experimentation with generative models, conversation memory, and rapid prototyping of AI therapist-like experiences. It can remember past messages within a session to produce more empathetic and context-aware responses. :contentReference[oaicite:2]{index=2}

---

## ✨ Features

✔️ Conversational chatbot interface  
✔️ Memory support for context–aware replies  
✔️ Built on Groq API for AI responses  
✔️ Clean UI using Streamlit  
✔️ Simple, extensible design for further experimentation


---

## 🧠 Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend UI | Streamlit |
| AI Engine | Groq API |
| Language | Python |
| Chat Memory | Custom session memory |

---

## 🚀 Getting Started

Follow the steps below to run the application locally:

### 1. Clone repository
```bash
git clone https://github.com/sisira214/personal_therapy_assistant.git
cd personal_therapy_assistant
````

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file with your Groq API key:

```bash
GROQ_API_KEY="your_groq_api_key_here"
```

Add any other configuration keys required by the code.

### 5. Run the app

```bash
streamlit run therApp.py
```

---

## 💡 Usage

1. Open the Streamlit app in your browser after starting it.
2. Type your messages into the chat input.
3. The assistant will respond using the Groq API and keep context for improved continuity.

Feel free to enhance the bot’s behavior, add logging, or integrate sentiment analysis for richer therapeutic responses.

---

## 📁 Project Structure

```
personal_therapy_assistant/
├── .gitignore
├── LICENSE
├── README.md
├── chatmanager.py      # Conversation and memory logic
├── grokApp.py          # App integration with Groq API
├── therApp.py          # Streamlit interface entrypoint
└── requirements.txt.txt
```

---

## 🤝 Contributing

Contributions are always welcome! Feel free to:

* Add new features (e.g., sentiment awareness, long-term memory)
* Improve conversation quality
* Submit issues or pull requests

Please follow standard GitHub workflows for contributions.

---

## 🛡️ License

Distributed under the **MIT License**. See `LICENSE` for details. ([GitHub][1])

---

If you want, I can also generate badges (build status, API docs, license) and a GIF demo for this README.

[1]: https://github.com/sisira214/personal_therapy_assistant "GitHub - sisira214/personal_therapy_assistant: I have created a chatbot using Groq API, implemented memory too so that it can answer based on previous questions and used streamlit as user interface."

