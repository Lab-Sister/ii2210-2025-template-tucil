from sqlmodel import Field, SQLModel
from datetime import datetime

class MOTD(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    motd: str
    creator: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
