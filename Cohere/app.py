import os
import cohere
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Initialize Cohere ClientV2
co = cohere.ClientV2(api_key=os.getenv("COHERE_API_KEY"))

print("Sending request to Cohere...")

# Send request to Cohere
response = co.chat(
    model="command-r-plus",
    messages=[
        {
            "role": "user",
            "content": "Explain artificial intelligence in simple terms"
        }
    ]
)

# Display response
print("\nCohere Response:")
print(response.message.content[0].text)
