from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.record import Record
from app.utils.role_checker import require_roles

router = APIRouter(prefix="/dashboard")

@router.get("/summary")
def get_summary(
    db: Session = Depends(get_db),
    user=Depends(require_roles(["admin", "analyst"]))
):
    records = db.query(Record).all()

    total_income = sum(r.amount for r in records if r.type == "income")
    total_expense = sum(r.amount for r in records if r.type == "expense")

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense
    }