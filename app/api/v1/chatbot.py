from fastapi import APIRouter
from app.models.chatbot import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/", response_model=ChatResponse)
async def get_response(chat_request: ChatRequest):
    user_message = chat_request.message
    # Generate a response (for simplicity, echo the message)
    response = f"Bot: I received your message: '{user_message}'. How can I assist you?"
    return ChatResponse(response=response)
