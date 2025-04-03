# Jaycie AI - Autonomic Self-Learning Bot

Jaycie is an advanced AI chatbot that integrates with Google's mainframe server for autonomous learning and natural language processing capabilities. The system features both a modern web interface and a robust backend server that handles AI processing and learning capabilities.

## Features

- 🤖 Real-time chat interface with modern UI
- 🧠 Self-learning capabilities integrated with Google AI
- 💾 Message history and context awareness
- 🔄 Autonomous learning from user interactions
- 🎨 Modern, responsive design with glassmorphism effects
- ⚡ Real-time typing indicators and animations

## Project Structure

```
jaycie/
├── backend/
│   └── server.py           # Flask backend server
├── js/
│   └── main.js            # Frontend JavaScript
├── config.json            # Configuration settings
├── requirements.txt       # Python dependencies
└── index.html            # Main web interface
```

## Prerequisites

- Python 3.8 or higher
- Node.js 14.x or higher (for development)
- Google Cloud Platform account with AI Platform access
- Modern web browser

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jaycie-ai.git
cd jaycie-ai
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Configure Google Cloud credentials:
- Create a service account in Google Cloud Console
- Download the service account key JSON file
- Set the environment variable:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account.json"
```

4. Configure the application:
- Copy `config.json.example` to `config.json`
- Update the configuration values as needed
- Set sensitive values in environment variables

## Running the Application

1. Start the backend server:
```bash
cd backend
python server.py
```

2. Access the web interface:
- Open `index.html` in your web browser
- Or serve it using Python's built-in server:
```bash
python -m http.server 8000
```

The application will be available at `http://localhost:8000`

## Development

### Backend Development

The backend is built with Flask and handles:
- API endpoints for chat interactions
- Integration with Google AI Platform
- Message processing and learning capabilities
- Error handling and logging

### Frontend Development

The frontend features:
- Modern UI with Tailwind CSS
- Real-time chat interface
- Responsive design
- Smooth animations and transitions

## API Endpoints

### GET /status
- Returns the current status of the service
- Response includes server health and bot mode

### POST /interaction
- Handles chat interactions
- Request body: `{ "message": "user message" }`
- Returns AI response and learning updates

### POST /train
- Handles training data submissions
- Request body: `{ "training_data": [...] }`
- Returns training results and model updates

## Configuration

The `config.json` file contains settings for:
- Google API endpoints
- Server configuration
- AI model parameters
- Frontend settings
- Logging preferences
- Security settings

## Security Considerations

- API keys and sensitive data should be stored in environment variables
- CORS is enabled with configurable allowed origins
- Rate limiting is implemented to prevent abuse
- Input validation is performed on all endpoints

## Error Handling

The application implements comprehensive error handling:
- Backend errors are logged and return appropriate HTTP status codes
- Frontend displays user-friendly error messages
- Network connectivity issues are handled gracefully

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the development team.

## Acknowledgments

- Google Cloud Platform for AI services
- Tailwind CSS for styling
- Font Awesome for icons
- The open-source community for various tools and libraries