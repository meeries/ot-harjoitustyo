from entities.user import User

class UserRepository:

    def __init__(self):
        pass

    def create_user(self, user):
        self.user = user
        users = []
        users.append(user)
        

    def findby_username(self, username):
        self.username = username
