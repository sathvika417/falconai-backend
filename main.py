from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.chat import router as chat_router  # 👈 IMPORTANT

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    # Allow all origins for local network development. Replace with specific origins in production.
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROOT (optional)
@app.get("/")
def root():
    return {"message": "FalconAI backend is running 🚀"}

# 👇 THIS WAS MISSING
app.include_router(chat_router)