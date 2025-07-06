import os
import requests
from dotenv import load_dotenv

# ✅ Load .env from parent folder (TextSummarizerProject)
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path=env_path)

# ✅ Get API key from environment
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please check your .env file and variable name.")

# ✅ Prepare OpenRouter API call
url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "HTTP-Referer": "http://localhost",  # Required by OpenRouter
    "Content-Type": "application/json"
}

data = {
    "model": "mistralai/mistral-7b-instruct",
    "messages": [
        {"role": "user", "content": "What is the capital of India?"}
    ],
    "temperature": 0.7,
    "max_tokens": 100
}

response = requests.post(url, headers=headers, json=data)
output = response.json()

# ✅ Show result
print("🔹 Response:\n", output["choices"][0]["message"]["content"])
