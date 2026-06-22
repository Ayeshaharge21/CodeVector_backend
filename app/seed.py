from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models import Product
from faker import Faker
import random

fake = Faker()

# Ensure database tables are created
Base.metadata.create_all(bind=engine)

def seed_products(total=200000, batch_size=5000):
    """
    Seeds the database with dummy product data for performance testing.
    Uses batch inserts to optimize performance and reduce memory usage.
    """
    db: Session = SessionLocal()
    
    categories = ["Electronics", "Fashion", "Home", "Books", "Sports", "Beauty", "Grocery", "Toys"]
    
    try:
        print(f"Starting database seeding process for {total:,} products...")
        
        for i in range(0, total, batch_size):
            products = []
            for _ in range(batch_size):
                product = Product(
                    name=fake.catch_phrase(),
                    description=fake.text(max_nb_chars=200),
                    price=round(random.uniform(99.0, 9999.0), 2),
                    stock=random.randint(0, 500),
                    category=random.choice(categories),
                    rating=round(random.uniform(3.0, 5.0), 1)
                )
                products.append(product)
            
            db.bulk_save_objects(products)
            db.commit()
            print(f"Successfully inserted {i + batch_size:,} / {total:,} products")
    
    except Exception as e:
        db.rollback()
        print(f"Error occurred during seeding: {e}")
        raise
    finally:
        db.close()
        print("Database seeding completed successfully. All products have been added.")

if __name__ == "__main__":
    seed_products()