from pydantic import BaseModel, ConfigDict

class LinkCreate(BaseModel):
    original_url: str

class LinkResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    original_url: str
    short_code: str
    clicks: int