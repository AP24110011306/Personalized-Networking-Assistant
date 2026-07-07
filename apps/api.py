from fastapi import FastAPI
from pydantic import BaseModel

from theme_classifier import classify_theme
from conversation_generator import generate_conversation
from fact_checker import fact_check
from history_logger import save_history

app = FastAPI(title="Personalized Networking Assistant")


class UserRequest(BaseModel):
    event: str
    interests: str


@app.get("/")
def home():
    return {"message": "Personalized Networking Assistant API is running"}


@app.post("/generate")
def generate(request: UserRequest):
    themes = classify_theme(request.event)

    starters = generate_conversation(
        request.event,
        request.interests,
        themes
    )

    facts = fact_check(request.event)

    save_history(
        request.event,
        request.interests,
        starters
    )

    return {
        "themes": themes,
        "conversation_starters": starters,
        "fact_check": facts
    }
