from sqlmodel import Field, SQLModel
from datetime import datetime

class MOTDBase(SQLModel):
    motd: str

class MOTD(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    creator: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
