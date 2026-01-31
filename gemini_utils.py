import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_chat(chat_text, prompt):
    model = genai.GenerativeModel("models/gemini-flash-lite-latest")

    formatted_prompt = prompt.format(chat_text=chat_text)
    response = model.generate_content(formatted_prompt)

    return response.text
