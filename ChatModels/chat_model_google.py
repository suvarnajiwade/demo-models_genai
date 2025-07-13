from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get your Google API key from the environment
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

# Initialize Gemini Pro model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",  # ✅ Correct model name
    google_api_key=google_api_key
)

# Ask a question
result = model.invoke("What is the capital of India?")
print(result.content)
