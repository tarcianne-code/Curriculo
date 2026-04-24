from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, User

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"msg": "API rodando"}

@app.post("/users")
def create_user(name: str, email: str):
    db = SessionLocal()
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users")
def list_users():
    db = SessionLocal()
    return db.query(User).all()
