from sqlalchemy.orm import Session
from app.models import Product
from typing import Optional

def get_products(db: Session, category: Optional[str], cursor: Optional[str], limit: int = 50):
    query = db.query(Product)

    if category:
        query = query.filter(Product.category == category)

    if cursor:
        created_at_str, id_str = cursor.split("_")
        query = query.filter(
            (Product.created_at, Product.id) < (created_at_str, id_str)
        )

    products = query.order_by(Product.created_at.desc(), Product.id.desc()).limit(limit + 1).all()

    next_cursor = None
    if len(products) > limit:
        last_product = products[limit - 1]
        next_cursor = f"{last_product.created_at.isoformat()}_{last_product.id}"
        products = products[:limit]

    return {"data": products, "next_cursor": next_cursor}