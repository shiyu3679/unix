import bcrypt
# plain_password 明文密码
# hashed_password 哈希密码

# 生成密码哈希（加密过程）
def hash_password(plain_password):
    # 将明文密码转换为字节
    password_bytes = plain_password.encode('utf-8')
    
    # 生成盐值并哈希密码
    # bcrypt.gensalt() 会自动生成随机盐值
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    
    # 返回哈希后的密码（包含盐值）
    return hashed_password.decode('utf-8')

# 验证密码（检查密码是否匹配）
def verify_password(plain_password, hashed_password):
    # 将明文密码和哈希密码都转换为字节
    password_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    
    # 验证密码
    # bcrypt 会从哈希值中提取盐值并重新计算哈希进行比较
    return bcrypt.checkpw(password_bytes, hashed_bytes)

# 示例用法
if __name__ == "__main__":
    # 原始密码
    password = "my_secure_password123"
    
    # 哈希加密
    hashed = hash_password(password)
    print("哈希后的密码:", hashed)
    
    # 验证正确密码
    is_valid = verify_password(password, hashed)
    print("密码验证（正确密码）:", is_valid)  # 输出 True
    
    # 验证错误密码
    is_valid_wrong = verify_password("wrong_password", hashed)
    print("密码验证（错误密码）:", is_valid_wrong)  # 输出 False
    