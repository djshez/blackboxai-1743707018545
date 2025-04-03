from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import json
import os
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load configuration
def load_config():
    try:
        with open('../config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning("Config file not found. Using default configuration.")
        return {
            "googleApiEndpoint": os.getenv("GOOGLE_API_ENDPOINT"),
            "projectId": os.getenv("GOOGLE_PROJECT_ID"),
            "botMode": "chat"
        }

config = load_config()

# Google API Authentication
def get_google_credentials():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            'path/to/service-account.json',
            scopes=['https://www.googleapis.com/auth/cloud-platform']
        )
        return credentials
    except Exception as e:
        logger.error(f"Error loading Google credentials: {e}")
        return None

# Initialize Google API client
def init_google_client():
    credentials = get_google_credentials()
    if credentials:
        try:
            service = build('aiplatform', 'v1', credentials=credentials)
            return service
        except Exception as e:
            logger.error(f"Error initializing Google API client: {e}")
    return None

# Error handler for all exceptions
@app.errorhandler(Exception)
def handle_error(error):
    logger.error(f"Unexpected error: {error}")
    return jsonify({
        "error": "An unexpected error occurred",
        "message": str(error)
    }), 500

# Health check endpoint
@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "mode": config.get("botMode", "chat")
    })

# Main interaction endpoint
@app.route('/interaction', methods=['POST'])
def handle_interaction():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({
                "error": "Invalid request",
                "message": "Message field is required"
            }), 400

        user_message = data['message']
        logger.info(f"Received message: {user_message}")

        # Process message and get response from Google AI
        response = process_message(user_message)
        
        return jsonify({
            "response": response,
            "timestamp": datetime.now().isoformat()
        })

    except Exception as e:
        logger.error(f"Error processing interaction: {e}")
        return jsonify({
            "error": "Processing error",
            "message": str(e)
        }), 500

# Training endpoint
@app.route('/train', methods=['POST'])
def handle_training():
    try:
        data = request.get_json()
        if not data or 'training_data' not in data:
            return jsonify({
                "error": "Invalid request",
                "message": "Training data is required"
            }), 400

        training_data = data['training_data']
        logger.info("Received training data")

        # Process training data
        training_result = process_training(training_data)
        
        return jsonify({
            "status": "success",
            "message": "Training data processed successfully",
            "result": training_result
        })

    except Exception as e:
        logger.error(f"Error processing training data: {e}")
        return jsonify({
            "error": "Training error",
            "message": str(e)
        }), 500

def process_message(message):
    """
    Process user message and integrate with Google AI
    """
    try:
        # Here we would typically:
        # 1. Preprocess the message
        # 2. Send to Google AI service
        # 3. Process the response
        # 4. Update learning model if necessary
        
        # Placeholder response
        return {
            "text": "I'm processing your message and learning from our interaction.",
            "confidence": 0.95,
            "learning_updates": {
                "new_patterns": 1,
                "model_version": "1.0.1"
            }
        }
    except Exception as e:
        logger.error(f"Error in message processing: {e}")
        raise

def process_training(training_data):
    """
    Process training data and update the model
    """
    try:
        # Here we would typically:
        # 1. Validate training data
        # 2. Preprocess data
        # 3. Send to Google AI service for model update
        # 4. Verify training success
        
        # Placeholder response
        return {
            "processed_entries": len(training_data),
            "model_updates": {
                "new_patterns": 2,
                "accuracy_improvement": "0.05"
            }
        }
    except Exception as e:
        logger.error(f"Error in training processing: {e}")
        raise

if __name__ == '__main__':
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    # Start server
    port = int(os.getenv('PORT', 8000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    logger.info(f"Starting Jaycie AI server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)