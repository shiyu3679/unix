from sqlalchemy.orm import Session
from app.models.user import DBUser, User

def get_user(db: Session, id: int):
    db_user = db.query(DBUser).filter(DBUser.id == id).first()
    if not db_user:
        return {"code": 400, "msg": "用户不存在", "success": False}
    return {"code": 200, "msg": "获取用户成功", "data": db_user, "success": True}

def update_user_info(db: Session, user_id: int, user: User):
    db_user = get_user(db, user_id)
    if db_user["success"] is False:
        return {"code": 400, "msg": "用户不存在", "success": False}
    if user.username:
        db_user["data"].username = user.username
    if user.avatar:
        db_user["data"].avatar = user.avatar
    if user.gender:
        db_user["data"].gender = user.gender
    if user.phone:
        db_user["data"].phone = user.phone
    if user.birthday:
        db_user["data"].birthday = user.birthday
    if user.status:
        db_user["data"].status = user.status
    if user.email:
        db_user["data"].email = user.email
    try:
        db.commit()
        db.refresh(db_user["data"])
    except Exception as e:
        db.rollback()
        return {"code": 500, "msg": "更新用户信息失败", "success": False}
    return {"code": 200, "msg": "更新用户信息成功", "success": True}
