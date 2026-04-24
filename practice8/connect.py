import psycopg2
from config import load_config

def test_connection():
    try:
        params = load_config()
        conn = psycopg2.connect(**params)
        print("Connected to PostgreSQL successfully!")
        conn.close()
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_connection()