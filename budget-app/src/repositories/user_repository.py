from entities.user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return[User(row["username"], row["password"]) for row in rows]

    user_repository = UserRepository(get_database_connection())
    users = user_repository.find_all()

    def create_user(self, user):
        self.user = user
        users = []
        users.append(user)

    def findby_username(self, username):
        self.username = username
