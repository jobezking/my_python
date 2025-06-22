#!/usr/bin/env_python3

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    """
    Handles requests to the root URL and returns a simple greeting.
    """
    return "<h1>Hello, Flask Application!</h1><p>This is a simple Python Flask app.</p>"

# Define another simple route
@app.route('/about')
def about():
    """
    Handles requests to the /about URL.
    """
    return "<h2>About This App</h2><p>This is a demonstration of a basic Flask web application.</p>"

# This block ensures the application runs only when executed directly (not imported)
if __name__ == '__main__':
    # Run the Flask application in debug mode.
    # In a production environment, you would use a production-ready WSGI server like Gunicorn.
    app.run(debug=True, host='0.0.0.0', port=5000)
