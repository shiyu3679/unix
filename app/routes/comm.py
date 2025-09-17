from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime
from app.services.comm_service import send_code
from app.models.comm import SendCode

router = APIRouter()
# 模板公共路径
templates = Jinja2Templates(directory="app/templates")

@router.get("/user-profile")
def user_profile(request: Request):
    # 模拟用户数据
    user = {
        "name": "张三",
        "email": "zhangsan@example.com",
        "age": 30,
        "hobbies": ["阅读", "旅行", "运动"]
    }
    
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "用户 profile",
            "user": user,
            "now": datetime.now()
        }
    )
# 发送验证码
@router.post("/send_code", name="发送验证码")
def send_code_email(data: SendCode):
    return send_code(data)
