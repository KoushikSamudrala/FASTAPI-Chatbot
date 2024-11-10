from fastapi import FastAPI
from app.api.v1.chatbot import router as chatbot_router

app = FastAPI()

# Include the chatbot API
app.include_router(chatbot_router, prefix="/api/v1/chatbot", tags=["chatbot"])
