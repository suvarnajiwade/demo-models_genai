# from langchain_huggingface.chat_models import ChatHuggingFace
# from langchain_huggingface.llms import HuggingFaceEndpoint
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv(dotenv_path="../.env")

# # Get Hugging Face API token
# hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
# if not hf_token:
#     raise ValueError("Hugging Face token not found.")

# # Use a chat-friendly, API-compatible model
# llm = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     task="text-generation",
#     huggingfacehub_api_token=hf_token
# )

# chat_model = ChatHuggingFace(llm=llm)

# # Run chat and print only the content
# response = chat_model.invoke("What is the capital of France?")
# print(response.content.strip())  # ✅ Print actual text only


from langchain_huggingface.chat_models import ChatHuggingFace
from langchain_huggingface.llms import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(dotenv_path="../.env")

# Get Hugging Face API token
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not hf_token:
    raise ValueError("Hugging Face token not found.")

# Create LangChain-compatible model with max token limit
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    max_new_tokens=2,
    #  temperature=0.2,
    #   top_p=0.9# ✅ Pass directly
)

# Wrap with chat
chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("Answer in one word only: What is the capital of India?")
print(response.content.strip())


# Run
# response = chat_model.invoke("What is the capital of India ?")
# print(response.content.strip())
