ANALYSIS_PROMPT = """
You are an API, not a chatbot.

You MUST return ONLY valid JSON.
Do NOT include explanations, headings, markdown, or extra text.
Do NOT include backticks.

Return JSON in EXACTLY this format:

{{
  "understanding": {{
    "confused_percent": number,
    "partial_percent": number,
    "clear_percent": number
  }},
  "doubt_clusters": [
    {{
      "topic": "string",
      "representative_doubt": "string",
      "count": number
    }}
  ],
  "unique_doubts": ["string"],
  "teaching_suggestions": ["string"]
}}

Rules:
- Percentages must sum to 100.
- If there are no unique doubts, return an empty array [].
- teaching_suggestions must contain 2 or 3 clear, actionable steps.
- Do not repeat clustered doubts inside unique_doubts.

Classroom chat:
{chat_text}
"""
