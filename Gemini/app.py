import os
from google import genai
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Create Gemini client using API key from .env
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

print("Sending request to Gemini...")

# Send request to Gemini
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Explain artificial intelligence in simple terms'
)

# Display response
print("\nGemini Response:")
print(response.text)
