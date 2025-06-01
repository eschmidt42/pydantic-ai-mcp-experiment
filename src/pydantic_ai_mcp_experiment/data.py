from pydantic import BaseModel


class CityLocation(BaseModel):
    city: str
    country: str
