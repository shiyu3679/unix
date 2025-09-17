from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
from pydantic import BaseModel

# 数据库模型
class DBOrder(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_no = Column(String(50), unique=True, index=True)
    total_amount = Column(Float, default=0.0)
    status = Column(Integer, default=1)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    # 外键定义：关联到user表的id字段
    user_id = Column(Integer, ForeignKey("user.id"))
    
    # 关系定义：一个订单属于一个用户
    user = relationship("DBUser", back_populates="orders")

# Pydantic模型
class Order(BaseModel):
    order_no: str
    total_amount: float
    status: int = 1
    
    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    total_amount: float
    
    class Config:
        orm_mode = True