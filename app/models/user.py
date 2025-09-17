from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship  # 新增导入
from app.database import Base
from pydantic import BaseModel

# 数据库模型
class DBUser(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), index=True)
    avatar = Column(String(100), nullable=True)
    gender = Column(Integer, default=2, nullable=True, comment="用户性别, 1: 男, 0: 女, 2: 未知")
    phone = Column(String(11), unique=True, nullable=True)
    birthday = Column(String(10), nullable=True)
    status = Column(Integer)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))
    
    # 关系定义：一个用户可以有多个订单
    orders = relationship("DBOrder", back_populates="user", cascade="all, delete-orphan")

# Pydantic模型
class User(BaseModel):
    username: str = None
    avatar: str = None
    gender: int = None
    phone: str = None
    birthday: str = None
    status: int = 1
    email: str = None
    age: int = None

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: str
    password: str
    class Config:
        orm_mode = True

class UserRegister(BaseModel):
    email: str
    password: str
    code: str
    class Config:
        orm_mode = True

class UserForgetPassword(BaseModel):
    email: str
    password: str
    code: str
    class Config:
        orm_mode = True
