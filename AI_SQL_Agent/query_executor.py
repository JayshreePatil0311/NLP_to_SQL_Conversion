from database import connect_to_db
from ai_sql import convert_to_sql
import re
import json
from decimal import Decimal
from datetime import date  # Import date module

def clean_sql_query(ai_response):
    """Cleans AI-generated SQL query by removing unnecessary characters."""
    sql_query = re.sub(r"```sql|```", "", ai_response, flags=re.MULTILINE)  # Remove Markdown blocks
    sql_query = re.sub(r"--.*", "", sql_query)  # Remove inline comments
    sql_query = sql_query.strip().split("\n\n")[0]  # Keep only first SQL statement
    return sql_query.strip()

def convert_to_serializable(data):
    """Recursively converts Decimal and date values to JSON serializable types."""
    if isinstance(data, list):
        return [convert_to_serializable(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_to_serializable(value) for key, value in data.items()}
    elif isinstance(data, Decimal):
        return float(data)  # Convert Decimal to float
    elif isinstance(data, date):
        return data.isoformat()  # Convert date to string (YYYY-MM-DD)
    return data

def execute_query(user_query):
    """Executes AI-generated SQL query and returns results in JSON format."""
    conn = connect_to_db()
    if conn is None:
        return json.dumps({"error": "Database connection failed."})

    ai_response = convert_to_sql(user_query)  # AI generates SQL query
    sql_query = clean_sql_query(ai_response)  # Clean the SQL query
    
    print(f"\n✅ Cleaned SQL Query:\n{sql_query}\n")  # Debugging output

    try:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        columns = [desc[0] for desc in cursor.description]  # Get column names
        results = cursor.fetchall()

        conn.close()

        # Convert results to JSON format
        json_output = json.dumps(
            convert_to_serializable([dict(zip(columns, row)) for row in results]), 
            indent=4
        )
        return json_output

    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    test_queries = [
        "List employees working in the IT department.",
        "Show all employees in Mumbai.",
        "Find employees who joined after 2021.",
        "Who is the highest-paid employee?"
    ]

    for query in test_queries:
        print(f"\n🔍 User Query: {query}")
        result = execute_query(query)
        print("📝 AI-Generated SQL Query:", convert_to_sql(query))
        print("📊 Query Result:", result)
