import os
from groq import Groq
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

print("Sending request to Groq...")

# Send request to Groq
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Explain artificial intelligence in simple terms"}
    ]
)

# Display response
print("\nGroq Response:")
print(response.choices[0].message.content)
