# Chatbot Web Application

This project is a simple and secure chatbot web application built using Flask. The chatbot interacts with a generative language API to provide intelligent responses to user input. The front end is built with HTML, CSS, and JavaScript, providing a clean and user-friendly interface.

## Features

- **Chat Interface**: A sleek chat interface where users can send messages and receive AI-powered responses.
- **Responsive Design**: The web application is designed to be fully responsive, meaning it works seamlessly across various devices (PC, tablet, mobile).
- **API Integration**: The app connects to a generative language API to process and respond to user messages.
- **Environment Variables**: Sensitive information like API keys is stored securely in a `.env` file.

## Technologies Used

- **Flask**: A lightweight Python web framework used for building the backend API.
- **HTML/CSS/JavaScript**: Used for building the responsive front-end interface.
- **Generative Language API**: A powerful external API that generates AI-driven responses to user input.
- **.env**: To securely store the API key.

## Installation

Follow these steps to get your project up and running:

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/chatbot-web-app.git
```

### 2. Navigate to the project directory

```bash
cd chatbot-web-app
```

### 3. Install dependencies

Make sure you have `pip` installed and run:

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root directory and add your API key like this:

```bash
API_KEY=your_api_key_here
```

### 5. Run the application

Start the Flask development server:

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to interact with the chatbot.

## How It Works

1. The user sends a message through the chat interface.
2. The message is sent to the Flask backend.
3. The backend sends the message to the generative language API to get a response.
4. The response is sent back to the frontend, and the chatbot displays the answer.

## Contributing

We welcome contributions to this project! If you'd like to improve it or add new features, please feel free to fork the repository and create a pull request.

## License

This project is open-source and available under the MIT License.

## Contact

If you have any questions or need help with the project, feel free to open an issue or contact us directly.

Happy coding! 😊
