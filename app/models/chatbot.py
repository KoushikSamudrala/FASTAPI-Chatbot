from pydantic import BaseModel

# Model for the incoming request to the chatbot
class ChatRequest(BaseModel):
    message: str  # The message from the user

# Model for the outgoing response from the chatbot
class ChatResponse(BaseModel):
    response: str  # The response message from the bot
