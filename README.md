
# Simple Chatbot with FastAPI

This project is a simple chatbot API built with [FastAPI](https://fastapi.tiangolo.com/). The chatbot responds to user messages with predefined responses and demonstrates basic API-first development principles, making it an excellent foundation for more advanced chatbot functionality.

## Features

- **API-First Development**: Built following the API-first approach, ensuring that the API structure is well-defined and organized.
- **Simple Responses**: Returns a basic response to user messages (can be extended with AI or NLP models).
- **Easy Deployment**: Containerized with Docker, making it easy to deploy on various platforms.

## Prerequisites

- Python 3.7+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server for FastAPI)
- Docker (optional, for containerized deployment)

## Project Structure

```
chatbot/
│
├── app/
│   ├── main.py               # Main entry point for the FastAPI application
│   ├── api/
│   │   └── v1/
│   │       └── chatbot.py     # Chatbot API routes
│   └── models/
│       └── chatbot.py         # Data models for the chatbot API
├── requirements.txt           # Required Python packages
└── Dockerfile                 # Dockerfile for containerizing the app
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/simplechatbotfastapi.git
cd simplechatbotfastapi
```

### 2. Create a Virtual Environment and Install Dependencies

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   ```bash
   # On Windows
   venv\Scripts\activate

   # On MacOS/Linux
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### 3. Run the Application

Use Uvicorn to run the FastAPI app:

```bash
uvicorn app.main:app --reload
```

The API should now be available at `http://127.0.0.1:8000`.

### 4. Test the Chatbot API

You can test the API by sending a POST request to the `/api/v1/chatbot/` endpoint.

#### Example Request

Using `curl`:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/chatbot/' \
  -H 'Content-Type: application/json' \
  -d '{
  "message": "Hello, chatbot!"
}'
```

#### Expected Response

```json
{
  "response": "Bot: I received your message: 'Hello, chatbot!'. How can I assist you?"
}
```

## Project Files

### app/main.py

This file initializes the FastAPI app and includes the chatbot API router.

```python
from fastapi import FastAPI
from app.api.v1.chatbot import router as chatbot_router

app = FastAPI()

# Include the chatbot API
app.include_router(chatbot_router, prefix="/api/v1/chatbot", tags=["chatbot"])
```

### app/api/v1/chatbot.py

Defines the `/api/v1/chatbot/` endpoint, which takes a user message and returns a simple chatbot response.

```python
from fastapi import APIRouter
from app.models.chatbot import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/", response_model=ChatResponse)
async def get_response(chat_request: ChatRequest):
    user_message = chat_request.message
    response = f"Bot: I received your message: '{user_message}'. How can I assist you?"
    return ChatResponse(response=response)
```

### app/models/chatbot.py

Contains Pydantic models to define the request and response structure.

```python
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
```

### Dockerfile

A Dockerfile to containerize the FastAPI application.

```dockerfile
# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory into the container
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Deployment with Docker

To deploy this project using Docker:

1. Build the Docker image:

   ```bash
   docker build -t chatbot-fastapi .
   ```

2. Run the Docker container:

   ```bash
   docker run -d -p 8000:8000 chatbot-fastapi
   ```

The application will be accessible at `http://localhost:8000`.

## Deployment to Cloud (Optional)

You can deploy this FastAPI app on cloud platforms like AWS, Azure, or Heroku. For Heroku deployment, initialize a Git repository and follow these commands:

```bash
heroku create your-app-name
git push heroku main
```

## Contributing

If you would like to contribute to this project, please feel free to fork the repository and submit a pull request.

## Contact

If you need a reliable backend solution for your projects, feel free to reach out. I’d be happy to help you build a robust and scalable backend tailored to your needs.
