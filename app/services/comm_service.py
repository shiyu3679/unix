import random
from app.utils.useRedis import set_redis
from app.models.comm import SendCode

# 发送验证码
def send_code(data: SendCode):
    if not data.email or not data.code_type:
        return {"code": 400, "msg": "参数错误: email或code_type不能为空", "success": False}
    try:
        # 生成的验证码
        code = random.randint(1000, 999999)
        res = set_redis(generate_key(data.code_type, data.email), code, 300)
        if res:
            return {"code": 200, "msg": "发送成功", "success": True}
        else:
            return {"code": 500, "msg": "发送失败", "success": False}
    except:
        return {"code": 500, "msg": "发送失败", "success": False}


# 生成 key
def generate_key(code_type: str, email: str):
    return f"{code_type}:{email}"
