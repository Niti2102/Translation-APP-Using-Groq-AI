Here's a `README.md` for your **Translation App using Groq AI and Streamlit**:

---

# 🌐 Translation App using Groq AI

This is a simple and interactive language translation web application built with [Streamlit](https://streamlit.io/) and powered by [Groq's LLaMA3-70B model](https://groq.com/). It allows users to translate text from one language to another using natural language prompts.

## 🚀 Features

* ✍️ User-friendly text input
* 🌍 Translate into multiple languages: English, French, Spanish, Tamil, Hindi, and German
* ⚡ Powered by **Groq** LLM (LLaMA3-70B)
* 🔒 API Key securely managed with Streamlit Secrets

## 🖥️ Demo

https://translation-app-using-groq-ai-mwkvvs4fay37umnxdkaenr.streamlit.app/

---

## 🧠 Tech Stack

* **Frontend**: Streamlit
* **Backend**: LangChain + Groq AI
* **Model**: `llama3-70b-8192` via `langchain_groq`

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/translation-groq-app.git
cd translation-groq-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key

In `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

> **Note:** Never commit your API key to version control.

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📂 File Structure

```
translation-groq-app/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
└── .streamlit/
    └── secrets.toml        # API key configuration
```

---

## 🧾 Example Prompt Template

The app uses a LangChain prompt template like:

```
System: You are a helpful assistant which helps in translating one language to another.

User: Translate {frominput} to {tooutput}.
```

---

## 📦 Dependencies

```txt
streamlit
langchain
langchain_groq
```

---

## 🧠 Future Improvements

* Auto-detect input language
* Add speech-to-text and text-to-speech
* History of translations
* More language options

---

## 📜 License

MIT License

---

## 🙌 Acknowledgements

* [Groq AI](https://groq.com/)
* [LangChain](https://www.langchain.com/)
* [Streamlit](https://streamlit.io/)

