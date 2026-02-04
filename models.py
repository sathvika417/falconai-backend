from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Chat(BaseModel):
    title: str
    created_at: datetime = datetime.utcnow()

class Message(BaseModel):
    chat_id: str
    role: str  # "user" or "ai"
    content: str
    timestamp: datetime = datetime.utcnow()
