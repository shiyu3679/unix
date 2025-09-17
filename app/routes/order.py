from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import db_session
from app.models.order import OrderCreate
from app.services.order_service import create_order, get_user_orders, get_order_with_user

router = APIRouter()

@router.post("/create", name="创建订单")
def create_new_order(
    order: OrderCreate,
    user_id: int = 1,  # 实际应用中应该从认证获取用户ID
    db: Session = Depends(db_session)
):
    return create_order(db, user_id, order)

@router.get("/user/{user_id}", name="获取用户订单")
def get_orders_by_user(
    user_id: int,
    db: Session = Depends(db_session)
):
    return get_user_orders(db, user_id)

@router.get("/{order_id}", name="获取订单详情")
def get_order_detail(
    order_id: int,
    db: Session = Depends(db_session)
):
    return get_order_with_user(db, order_id)