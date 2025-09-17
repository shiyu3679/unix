from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import user, sign, comm, order

from app.database import engine, Base

def create_app():
    # 创建数据库表
    Base.metadata.create_all(bind=engine)

    # 初始化FastAPI应用
    app = FastAPI(
        title="模块化FastAPI应用",
        description="使用蓝图实现的模块化FastAPI应用",
        version="1.0.0"
    )

    # 可选：配置静态文件目录
    app.mount("/static", StaticFiles(directory="app/static"), name="static")

    # 注册蓝图
    app.include_router(user.router, prefix="/user", tags=["用户管理"])
    app.include_router(sign.router, prefix="/sign", tags=["登录注册"])
    app.include_router(comm.router, prefix="/comm", tags=["公共方法"])
    app.include_router(order.router, prefix="/order", tags=["订单管理"])

    
    return app