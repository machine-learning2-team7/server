from pydantic import BaseModel


class Input(BaseModel):
    lang: str
    text: str
