from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List, Optional

from contrib.database import get_db
from .models import Measurement
from .schemas import MeasurementCreate

router = APIRouter(prefix="/measurements", tags=["measurements"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_measurement(measurement: MeasurementCreate, db: Session = Depends(get_db)):
    db_measurement = Measurement(**measurement.dict())
    try:
        db.add(db_measurement)
        db.commit()
        db.refresh(db_measurement)
        return db_measurement
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail="Data integrity error in measurements")

@router.get("/")
def get_measurements(
    athlete_id: Optional[int] = Query(None),
    weight: Optional[float] = Query(None),
    height: Optional[float] = Query(None),
    db: Session = Depends(get_db)
):
    stmt = select(Measurement)
    if athlete_id:
        stmt = stmt.where(Measurement.athlete_id == athlete_id)
    if weight:
        stmt = stmt.where(Measurement.weight == weight)
    if height:
        stmt = stmt.where(Measurement.height == height)
    return db.scalars(stmt).all()