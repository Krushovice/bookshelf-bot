from pydantic import BaseModel, ConfigDict


class ReaderBase(BaseModel):
    username: str
    first_name: str
    last_name: str


class ReaderCreate(ReaderBase):
    pass


class ReaderUpdate(ReaderCreate):
    pass


class ReaderUpdatePartial(ReaderCreate):
    usernname: str | None = None
    first_name: str | None = None
    last_name: str | None = None


class Reader(ReaderBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
