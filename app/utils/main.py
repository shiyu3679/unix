import random
import string

def generate_random(length: int = 6, prefix: str = "") -> str:
    """生成指定长度的随机字符串
    Args:
      length: 字符串长度，默认为6
    Returns:
      随机字符串
    """
    # 定义字符集：大小写字母 + 数字
    chars = string.ascii_letters + string.digits
    
    # 从字符集中随机选择字符
    random_string = ''.join(random.choice(chars) for _ in range(length))
    
    return prefix + random_string 
