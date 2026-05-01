import os
from dotenv import load_dotenv
import google.generativeai as genai

# carrega o .env
load_dotenv()

# pega a variável
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("A chave da API não foi encontrada no .env")

# configura a IA
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def call_llm(prompt):
    response = model.generate_content(prompt)
    return response.text