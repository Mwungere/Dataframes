from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Product

router = APIRouter()

@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
