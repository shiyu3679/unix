from app import create_app
import os

# 创建应用实例
app = create_app()

# 获取端口号，Render会通过环境变量提供
PORT = int(os.environ.get("PORT", 8000))

# 导出ASGI应用，供Vercel使用
def handler(event, context):
    import uvicorn
    return uvicorn.run(app, host="0.0.0.0", port=8000, lifespan="off")

# 保留本地开发的运行方式
if __name__ == "__main__":
    import uvicorn
    # 使用Render提供的端口或默认端口
    uvicorn.run(app, host="0.0.0.0", port=PORT)