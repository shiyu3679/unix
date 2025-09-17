from sqlalchemy.orm import Session
from app.models.user import DBUser, UserLogin, UserRegister, UserForgetPassword
from app.utils.bcrypt_pwd import hash_password, verify_password
from app.utils.main import generate_random

# 登录
def login(db: Session, user: UserLogin):
    db_user = db.query(DBUser).filter(DBUser.email == user.email).first()
    if not db_user:
        return {"code": 400, "msg": "用户不存在"}
    if not verify_password(user.password, db_user.password):
        return {"code": 400, "msg": "密码错误"}
    data = {
      "token": "123456",
      "user_id": db_user.id
    }
    return {"code": 200, "msg": "登录成功", "data": data, "success": True}


# 注册
def register(db: Session, user: UserRegister):
    # 检查用户是否存在
    check_email = db.query(DBUser).filter(DBUser.email == user.email).first()
    if check_email:
        return {"code": 400, "msg": "用户已存在"}

    db_user = DBUser(
        email=user.email,
        username=f'用户_{generate_random(6, "")}',
        password=hash_password(user.password),
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        return {"code": 400, "msg": f"注册失败：{e}"}
    
    return {"code": 200, "msg": "注册成功", "success": True}


# 忘记密码
def forget_password(db: Session, user: UserForgetPassword):
    # 检查用户是否存在
    check_email = db.query(DBUser).filter(DBUser.email == user.email).first()
    if not check_email:
        return {"code": 400, "msg": "用户不存在"}
    # 加密新密码
    new_password = hash_password(user.password)
    # 更新数据库
    check_email.password = new_password
    db.commit()
    return {"code": 200, "msg": "密码重置成功", "success": True}



