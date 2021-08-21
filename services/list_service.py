from models.list import List

# ALL ARE TAKEN CARE OF
# get all lists of a board
# get all cards in a list
# get all cards in a board

# get a list with list_id


class ListService:

    def __init__(self):
        self.lists = {}  # {"list_id", List object}
        self.cards = {}  # {"list_id": List of Cards[]}
        # self.lists = {}

    def add_list(self, trello_list):
        self.lists[trello_list.id] = trello_list

    def add_card_to_list(self, list_id, card):
        trello_list = self.lists[list_id]
        trello_list.add_card(card)
        if list_id not in self.cards:
            self.cards[list_id] = []
        self.cards[list_id].append(card)

    def get_cards(self, list_id):
        trello_list = self.lists[list_id]
        return self.trello_list.get_cards()

    # def add_list_to_board(self, board_id: str, list: List):
    #     if board_id not self.lists:
    #         self.list[board_id] = []
    #     self.lists[board_id].append(list)
