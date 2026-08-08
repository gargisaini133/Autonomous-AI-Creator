import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("LLM_API_KEY")

client = genai.Client(api_key=api_key)


def ask_ai(prompt):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text