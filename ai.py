import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def get_ai_response(user_message: str):
    chat_completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ UPDATED MODEL
        messages=[
            {"role": "system", "content": "You are FalconAI, a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )
    return chat_completion.choices[0].message.content