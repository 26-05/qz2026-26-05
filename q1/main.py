import json
import os

def analyze_log(filepath: str) -> dict:
    result = {
        "total": 0,
        "by_level": {},
        "by_user": {},
        "last_error": None
    }

    # 检查文件是否存在
    if not os.path.exists(filepath):
        return result

    # 打开文件
    try:
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

                # 统计总数
                result["total"] += 1

                # 统计 level，记录最后一条 ERROR 的 message
                level = my_dict.get("level")
                if level:
                    result["by_level"][level] = result["by_level"].get(level, 0) + 1
                    if level == "ERROR":
                        result["last_error"] = my_dict.get("message")

                # 统计 user
                user = my_dict.get("user")
                if user:
                    result["by_user"][user] = result["by_user"].get(user, 0) + 1

    # except保证正常进行
    except Exception:
        pass

    
    return result
