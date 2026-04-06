from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.record import Record
from app.schemas.record_schema import RecordCreate
from app.utils.role_checker import require_roles

router = APIRouter()

@router.post("/records")
def create_record(record: RecordCreate, db: Session = Depends(get_db)):
    db_record = Record(**record.dict(), created_by=1)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

@router.get("/records")
def get_records(db: Session = Depends(get_db)):
    return db.query(Record).all()

@router.post("/records")
def create_record(
    record: RecordCreate,
    db: Session = Depends(get_db),
    user=Depends(require_roles(["admin"]))
):
    db_record = Record(**record.dict(), created_by=user["id"])
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


@router.get("/records")
def get_records(
    db: Session = Depends(get_db),
    user=Depends(require_roles(["admin", "analyst", "viewer"]))
):
    return db.query(Record).all()

@router.delete("/records/{id}")
def delete_record(
    id: int,
    db: Session = Depends(get_db),
    user=Depends(require_roles(["admin"]))
):
    record = db.query(Record).filter(Record.id == id).first()
    db.delete(record)
    db.commit()
    return {"message": "Deleted"}

