from main import UserManager

# 根据题目行为示例进行测试
um = UserManager()
print(um.add_user("张三", 18))    # 期望: {'id': 1, 'name': '张三', 'age': 18}
print(um.add_user("李四", 20))    # 期望: {'id': 2, 'name': '李四', 'age': 20}
print(um.get_user(1))             # 期望: {'id': 1, 'name': '张三', 'age': 18}
print(um.get_user(99))            # 期望: None
print(um.update_age(1, 19))       # 期望: True
print(um.remove_user(2))          # 期望: True
print(um.remove_user(2))          # 期望: False
print(um.list_users())            # 期望: [{'id': 1, 'name': '张三', 'age': 19}]

# 保存与加载测试
um.save_to_json("users.json")
um2 = UserManager()
um2.load_from_json("users.json")
print(um2.list_users())           # 期望: [{'id': 1, 'name': '张三', 'age': 19}]
