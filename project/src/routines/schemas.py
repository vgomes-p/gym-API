from typing import Annotated
from pydantic import Field, PositiveFloat, PositiveInt
from contrib.schemas import BaseSchema

class RoutineCreate(BaseSchema):
    athlete_id: Annotated[PositiveInt, Field(description="Athlete ID", example=1)]
    name: Annotated[str, Field(description="Routine name", example="Full Body", max_length=100)]
    exercises: Annotated[str, Field(description="Exercises", example="Squats, Bench Press")]
    volume: Annotated[PositiveFloat, Field(description="Total volume", example=10000.0)]
    time: Annotated[PositiveFloat, Field(description="Time", example=60.0)]
    muscles_worked: Annotated[str, Field(description="Muscles worked", example="Legs, Chest")]