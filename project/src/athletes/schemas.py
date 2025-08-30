from typing import Annotated, Optional
from pydantic import Field
from contrib.schemas import BaseSchema

class AthleteCreate(BaseSchema):
    name: Annotated[str, Field(description="Athlete's name", example="John Doe", max_length=100)]
    login: Annotated[str, Field(description="Athlete's login", example="johndoe", max_length=50)]
    age: Annotated[int, Field(description="Athlete's age", example=25)]
    sex: Annotated[str, Field(description="Athlete's sex", example="M", max_length=1)]

class AthleteResponse(BaseSchema):
    name: str
    gym: Optional[str] = None
    routine: Optional[str] = None