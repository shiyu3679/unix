from sqlalchemy.orm import Session
from app.models.order import DBOrder, OrderCreate
from app.utils.main import generate_random
from datetime import datetime

# 创建订单
def create_order(db: Session, user_id: int, order: OrderCreate):
    # 生成订单号
    order_no = f"ORD{datetime.now().strftime('%Y%m%d%H%M%S')}{generate_random(6, '')}"
    
    # 创建订单对象
    db_order = DBOrder(
        order_no=order_no,
        total_amount=order.total_amount,
        user_id=user_id
    )
    
    try:
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return {"code": 200, "msg": "订单创建成功", "data": db_order, "success": True}
    except Exception as e:
        db.rollback()
        return {"code": 400, "msg": f"订单创建失败：{str(e)}"}

# 获取用户的所有订单
def get_user_orders(db: Session, user_id: int):
    orders = db.query(DBOrder).filter(DBOrder.user_id == user_id).all()
    return {"code": 200, "msg": "查询成功", "data": orders, "success": True}

# 获取订单详情（包含用户信息）
def get_order_with_user(db: Session, order_id: int):
    order = db.query(DBOrder).filter(DBOrder.id == order_id).first()
    if not order:
        return {"code": 400, "msg": "订单不存在"}
    
    # 通过关联关系获取用户信息
    order_data = {
        "id": order.id,
        "order_no": order.order_no,
        "total_amount": order.total_amount,
        "status": order.status,
        "create_time": order.create_time,
        "user": {
            "id": order.user.id,
            "username": order.user.username,
            "email": order.user.email
        }
    }
    
    return {"code": 200, "msg": "查询成功", "data": order_data, "success": True}

def refund_order(db: Session, order_id: int):
    order = db.query(DBOrder).filter(DBOrder.id == order_id).first()
    if not order:
        return {"code": 400, "msg": "订单不存在", "success": False}
    return {"code": 200, "msg": "查询成功", "data": order, "success": True}