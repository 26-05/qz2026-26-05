import json
import os

def analyze_log(filepath: str) -> dict:
    result = {
        "total": 0,
        "by_level": {},
        "by_user": {},
        "last_error": None
    }
    
    # 检查文件存不存在
    if not os.path.exists(filepath):
        return result
        
    # 打开文件
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            # 跳过空行
            line = line.strip()
            if not line:
                continue

    # 解析 JSON，失败不报错
            try:
                my_dict = json.loads(line)
            except json.JSONDecodeError:
                continue
            
    return result
