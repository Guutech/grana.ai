from core.intent_classifier import classify_intent
from data.data_service import DataService
from use_cases import analyze_finances, generate_chart


data_service = DataService()

def handle(user_input, df):
    intent = classify_intent(user_input)

    if intent == "analysis":
        return analyze_finances.execute(df)

    elif intent == "chart":
        return generate_chart.execute(df)

    return {"text": "Não entendi sua pergunta ainda."}