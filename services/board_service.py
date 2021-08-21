from typing import List, Dict

from models.board import Board
from models.user import User
from services.list_service import ListService


# get all cards for a user in a board


class BoardService:

    def __init__(self, boards: Dict[str, Board]={}):  # board_id. Board
        self.boards = boards
        self.lists = {}  # {"board_id": List of lists[]}
        self.list_service = ListService()

    def is_user_authorized(self, user_id, board_id):  # This can be kept as a separate service.
        return True

    def add_board(self, user_id, board: Board):
        # if user_id is authenticated
        self.boards[board.id] = board

    def add_user_to_board(self, user_id, board_id, member):
        if not self.is_user_authorized:
            raise Exception("Invalid User")
        self.boards[board_id].add_user(member)

    # get all users in a board

    def add_list_to_board(self, board_id: str, trello_list: List):
        if board_id not in self.lists:
            self.lists[board_id] = []
        self.lists[board_id].append(trello_list)
        self.list_service.add_list(trello_list)

    def remove_list_from_board(self, board_id: str, list: List):
        self.lists[board_id].remove(list)

    def add_card_to_list(self, board_id: str, list_id: str, card):
        self.list_service.add_card_to_list(list_id, card)

    def delete_board(self, board_id):
        board = self.boards[board_id]
        del self.boards[board_id]

    def remove_user_from_board(self, board_id):
        pass

    def get_all_users_in_board(self, board_id):
        pass

    def get_all_lists(self, user_id, board_id):  # cached API
        pass

    def get_all_cards(self, user_id, board_id):  # cached API
        pass

    def get_all_boards(self, user_id):
        return self.boards
