import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_PARAMS = {
    "dbname": os.getenv("DB_DATABASE"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}

def connect_db():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        print("Connected to the database successfully!")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def execute_query(conn, query, params=None):
    """Execute a query and fetch results (if applicable)."""
    with conn.cursor() as cur:
        cur.execute(query, params or ())
        if query.strip().lower().startswith("select"):
            return cur.fetchall()
        conn.commit()

def main():
    conn = connect_db()
    if conn is None:
        raise Exception("Failed to connect to the database")

    test_query = "SELECT * FROM pg_extension"
    print("Users:", execute_query(conn, test_query))

    conn.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()