import ollama

response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "Reply with exactly the word SUCCESS."
        }
    ]
)

print(response)