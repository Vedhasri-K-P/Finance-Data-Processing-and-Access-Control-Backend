from pydantic import BaseModel

class RecordCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: str
    note: str

class RecordResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str

    class Config:
        from_attributes = True