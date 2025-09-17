from app import create_app

# 创建应用实例
app = create_app()

# 导出ASGI应用，供Vercel使用
def handler(event, context):
    import uvicorn
    return uvicorn.run(app, host="0.0.0.0", port=8000, lifespan="off")

# 保留本地开发的运行方式
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)