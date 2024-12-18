from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User, Product
from faker import Faker

fake = Faker()

def seed_database():
    db: Session = SessionLocal()
    try:
        users = []
        products = []

        # Generate 500,000 users
        for _ in range(500_000):
            users.append(User(name=fake.name(), email=fake.unique.email()))

        db.bulk_save_objects(users)
        db.commit()

        # Generate 500,000 products
        user_ids = db.query(User.id).all()
        for user_id in user_ids:
            products.append(
                Product(
                    name=fake.word(),
                    price=fake.random_int(min=1, max=1000),
                    owner_id=user_id[0]
                )
            )

        db.bulk_save_objects(products)
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
