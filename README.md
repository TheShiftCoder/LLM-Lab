# LLM Lab

A comprehensive, lightweight testbed for experimenting with major LLM APIs and local models safely using environment variables.

## Supported Providers & Models

| Provider | Folder | Default Model | Key / Config Required |
| :--- | :--- | :--- | :--- |
| **OpenAI** | `OpenAI/` | `gpt-4o` | `OPENAI_API_KEY` |
| **Google Gemini** | `Gemini/` | `gemini-2.5-flash` | `GEMINI_API_KEY` |
| **Anthropic** | `Anthropic/` | `claude-3-5-sonnet-20241022` | `ANTHROPIC_API_KEY` |
| **DeepSeek** | `DeepSeek/` | `deepseek-chat` | `DEEPSEEK_API_KEY` |
| **Groq** | `Groq/` | `llama-3.3-70b-versatile` | `GROQ_API_KEY` |
| **Ollama** | `Ollama/` | `llama3.2` | Local server (No API key) |
| **Mistral AI** | `Mistral/` | `mistral-small-latest` | `MISTRAL_API_KEY` |
| **Cohere** | `Cohere/` | `command-r-plus` | `COHERE_API_KEY` |

---

## Project Structure

```
LLM Lab/
├── Anthropic/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
├── Cohere/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
├── DeepSeek/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
├── Gemini/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
├── Groq/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
├── Mistral/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
├── Ollama/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
├── OpenAI/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
├── .gitignore
└── README.md
```

---

## General Quickstart

For any provider (e.g., `Anthropic`, `DeepSeek`, `Groq`, etc.):

1. **Navigate to the provider directory:**
   ```bash
   cd <ProviderFolder>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   Open `.env` and fill in your API key.

5. **Run the application:**
   ```bash
   python app.py
   ```
