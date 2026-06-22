from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_products
from app.schemas import ProductListResponse
from typing import Optional

app = FastAPI(title="CodeVector Products API")

@app.get("/products", response_model=ProductListResponse)
def read_products(
    category: Optional[str] = Query(None),
    cursor: Optional[str] = Query(None),
    limit: int = Query(50, le=100),
    db: Session = Depends(get_db)
):
    return get_products(db, category, cursor, limit)

@app.get("/")
def root():
    return {"message": "API is running"}