import os
from mistralai import Mistral
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Initialize Mistral client
api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)

print("Sending request to Mistral AI...")

# Send request to Mistral
response = client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role": "user",
            "content": "Explain artificial intelligence in simple terms",
        },
    ]
)

# Display response
print("\nMistral Response:")
print(response.choices[0].message.content)
