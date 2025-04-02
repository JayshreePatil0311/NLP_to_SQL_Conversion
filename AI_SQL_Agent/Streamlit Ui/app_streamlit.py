import streamlit as st
from database import connect_to_db
from ai_sql import convert_to_sql
import pandas as pd

# Streamlit UI
st.title("AI-Powered SQL Agent")
st.write("Enter your natural language query below and get the SQL query along with results.")

# User input
user_query = st.text_input("Enter your query:")

if st.button("Generate SQL and Execute"):
    if user_query:
        # Convert to SQL using AI
        sql_query = convert_to_sql(user_query)
        
        st.subheader("Generated SQL Query")
        st.code(sql_query, language="sql")
        
        # Execute SQL query
        conn = connect_to_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql_query)
                results = cursor.fetchall()
                
                # Fetch column names
                column_names = [desc[0] for desc in cursor.description]

                # Convert results to DataFrame
                df = pd.DataFrame(results, columns=column_names)
                
                st.subheader("Query Results")
                st.dataframe(df)  # Display results in a table format
                
                conn.close()
            except Exception as e:
                st.error(f"Error executing query: {e}")
        else:
            st.error("Database connection failed!")
    else:
        st.warning("Please enter a query.")

