from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, Task

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"msg": "API Tasks rodando"}

@app.post("/tasks")
def create_task(title: str):
    db = SessionLocal()
    task = Task(title=title)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.get("/tasks")
def list_tasks():
    db = SessionLocal()
    return db.query(Task).all()

@app.patch("/tasks/{task_id}/done")
def finish_task(task_id: int):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"erro": "Task não encontrada"}

    task.status = "concluida"
    db.commit()
    return task
