# Project Name
AI Agent for SQL Query Execution
# Problem Statement 
Many organizations require seamless interaction with databases for data retrieval and 
insights. However, non-technical users struggle with writing SQL queries. This AI agent will 
bridge the gap by enabling: 

• Conversion of natural language queries to SQL

• Execution of queries on a PostgreSQL database 

• Returning results in JSON or tabular format

# Dataset
For this AI-powered SQL Agent, we utilized a structured PostgreSQL database containing sample employee records to test and validate the AI-generated SQL queries. Below are the details of the dataset used
Dataset Name: employee_db

![image](https://github.com/user-attachments/assets/80d9b848-7e86-4040-86ff-b0e66c4ebd3a)

# Technologies & Libraries Used 
1.Programming Language: 
• Python 

2.Database: 
• PostgreSQL

3.AI Model for SQL Conversion: 
• Google Gemini API (via google-generativeai package) 

4.Backend Framework: 
• Flask 

5.Frontend UI 
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
![image](https://github.com/user-attachments/assets/bf98a5b1-b1cc-4a46-a83b-4e227c39161d)

• database.py: Handles database connection and query execution. 

• ai_sql.py: Converts natural language queries to SQL using Google Gemini API. 

• query_executor.py: Processes AI-generated SQL and executes it. 

• app.py: Main Flask application that serves the API. 

# Streamlit UI : 
• streamlit_app.py: Provides a simple UI for user input and displays query results.

# Output:- 
![image](https://github.com/user-attachments/assets/90ac2262-1d95-4ee3-9de4-f4ea3ee9a8a8)
![image](https://github.com/user-attachments/assets/da1234e4-935d-492d-8ba7-13a4dda3ba2e)

# Demo Video:-

https://drive.google.com/drive/folders/1DyRMy0gWZyUJ7nFXUTi4nX1GPQ_9EWpJ?usp=sharing

(note:- Uploaded on Project Video Folder also)

# License
This project is open-source and available.





