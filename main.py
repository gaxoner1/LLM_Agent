from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from google import genai
from groq import Groq

load_dotenv()

#--llm = genai (model="gemini-2.5-flash") --see https://aistudio.google.com/docs/get-started for latest availble models.

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain quantum computing in one sentence."
)
print(response.text)

