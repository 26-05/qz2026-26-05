import json
import os

class UserManager:
    def __init__(self):
        self.roster = {}
        # 记录下一个可用的id，从1开始
        self.id_counter = 1

    def id_user(self, id):
        # 找不到就返回None
        return self.roster.get(id, None)
