#!/bin/bash
# 确保脚本可执行
# chmod +x start.sh

# 安装依赖
pip install -r requirements.txt

# 运行应用
uvicorn main:app --host 0.0.0.0 --port $PORT