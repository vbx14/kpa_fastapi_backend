from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import WheelSpecification
from app.schemas import WheelSpecCreate, WheelSpecResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/formdata", response_model=WheelSpecResponse)
def create_form(data: WheelSpecCreate, db: Session = Depends(get_db)):
    form = WheelSpecification(**data.dict())
    db.add(form)
    db.commit()
    return form
