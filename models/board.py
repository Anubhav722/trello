from typing import List, Dict

from models.user import User

class Board:

    def __init__(self, id: str, name: str, url: str, members: Dict[str, User]):
        self.id = id
        self.name = name
        self.url = url
        self.members = members
        self.is_private = False

    def add_user(self, user):
        self.members[user.id] = user

    def remove_user_from_board(self, user):
        del self.members[user_id]
