from typing import List, Dict, Any
from pydantic import BaseModel

class ClientMessage(BaseModel):
    role: str
    content: str

def convert_to_openai_messages(messages: List[ClientMessage]) -> List[Dict[str, Any]]:
    return [message.model_dump() for message in messages]
