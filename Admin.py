from User import *


class Admin(User):
    def __init__(self, username, id, password):
        super().__init__(username, id, password)

    def display_menu_admin(self):
        print(
            "********MAIN MENU*********\n1)Add a new record file\n2)Add new semester\n3)Update\n4)Student statistics\n5)Global statistics\n6)Searching\n7)Exit")