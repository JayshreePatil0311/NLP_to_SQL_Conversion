import google.generativeai as genai
import re

# Function to get API key from user input
API_KEY = input("Enter your Google API Key: ").strip()
genai.configure(api_key=API_KEY)

def extract_sql(text):
    """
    Extracts only the SQL query from AI-generated text and removes extra explanations.
    """
    sql_query = re.findall(r"SELECT.*?;", text, re.DOTALL)  # Extract SQL query only
    return sql_query[0] if sql_query else "Error: No valid SQL found."

def convert_to_sql(user_query):
    """Function to convert natural language to SQL using Gemini AI."""
    model = genai.GenerativeModel("gemini-1.5-pro")  # Use correct model
    response = model.generate_content(f"Convert this to SQL and return only the query:\n{user_query}")

    if response and hasattr(response, "text"):
        return extract_sql(response.text.strip())  # Extract only the SQL query
    else:
        return "Error: Failed to generate SQL."

# Test the function
if __name__ == "__main__":
    user_query = "List employees working in the IT department."
    sql_query = convert_to_sql(user_query)
    print("Generated SQL:", sql_query)
