import json
import re
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def extract_json(text):
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("No JSON found in response")
    return json.loads(match.group())


def analyze_chat(chat_text, prompt):
    model = genai.GenerativeModel("models/gemini-flash-lite-latest")
    response = model.generate_content(prompt.format(chat_text=chat_text))

    raw = response.text.strip()

    try:
        # Try strict JSON first
        return json.loads(raw)
    except json.JSONDecodeError:
        # Fallback: extract JSON from messy output
        return extract_json(raw)
