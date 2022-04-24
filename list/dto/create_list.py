from pydantic import BaseModel


class CreateList(BaseModel):
    title: str
    description: str
