import os
import anthropic
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Initialize Anthropic client
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

print("Sending request to Anthropic (Claude)...")

# Send request to Claude
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Explain artificial intelligence in simple terms"}
    ]
)

# Display response
print("\nClaude Response:")
print(message.content[0].text)
