import psycopg2
import config

def connect():
    try:
        conn = psycopg2.connect(
            host=config.host,
            dbname=config.dbname,
            user=config.user,
            password=config.password,
            port=config.port
        )
        return conn
    except Exception as e:
        print("Connection error:", e)