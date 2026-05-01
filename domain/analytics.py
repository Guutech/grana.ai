def generate_metrics(df):
    total_income = df["income"].sum()
    total_expense = df["expense"].sum()

    by_category = df.groupby("category")["expense"].sum()

    top_category = by_category.idxmax()

    return {
        "income": total_income,
        "expenses": total_expense,
        "top_category": top_category,
        "by_category": by_category.to_dict()
    }