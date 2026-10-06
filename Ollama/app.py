import ollama

print("Sending request to local Ollama model...")

# Send request to local Ollama instance
response = ollama.chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': 'Explain artificial intelligence in simple terms',
        },
    ]
)

# Display response
print("\nOllama Response:")
print(response['message']['content'])
