from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from contrib.models import BaseModel

class Measurement(BaseModel):
    __tablename__ = 'measurements'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    athlete_id: Mapped[int] = mapped_column(ForeignKey("athletes.id"))
    weight: Mapped[float] = mapped_column(Float)
    height: Mapped[float] = mapped_column(Float)
    neck: Mapped[float] = mapped_column(Float)
    shoulder: Mapped[float] = mapped_column(Float)
    chest: Mapped[float] = mapped_column(Float)
    biceps_right: Mapped[float] = mapped_column(Float)
    biceps_left: Mapped[float] = mapped_column(Float)
    forearm_right: Mapped[float] = mapped_column(Float)
    forearm_left: Mapped[float] = mapped_column(Float)
    abdomen: Mapped[float] = mapped_column(Float)
    waist: Mapped[float] = mapped_column(Float)
    hip: Mapped[float] = mapped_column(Float)
    thigh_right: Mapped[float] = mapped_column(Float)
    thigh_left: Mapped[float] = mapped_column(Float)
    calf_right: Mapped[float] = mapped_column(Float)
    calf_left: Mapped[float] = mapped_column(Float)
    athlete = relationship("Athlete", back_populates="measurements")