import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URI

def test_connection():
    try:
        # Cria a engine de conexão
        engine = create_engine(DATABASE_URI)
        
        # Executa um simples SELECT
        query = "SELECT * FROM COMPRAS"
        df = pd.read_sql_query(query, engine)
        
        # Exibe os resultados
        print(df)
        
        print("Conexão bem-sucedida!")
    except Exception as e:
        print(f"Erro ao conectar: {e}")

if __name__ == "__main__":
    test_connection()
