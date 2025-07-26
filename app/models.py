from sqlalchemy import Column, String, JSON
from app.database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    formNumber = Column(String, primary_key=True)
    submittedBy = Column(String, primary_key=True)
    submittedDate = Column(String, primary_key=True)
    fields = Column(JSON, nullable=False)