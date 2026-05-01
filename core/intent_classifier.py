def classify_intent(text):
    text = text.lower()

    if "gráfico" in text or "grafico" in text:
        return "chart"

    if "simular" in text:
        return "simulation"

    return "analysis"