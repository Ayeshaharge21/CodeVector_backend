from sqlalchemy import Column, Integer, String, Numeric, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False, index=True)
    price = Column(Numeric(10, 2), nullable=False)
    description = Column(String(1000), nullable=True)
    stock = Column(Integer, nullable=True, default=0)
    rating = Column(Numeric(3, 2), nullable=True, default=4.5)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        Index('idx_created_id', 'created_at', 'id'),
        Index('idx_category_created_id', 'category', 'created_at', 'id'),
    )