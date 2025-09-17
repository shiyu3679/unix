from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import UserLogin, UserRegister, UserForgetPassword
from app.services.sign_service import login, register, forget_password
from app.database import db_session

router = APIRouter()

@router.post("/login", name="登录")
async def login_user(user: UserLogin, db: Session = Depends(db_session)):
    return login(db, user)

@router.post("/register", name="注册")
async def register_user(user: UserRegister, db: Session = Depends(db_session)):
    return register(db, user)

@router.post("/forget_password", name="忘记密码")
async def forget_password_user(user: UserForgetPassword, db: Session = Depends(db_session)):
    return forget_password(db, user)
