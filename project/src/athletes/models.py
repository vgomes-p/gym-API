from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from contrib.models import BaseModel

class Athlete(BaseModel):
    __tablename__ = 'athletes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    login: Mapped[str] = mapped_column(String, unique=True, index=True)
    age: Mapped[int] = mapped_column(Integer)
    sex: Mapped[str] = mapped_column(String)
    measurements = relationship("Measurement", back_populates="athlete")
    routines = relationship("Routine", back_populates="athlete")