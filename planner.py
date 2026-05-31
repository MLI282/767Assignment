# planner.py

from openai import OpenAI

import json

client = OpenAI(
    api_key="sk-22f087eba9ef4eca8edc0264b0226fb2",
    base_url="https://api.deepseek.com"
)


def extract_preferences(user_input,memory):

    prompt = f"""
You are an intelligent planning agent.

Convert the user request into STRICT JSON.

Return format:

{{
  "type": "restaurant | cafe | supermarket | etc",

  "cuisine": "italian | chinese | korean | null",

  "keywords": "spicy | sushi | coffee | null",

  "price": "cheap | medium | expensive | null",

  "max_distance_km": number | null
}}

Rules:
- Return JSON only
- No markdown
- No explanation
- If unknown use null

User memory:
{memory}

User request:
{user_input}
"""

    response = client.chat.completions.create(

        model="deepseek-chat",

        messages=[

            {
                "role": "system",
                "content": "You are a planning agent."
            },

            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )

    raw = (
        response
        .choices[0]
        .message
        .content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:

        parsed = json.loads(raw)

        return parsed

    except Exception as e:

        print("\n[Planner Error]")
        print(raw)

        return {
            "type": "restaurant",
            "cuisine": None,
            "keywords": user_input,
            "price": None,
            "max_distance_km": None
        }