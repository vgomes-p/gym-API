from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi_pagination import Page, paginate

from contrib.database import get_db
from .models import Athlete
from .schemas import AthleteCreate, AthleteResponse

router = APIRouter(prefix="/athletes", tags=["athletes"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_athlete(athlete: AthleteCreate, db: Session = Depends(get_db)):
    db_athlete = Athlete(**athlete.dict())
    try:
        db.add(db_athlete)
        db.commit()
        db.refresh(db_athlete)
        return db_athlete
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Already exists an athlete registered with login: {athlete.login}")

@router.get("/", response_model=Page[AthleteResponse])
def get_athletes(
    name: Optional[str] = Query(None),
    login: Optional[str] = Query(None),
    age: Optional[int] = Query(None),
    sex: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    stmt = select(Athlete)
    if name:
        stmt = stmt.where(Athlete.name == name)
    if login:
        stmt = stmt.where(Athlete.login == login)
    if age:
        stmt = stmt.where(Athlete.age == age)
    if sex:
        stmt = stmt.where(Athlete.sex == sex)
    athletes = db.scalars(stmt).all()
    response = [
        AthleteResponse(
            name=a.name,
            gym="Example Gym",
            routine=a.routines[0].name if a.routines else None
        ) for a in athletes
    ]
    return paginate(response)