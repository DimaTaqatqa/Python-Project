class User:
    def __init__(self, username, id, password):
        self.username = username
        self.id = id
        self.password = password

    def set_username(self, username):
        self.username = username

    def set_id(self, id):
        self.id = id

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username
