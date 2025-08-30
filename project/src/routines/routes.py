from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List, Optional

from contrib.database import get_db
from .models import Routine
from .schemas import RoutineCreate

router = APIRouter(prefix="/routines", tags=["routines"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_routine(routine: RoutineCreate, db: Session = Depends(get_db)):
    db_routine = Routine(**routine.dict())
    try:
        db.add(db_routine)
        db.commit()
        db.refresh(db_routine)
        return db_routine
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail="Data integrity error in routines")

@router.get("/")
def get_routines(
    athlete_id: Optional[int] = Query(None),
    name: Optional[str] = Query(None),
    exercises: Optional[str] = Query(None),
    volume: Optional[float] = Query(None),
    time: Optional[float] = Query(None),
    muscles_worked: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    stmt = select(Routine)
    if athlete_id:
        stmt = stmt.where(Routine.athlete_id == athlete_id)
    if name:
        stmt = stmt.where(Routine.name == name)
    if exercises:
        stmt = stmt.where(Routine.exercises == exercises)
    if volume:
        stmt = stmt.where(Routine.volume == volume)
    if time:
        stmt = stmt.where(Routine.time == time)
    if muscles_worked:
        stmt = stmt.where(Routine.muscles_worked == muscles_worked)
    return db.scalars(stmt).all()