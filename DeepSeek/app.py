import os
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# DeepSeek uses OpenAI compatible API format
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

print("Sending request to DeepSeek...")

# Send request to DeepSeek
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Explain artificial intelligence in simple terms"}
    ]
)

# Display response
print("\nDeepSeek Response:")
print(response.choices[0].message.content)
