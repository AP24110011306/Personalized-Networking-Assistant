from pydantic import BaseModel

class UserRequest(BaseModel):
    event: str
    interests: str

class FeedbackRequest(BaseModel):
    event: str
    feedback: str
