
from models.user import User


class Card:

    def __init__(self, id: str, name: str, created_by: User, assigned_to: User):
        self.id = id
        self.name = name
        self.created_by = created_by
        self.assigned_to = assigned_to
