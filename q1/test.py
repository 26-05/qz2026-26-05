from main import analyze_log

# ==========================================
# 示例 1：正常日志 (app.jsonl)
# ==========================================
with open("app.jsonl", "w", encoding="utf-8") as f:
    f.write('{"timestamp": "2026-10-01 10:23:45", "level": "INFO", "message": "用户登录成功", "user": "张三"}\n')
    f.write('{"timestamp": "2026-10-01 10:24:01", "level": "ERROR", "message": "数据库连接失败", "user": "李四"}\n')
    f.write('{"timestamp": "2026-10-01 10:25:12", "level": "INFO", "message": "用户登出", "user": "张三"}\n')
    f.write('{"timestamp": "2026-10-01 10:26:30", "level": "ERROR", "message": "超时", "user": "李四"}\n')
    f.write('{"timestamp": "2026-10-01 10:27:00", "level": "INFO", "message": "任务完成", "user": "王五"}\n')

result = analyze_log("app.jsonl")
print(result["total"])        # 5
print(result["by_level"])     # {'INFO': 3, 'ERROR': 2}
print(result["by_user"])      # {'张三': 2, '李四': 2, '王五': 1}
print(result["last_error"])   # 超时

# ==========================================
# 示例 2：文件不存在
# ==========================================
result = analyze_log("not_exist.jsonl")
print(result)

# ==========================================
# 示例 3：空文件
# ==========================================
# 文件存在但内容为空
with open("empty.jsonl", "w", encoding="utf-8") as f:
    pass

result = analyze_log("empty.jsonl")
print(result)

# ==========================================
# 示例 4：含格式错误的行 (bad.jsonl)
# ==========================================
# 文件内容：
# {"timestamp": "2026-10-01 10:23:45", "level": "INFO", "message": "ok", "user": "张三"}
# 这不是合法的 JSON
# {"timestamp": "2026-10-01 10:24:01", "level": "ERROR", "message": "失败", "user": "李四"}

with open("bad.jsonl", "w", encoding="utf-8") as f:
    f.write('{"timestamp": "2026-10-01 10:23:45", "level": "INFO", "message": "ok", "user": "张三"}\n')
    f.write('这不是合法的 JSON\n')
    f.write('{"timestamp": "2026-10-01 10:24:01", "level": "ERROR", "message": "失败", "user": "李四"}\n')

result = analyze_log("bad.jsonl")
print(result["total"])        # 2 (跳过格式错误行)
print(result["by_level"])     # {'INFO': 1, 'ERROR': 1}
print(result["last_error"])   # 失败
