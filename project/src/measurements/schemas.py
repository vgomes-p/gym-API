from typing import Annotated
from pydantic import Field, PositiveFloat, PositiveInt
from contrib.schemas import BaseSchema

class MeasurementCreate(BaseSchema):
    athlete_id: Annotated[PositiveInt, Field(description="Athlete ID", example=1)]
    weight: Annotated[PositiveFloat, Field(description="Weight", example=75.0)]
    height: Annotated[PositiveFloat, Field(description="Height", example=1.75)]
    neck: Annotated[PositiveFloat, Field(description="Neck", example=40.0)]
    shoulder: Annotated[PositiveFloat, Field(description="Shoulder", example=120.0)]
    chest: Annotated[PositiveFloat, Field(description="Chest", example=100.0)]
    biceps_right: Annotated[PositiveFloat, Field(description="Biceps right", example=35.0)]
    biceps_left: Annotated[PositiveFloat, Field(description="Biceps left", example=35.0)]
    forearm_right: Annotated[PositiveFloat, Field(description="Forearm right", example=28.0)]
    forearm_left: Annotated[PositiveFloat, Field(description="Forearm left", example=28.0)]
    abdomen: Annotated[PositiveFloat, Field(description="Abdomen", example=80.0)]
    waist: Annotated[PositiveFloat, Field(description="Waist", example=75.0)]
    hip: Annotated[PositiveFloat, Field(description="Hip", example=95.0)]
    thigh_right: Annotated[PositiveFloat, Field(description="Thigh right", example=55.0)]
    thigh_left: Annotated[PositiveFloat, Field(description="Thigh left", example=55.0)]
    calf_right: Annotated[PositiveFloat, Field(description="Calf right", example=38.0)]
    calf_left: Annotated[PositiveFloat, Field(description="Calf left", example=38.0)]