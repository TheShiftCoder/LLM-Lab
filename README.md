# LLM Lab

A lightweight Python project for experimenting with OpenAI's API.

## Project Structure

```
LLM Lab/
├── OpenAI/
│   ├── app.py              # Main script to query OpenAI models
│   ├── requirements.txt    # Python dependencies
│   ├── .env.example        # Example environment configuration
│   └── .gitignore
├── .gitignore
└── README.md
```

## Setup Instructions

### 1. Prerequisites
- Python 3.8+ installed
- An active OpenAI API key

### 2. Installation
Navigate to the `OpenAI` directory and set up your virtual environment:

```bash
cd OpenAI
python -m venv venv
```

Activate the virtual environment:
- **Windows (PowerShell):** `.\venv\Scripts\Activate.ps1`
- **Windows (CMD):** `.\venv\Scripts\activate.bat`
- **macOS/Linux:** `source venv/bin/activate`

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the `OpenAI/` directory based on `.env.example`:

```bash
cp .env.example .env
```

Open `.env` and insert your OpenAI API key:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Running the Code
Run the application:
```bash
python app.py
```
