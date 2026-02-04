from database import chat_collection

chat_collection.insert_one({"test": "connected"})
print("MongoDB Atlas connected successfully")