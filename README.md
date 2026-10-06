# LLM Lab

A lightweight testbed for experimenting with different LLM APIs (OpenAI & Google Gemini) safely using environment variables.

## Project Structure

```
LLM Lab/
├── OpenAI/
│   ├── app.py              # OpenAI test script
│   ├── requirements.txt    # OpenAI dependencies
│   ├── .env.example        # Environment variables template
│   └── .gitignore
├── Gemini/
│   ├── app.py              # Google Gemini test script
│   ├── requirements.txt    # Gemini dependencies (google-genai)
│   ├── .env.example        # Environment variables template
│   └── .gitignore
├── .gitignore
└── README.md
```

## Setup & Running

### 1. OpenAI Lab

```bash
cd OpenAI
python -m venv venv

# Activate venv (Windows PowerShell)
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
cp .env.example .env
```
Add your API key inside `OpenAI/.env`:
```env
OPENAI_API_KEY=your_openai_api_key_here
```
Run the script:
```bash
python app.py
```

---

### 2. Gemini Lab

```bash
cd Gemini
python -m venv venv

# Activate venv (Windows PowerShell)
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
cp .env.example .env
```
Add your API key inside `Gemini/.env`:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```
Run the script:
```bash
python app.py
```
