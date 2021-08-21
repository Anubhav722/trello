from typing import Dict, List

from models.card import Card


class List:

    def __init__(self, id: str, name: str, board_id: str, cards: Dict[str, List[Card]]={}):
        self.id = id
        self.name = name
        self.cards = cards  # {"card_id": Card obj}
        self.board_id = board_id

    def add_card(self, card):
        self.cards[card.id] = card

    def get_all_cards(self):
        return self.cards
