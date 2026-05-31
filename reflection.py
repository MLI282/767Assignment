# reflection.py

from openai import OpenAI


OPENAI_API_KEY="sk-22f087eba9ef4eca8edc0264b0226fb2"
OPENAI_MODEL="deepseek-chat"


client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.deepseek.com"
)


def reflect_recommendations(

    user_input,

    preferences,

    recommendations
):

    prompt = f"""
You are a reflection agent.

Your job is to evaluate whether the recommendations satisfy the user's goal.

User request:
{user_input}

Extracted preferences:
{preferences}

Recommendations:
{recommendations}

Tasks:
1. Check whether recommendations match the user goal
2. Identify possible problems
3. Give a short improvement suggestion

Keep response concise.
"""

    response = client.chat.completions.create(

        model=OPENAI_MODEL,

        messages=[

            {
                "role": "system",
                "content":
                    "You are a reflection agent."
            },

            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )

    return (
        response
        .choices[0]
        .message
        .content
    )