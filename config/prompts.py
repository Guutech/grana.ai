def build_analysis_prompt(metrics):
    return f"""
    Usuário tem:
    - Renda: {metrics['income']}
    - Gastos: {metrics['expenses']}
    - Maior gasto: {metrics['top_category']}

    Explique de forma simples e dê sugestões financeiras práticas.
    """