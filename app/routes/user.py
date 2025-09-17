from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.services.user_service import get_user, update_user_info
from app.database import db_session

router = APIRouter()

@router.get("/{user_id}", name="获取用户")
async def read_user(user_id: int, db: Session = Depends(db_session)):
    return get_user(db, user_id)

@router.put("/{user_id}", name="修改用户信息")
async def update_user(user_id: int, user: User, db: Session = Depends(db_session)):
    return update_user_info(db, user_id, user)
