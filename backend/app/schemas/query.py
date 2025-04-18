from pydantic import BaseModel

class QueryCreate(BaseModel):
    query: str

