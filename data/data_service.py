import pandas as pd

class DataService:
    def get_data(self, file):
        if file is None:
            raise ValueError("Nenhum arquivo foi enviado.")

        try:
            df = pd.read_csv(file)
            return df

        except Exception as e:
            raise ValueError(f"Erro ao ler o arquivo: {e}")
        
REQUIRED_COLUMNS = ["income", "expense", "category"]

def validate(df):
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            raise ValueError(f"Coluna obrigatória ausente: {col}")