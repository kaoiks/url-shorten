from pydantic import BaseModel


# pydantic models

class UrlBase(BaseModel):
    hash_url: str
    original_url: str


class UrlCreate(BaseModel):
    url: str


class Url(UrlBase):
    pass

    class Config:
        orm_mode = True
