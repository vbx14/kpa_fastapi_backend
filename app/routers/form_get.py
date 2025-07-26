from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import WheelSpecification
from app.schemas import WheelSpecResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/formdata", response_model=WheelSpecResponse)
def get_form(
    formNumber: str = Query(...),
    submittedBy: str = Query(...),
    submittedDate: str = Query(...),
    db: Session = Depends(get_db),
):
    form = db.query(WheelSpecification).filter(
        WheelSpecification.formNumber == formNumber,
        WheelSpecification.submittedBy == submittedBy,
        WheelSpecification.submittedDate == submittedDate
    ).first()
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    return form
