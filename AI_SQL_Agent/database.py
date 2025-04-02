import psycopg2

# Database connection details
DB_NAME = "company_data"
DB_USER = "postgres"
DB_PASSWORD = "newpassword"
DB_HOST = "localhost"
DB_PORT = "5432"  # Default PostgreSQL port

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("✅ Connected to the database successfully!")
        return conn
    except Exception as e:
        print(f"❌ Error connecting to the database: {e}")
        return None
