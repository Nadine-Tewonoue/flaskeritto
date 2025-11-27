from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    """Renders the main status page."""
    # Flask looks for templates in a sub-folder named 'templates'
    return render_template('index.html')

# This block ensures the application runs when executed directly
if __name__ == '__main__':
    # Use 0.0.0.0 to listen on all public IPs, necessary for Docker
    app.run(host='0.0.0.0', port=80)