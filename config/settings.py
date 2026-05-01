import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

USE_AI = False  

if USE_AI:
    from google import genai
    client = genai.Client(api_key=API_KEY)


def call_llm(prompt):
    if USE_AI:
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            return response.text
        except Exception:
            return "⚠️ IA indisponível no momento."

    # fallback (sem IA)
    return "📊 Análise básica: você está gastando mais na categoria principal. Considere revisar esses custos."