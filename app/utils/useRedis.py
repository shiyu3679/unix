import redis
from app.config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_USER

# 1. 创建连接（默认参数）
r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True,
    username=REDIS_USER,
    password=REDIS_PASSWORD,
)

# 存储数据
def set_redis(key, value, ex=60):
    r.set(key, value, ex=ex)
    return {"code": 200, "msg": "设置成功", "success": True}

# 获取数据
def get_redis(key):
    value = r.get(key)
    if value:
        return {"code": 200, "msg": "获取成功", "success": True, "data": value.decode()}
    else:
        return {"code": 404, "msg": "键不存在", "success": False}

# 删除数据
def del_redis(key):
    r.delete(key)
    return {"code": 200, "msg": "删除成功", "success": True}

# 2. 测试连接（发送 ping 命令，返回 b'PONG' 表示连接成功）
print(r.ping())  # 输出：b'PONG'（若 decode_responses=True，输出 'PONG'）