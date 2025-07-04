from pydantic import BaseModel
from typing import Literal

class GenerateRequest(BaseModel):
    prompt: str
    media_type: Literal["image", "video"]