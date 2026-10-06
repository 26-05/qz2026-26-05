import json
import os

class UserManager:
    def __init__(self):
        self.roster = {}
        # 记录下一个可用的id，从1开始
        self.id_counter = 1

    def get_user(self, user_id):
        # 找不到就返回None
        return self.roster.get(user_id, None)
    def add_user(self, name, age):
        user_info = {"id": self.id_counter, "name": name, "age": age}
        self.roster[self.id_counter] = user_info
        self.id_counter += 1
        return user_info

    def update_age(self, user_id, new_age):
        # 先确认这个 id 在花名册里
        if user_id in self.roster:
            self.roster[user_id]["age"] = new_age
            return True
        return False

    def remove_user(self, user_id):
        # 删掉之前确认 id 存在
        if user_id in self.roster:
            del self.roster[user_id]
            return True
        return False
    def list_users(self)：
        return list(self.roster.values())
