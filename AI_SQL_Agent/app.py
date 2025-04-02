from flask import Flask, request, jsonify
from query_executor import execute_query  # Import query execution function

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the AI SQL Agent! Use the '/query' endpoint to interact."

@app.route('/query', methods=['POST'])
def query_database():
    """Process natural language queries and return SQL execution results."""
    data = request.get_json()
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({"error": "No query provided"}), 400
    
    result = execute_query(user_query)
    return jsonify({"result": result})

if _name_ == "_main_":
    app.run(debug=True)