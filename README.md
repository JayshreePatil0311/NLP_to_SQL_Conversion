# Project Name
 AI Agent for SQL Query Execution
# Technologies & Libraries Used 
# 1.Programming Language: 
• Python 
# 2.Database: 
• PostgreSQL
# 3.AI Model for SQL Conversion: 
• Google Gemini API (via google-generativeai package) 
# 4.Backend Framework: 
• Flask 
# 5.Frontend UI 
• Streamlit
# Dependencies & Libraries: 
• Flask → For backend API 
• psycopg2 → For PostgreSQL database connection 
• mysql-connector-python → For MySQL database connection 
• google-generativeai → For AI-based SQL conversion 
• pandas → For data handling in Streamlit 
• re → For cleaning SQL queries 
• json → For formatting query results 
• decimal → For handling numeric values 
• datetime → For date handling
# Installation Commands:
pip install Flask psycopg2 mysql-connector-python google-generativeai pandas 
# Project Architecture 
![UI Preview](![image](https://github.com/user-attachments/assets/dcfd8354-2472-4c6d-9c9f-125b45f042cd) 
• database.py: Handles database connection and query execution. 
• ai_sql.py: Converts natural language queries to SQL using Google Gemini API. 
• query_executor.py: Processes AI-generated SQL and executes it. 
• app.py: Main Flask application that serves the API. 
# (Streamlit UI ): 
• streamlit_app.py: Provides a simple UI for user input and displays query results.
# Output:- 
![image](https://github.com/user-attachments/assets/90ac2262-1d95-4ee3-9de4-f4ea3ee9a8a8)
![image](https://github.com/user-attachments/assets/da1234e4-935d-492d-8ba7-13a4dda3ba2e)
# License
This project is open-source and available.




