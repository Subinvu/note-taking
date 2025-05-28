import json
import os
from models.user import User

class UserManager:
    def __init__(self, file_path="data/users.json"):
        self.file_path = file_path
        self.users = []
        self.load_users()

    def load_users(self):
        if not os.path.exists(self.file_path):
            self.users = []
            return

        with open(self.file_path, "r") as f:
            data = json.load(f)
            self.users = [User.from_dict(user) for user in data]

    def save_users(self):
        with open(self.file_path, "w") as f:
            json.dump([user.to_dict() for user in self.users], f, indent=4)

    def authenticate(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None
    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
