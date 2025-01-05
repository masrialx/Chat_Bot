from flask import Flask, request, jsonify, render_template
import requests
import uuid
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# External API details
api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
api_key = os.getenv("API_KEY")  # Fetch API key from environment variable

# Route to render the chatbot UI (HTML)
@app.route('/')
def index():
    return render_template('index.html')  # Renders the HTML file from the 'templates' folder

# Chat creation endpoint
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    title = data.get('title', 'General')

    if not message:
        return jsonify({"error": "Message is required"}), 400

    # Prepare request to external API
    payload = {
        "contents": [
            {"parts": [{"text": message}]}
        ]
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(f"{api_url}?key={api_key}", json=payload, headers=headers)

    # Log the response from the external API
    print(f"External API response: {response.status_code} - {response.text}")

    if response.status_code != 200:
        return jsonify({"error": "Failed to get response from API"}), 500

    response_data = response.json()
    chat_response = response_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', 'No response')

    return jsonify({
        "conversation_id": str(uuid.uuid4()),  # Generate unique conversation ID
        "message": message,
        "response": chat_response
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
