from typing import List

from services.board_service import BoardService
from services.authentication_service import AuthenticationService


class Trello:

    def __init__(self, board_service, authentication_service=None):
        # self.search_service = SearchService()
        self.authentication_service = authentication_service
        self.board_service = board_service

    def add_board(self, user_id, board):
        self.board_service.add_board(user_id, board)

    def add_user_to_board(self, user_id, board_id, user):
        self.board_service.add_user_to_board(user_id, board_id, user)

    def remove_user_from_board(self, user_id, board_id):
        self.board_service.remove_user_from_board()

    def add_list_to_board(self, board_id, list):
        self.board_service.add_list_to_board(board_id, list)

    def add_card_to_list(self, board_id, list_id, card):
        self.board_service.add_card_to_list(board_id, list_id, card)



from models.board import Board
from models.user import User
from models.list import List
from models.card import Card

user_1 = User(1, "Anubhav", "Singh", "a@x.com")
user_2 = User(2, "Satyam", "Gupta", "g@x.com")

board = Board('goa', 'goa-board', 'check', {1: user_1})

board_service = BoardService()

trello = Trello(board_service=board_service)
trello.add_board(1, board)
trello.add_user_to_board(5, "goa", user_2)

# ADDING LIST
list1 = List('list-1', "China", "goa")
list2 = List('list-2', "India", "goa")
trello.add_list_to_board('goa', list1)
trello.add_list_to_board('goa', list2)

# import ipdb; ipdb.set_trace()

# ADDING CARD TO LIST

card1 = Card('card-1', 'fix this', user_1, user_2)

trello.add_card_to_list('goa', 'list-1', card1)

print (trello.get_all_cards())