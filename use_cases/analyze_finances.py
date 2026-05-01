from domain.analytics import generate_metrics
from config.prompts import build_analysis_prompt
from config.settings import call_llm

def execute(df):
    metrics = generate_metrics(df)

    prompt = build_analysis_prompt(metrics)

    response = call_llm(prompt)

    return {
        "text": response,
        "metrics": metrics
    }