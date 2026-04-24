from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, Order

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"msg": "API Orders rodando"}

@app.post("/orders")
def create_order(product: str):
    db = SessionLocal()
    order = Order(product=product)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@app.get("/orders")
def list_orders():
    db = SessionLocal()
    return db.query(Order).all()

@app.patch("/orders/{order_id}/pay")
def pay_order(order_id: int):
    db = SessionLocal()
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        return {"erro": "Pedido não encontrado"}

    order.status = "pago"
    db.commit()
    return order

@app.patch("/orders/{order_id}/deliver")
def deliver_order(order_id: int):
    db = SessionLocal()
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        return {"erro": "Pedido não encontrado"}

    if order.status != "pago":
        return {"erro": "Pedido não pode ser entregue sem pagamento"}

    order.status = "entregue"
    db.commit()
    return order
