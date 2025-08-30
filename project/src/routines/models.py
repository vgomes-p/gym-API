from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from contrib.models import BaseModel

class Routine(BaseModel):
    __tablename__ = 'routines'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    athlete_id: Mapped[int] = mapped_column(ForeignKey("athletes.id"))
    name: Mapped[str] = mapped_column(String)
    exercises: Mapped[str] = mapped_column(String)
    volume: Mapped[float] = mapped_column(Float)
    time: Mapped[float] = mapped_column(Float)
    muscles_worked: Mapped[str] = mapped_column(String)
    athlete = relationship("Athlete", back_populates="routines")