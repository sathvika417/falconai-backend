from fastapi import APIRouter, HTTPException
from database import chat_collection,message_collection
from models import Chat
from ai import get_ai_response

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/chat")
async def create_chat(chat: Chat):
    try:
        data = chat.dict()
        print("INSERTING DATA 👉", data)

        result = await chat_collection.insert_one(data)
        print("INSERT SUCCESS 👉", result.inserted_id)

        return {"chat_id": str(result.inserted_id)}

    except Exception as e:
        print("🔥 MONGODB ERROR 👉", e)
        raise HTTPException(status_code=500, detail=str(e))
    from ai import get_ai_response
from models import Message

@router.post("/chat/ai")
async def chat_with_ai(message: Message):
    # Get AI reply
    ai_reply = await get_ai_response(message.content)

    # Save user message
    message_collection.insert_one(message.dict())

    # Save AI message
    message_collection.insert_one({
        "chat_id": message.chat_id,
        "role": "ai",
        "content": ai_reply
    })

    return {"reply": ai_reply}